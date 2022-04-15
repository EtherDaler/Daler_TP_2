import requests
import os
import pytest
import json
from weather_03.weather_wrapper import WeatherWrapper, BASE_URL, FORECAST_URL


API_KEY = "562b6c52f5910dd54c80f6d31c0b9979"


def weather(url, city):
    global API_KEY
    return requests.get(
        url=url,
        params={
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }
    ).json()


def test_weather_get():
    global API_KEY
    city = "Moscow"
    response = requests.get(
        BASE_URL,
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }
    )
    data = json.loads(response.text)
    w = WeatherWrapper(API_KEY)
    j_w = json.loads(w.get("Moscow", BASE_URL).text)
    assert data == j_w


def test_city_error():
    global API_KEY
    city = "Umpalumpalend"
    try:
        WeatherWrapper(API_KEY).get_response_city(city, BASE_URL)
    except AttributeError as e:
        assert 1 == 1


def test_weather_get_diff_string():
    city1 = "Dushanbe"
    city2 = "Moscow"
    city3 = "Oymyakon"
    dif1 = int(abs(WeatherWrapper(API_KEY).find_diff_two_cities(city1, city2)))
    dif2 = int(abs(WeatherWrapper(API_KEY).find_diff_two_cities(city3, city1)))
    kwargs = {
        'first': f'Weather in {city1} is warmer than in {city2} by {dif1} degrees',
        'second': f'Weather in {city3} is colder than in {city1} by {dif2} degrees'
    }
    f_kwargs = {
        'first': WeatherWrapper(API_KEY).get_diff_string(city1, city2),
        'second': WeatherWrapper(API_KEY).get_diff_string(city3, city1)
    }
    assert kwargs == f_kwargs


def test_weather_get_tomorrow_diff():
    citys = ["Moscow", "Dushanbe", "Oymyakon", "London", "Los Angeles"]
    kwargs = {}
    for i in citys:
        tomorrow = weather(FORECAST_URL, i)['list'][7]['main']['temp']
        today = weather(BASE_URL, i)['main']['temp']
        diff = tomorrow - today
        if diff > 3:
            response = 'much warmer'
        elif diff > 0.5:
            response = 'warmer'
        elif diff < -3:
            response = 'much colder'
        elif diff < -0.5:
            response = 'colder'
        else:
            response = 'the same'
        kwargs[i] = f'The weather in {i} tomorrow will be {response} than today'
    f_kwargs = {}
    for i in citys:
        f_kwargs[i] = WeatherWrapper(API_KEY).get_tomorrow_diff(i)
    assert kwargs == f_kwargs