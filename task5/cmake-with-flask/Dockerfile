FROM ubuntu:20.04

LABEL maintainer="khodzhimatov.di@phystech.edu"

ENV TZ=Europe/Moscow

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN mkdir opt/techprog

ENV ADMIN=tp2022user

COPY . opt/techprog

WORKDIR ./opt/techprog

RUN apt-get update

RUN apt-get install -y make cmake python3 python3-pip g++

RUN pip install --upgrade pip

RUN pip install Flask

RUN cd /opt/techprog && mkdir build && cd build &&  cmake .. && make

RUN useradd -m -s /bin/bash $ADMIN

USER $ADMIN

EXPOSE 5000

CMD ["python3", "opt/techprog/app.py", "--port", "8898", "--host", "0.0.0.0"]