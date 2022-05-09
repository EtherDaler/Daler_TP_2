import requests
import os
import pytest
import json
from weather_03.weather_wrapper import WeatherWrapper, BASE_URL, FORECAST_URL
import unittest
from unittest import mock
from unittest.mock import Mock


API_KEY = ""
CITY_M = "Moscow"
CITY_D = "Dushanbe"

def requests_get(*args, **kwargs):
    if args[0] == BASE_URL:
        mock_test = Mock(status_code=200)
        mock_test.json.return_value = {"name": CITY_M, 'main': {'temp': 19}}
        return mock_test
    if args[0] == FORECAST_URL:
        mock_test = Mock(status_code=200)
        mock_test.json.return_value = {
            'list': [
                {0: 'smth'},
                {1: 'smth'},
                {2: 'smth'},
                {3: 'smth'},
                {4: 'smth'},
                {5: 'smth'},
                {6: 'smth'},
                {'main': {'temp': 6.66}}]}
        return mock_test
    mock_test = Mock(status_code=400)
    mock_test.json.return_value = None
    return mock_test


@mock.patch('requests.get', side_effect=requests_get)
def test_weather_get(mock_get):
    global API_KEY, CITY_M
    tmp = WeatherWrapper(API_KEY).get_temperature(CITY_M)
    response = WeatherWrapper(API_KEY).get_response_city(CITY_M, BASE_URL)
    assert [response["name"], tmp] == [CITY_M, response["main"]["temp"]]


@mock.patch('requests.get', side_effect=requests_get)
def test_city_error(mock_get):
    global API_KEY, CITY_M
    with pytest.raises(AttributeError) as e:
        WeatherWrapper(API_KEY).get_response_city(CITY_M, '1')
    assert str(e.value) == 'Incorrect city'


@mock.patch('requests.get', side_effect=requests_get)
def test_weather_get_diff_string(mock_get):
    global API_KEY, CITY_M, CITY_D
    data = WeatherWrapper(API_KEY).find_diff_two_cities(CITY_M, CITY_D)
    s_wait_data = f'Weather in {CITY_M} is warmer than in {CITY_D} by {data} degrees'
    s_data = WeatherWrapper(API_KEY).get_diff_string(CITY_M, CITY_D)
    assert s_wait_data == s_data


def tomorrow_diff(city, temp1, temp2):
    mock_test_1 = Mock(status_code=200)
    mock_test_1.json.return_value = {
        'list': [{0: 'smth'},
                 {1: 'smth'},
                 {2: 'smth'},
                 {3: 'smth'},
                 {4: 'smth'},
                 {5: 'smth'},
                 {6: 'smth'},
                 {'main': {'temp': temp1}}
                 ]}
    mock_test_2 = Mock(status_code=200)
    mock_test_2.json.return_value = {"name": city, 'main': {'temp': temp2}}
    return [mock_test_1, mock_test_2]

@mock.patch('requests.get')
def test_weather_get_tomorrow_diff(fake_request):
    global API_KEY, CITY_M
    res = []
    data = {(18,19), (19, 18), (18, 18), (18, 22), (22, 18)}
    wait_data = [
        "The weather in Moscow tomorrow will be colder than today",
        "The weather in Moscow tomorrow will be warmer than today",
        "The weather in Moscow tomorrow will be the same than today",
        "The weather in Moscow tomorrow will be much colder than today",
        "The weather in Moscow tomorrow will be much warmer than today"
    ]
    weather = WeatherWrapper(API_KEY)
    for i in range(len(data)):
        fake_request.side_effect = tomorrow_diff(CITY_M, data[i][0], data[i][1])
        response = weather.get_tomorrow_diff(CITY_M)
        res.append(response)
    assert wait_data == res