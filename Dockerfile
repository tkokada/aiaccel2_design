FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install netcat gcc \
    && apt-get clean

WORKDIR /code

COPY ./pyproject.toml ./poetry.lock* /code

RUN pip install --upgrade pip

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-dev

COPY . /code

CMD ["poetry", "run", "uvicorn", "aiaccel2.main:app", "--host", "0.0.0.0", "--port", "8080"]

