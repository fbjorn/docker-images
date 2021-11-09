FROM python:3.9.4-alpine3.13

ENV \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PATH="/root/.poetry/bin:${PATH}" \
    POETRY_URL="https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py" \
    POETRY_HOME="/.venv" \
    POETRY_VERSION="1.1.6" \
    PYTHONUNBUFFERED=1 \
    TZ="UTC" \
    WORKON_HOME="/.venv" \
    ENV_LAST_LINE="LEAVE-ME-HERE"

RUN apk add \
    curl \
    g++ \
    gcc \
    linux-headers \
    make \
    musl-dev \
    postgresql-dev \
    python3-dev \
    && curl -sSL ${POETRY_URL} -o /tmp/get-poetry.py \
    && python /tmp/get-poetry.py --version ${POETRY_VERSION} \
    && poetry config virtualenvs.in-project false \
    && poetry config virtualenvs.path ${WORKON_HOME}

WORKDIR /src/