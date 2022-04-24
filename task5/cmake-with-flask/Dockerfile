FROM ubuntu:latest

LABEL maintainer="khodzhimatov.di@phystech.edu"

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ENV ADMIN=tp2022user

RUN apt-get update

RUN apt-get install -y make cmake python3 python3-pip

RUN pip install --upgrade pip

RUN pip install Flask

RUN mkdir opt/techprog

COPY . opt/techprog

WORKDIR /opt/techprog

RUN cd /opt/techprog && cmake . && make

RUN useradd -m -s /bin/bash $ADMIN

USER $ADMIN

CMD ["python3", "opt/techprog/app.py", "--port", "8898", "--host", "0.0.0.0"]