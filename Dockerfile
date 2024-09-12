FROM python:3.12-slim

WORKDIR /app

RUN pip install pipenv

COPY data/clean_data.csv data/clean_data.csv
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --deploy --ignore-pipfile --system

COPY recommendation_eat_assistant_flask .

EXPOSE 5000

CMD gunicorn --bind 0.0.0.0:5000 app:app