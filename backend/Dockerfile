FROM python:3.11.5-slim as python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    POETRY_NO_ANSI=1

ENV PATH="$POETRY_HOME/bin:$PATH"

RUN apt-get update && apt-get install --no-install-recommends -y curl


FROM python-base as builder-base
RUN apt-get update && apt-get install --no-install-recommends -y build-essential
RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /app/backend
COPY . ./

RUN poetry install --only main


FROM python-base as dev-stage
COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base /app/backend /app/backend

WORKDIR /app/backend
RUN poetry install


FROM python-base as prod-stage
COPY --from=builder-base /app/backend /app/backend

WORKDIR /app/backend
