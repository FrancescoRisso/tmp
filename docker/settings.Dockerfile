FROM python:3.7

WORKDIR /settings

RUN apt update && apt -y install nano

COPY ./waitUpdatingSettings.py ./updateSettings.py

CMD python3 ./updateSettings.py
