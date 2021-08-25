FROM python:3.8
WORKDIR /app

ENV PYTHONPATH /app
ENV LC_ALL=C.UTF-8 LANG=C.UTF-8

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    vim \
    xz-utils \
    && rm -rf /var/lib/apt/lists/*
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip install --upgrade pip setuptools wheel
RUN python3 -m pip install --upgrade pip setuptools wheel

RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry config virtualenvs.in-project true

COPY pyproject.toml pyproject.toml
RUN poetry install

COPY . /app


CMD ["pserve", "production.ini", "--reload"]
