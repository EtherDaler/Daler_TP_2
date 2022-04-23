FROM ubuntu

LABEL maintainer="khodzhimatov.di@phystech.edu"

ENV TZ=Europe/Moscow

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN mkdir opt/techprog

ENV USER = "tp2022user"

COPY . opt/techprog

WORKDIR /opt/techprog

RUN apt-get update -y

RUN apt-get install -y make cmake python3 python3-pip

RUN pip install --upgrade pip

RUN pip install Flask

RUN cd /opt/techprog && mkdir build && cd build &&  cmake .. && make

RUN useradd -m -s /bin/bash tp2022user

USER tp2022user

EXPOSE 5000

RUN ["export", "FLASK_APP=opt/techprog/app.py:app"]

CMD ["flask", "run", "--port", "8898", "--host", "0.0.0.0"]
