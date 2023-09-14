#!/bin/bash
set -e


# api database initialization

psql -v ON_ERROR_STOP=1 --username ${POSTGRES_USER} <<-EOSQL
    CREATE USER ${BACKEND__DJANGO_POSTGRES_DB_USER} WITH PASSWORD '${BACKEND__DJANGO_POSTGRES_DB_PASSWORD}';
    CREATE DATABASE ${BACKEND__DJANGO_POSTGRES_DB_NAME};
    GRANT ALL PRIVILEGES ON DATABASE ${BACKEND__DJANGO_POSTGRES_DB_NAME} to ${BACKEND__DJANGO_POSTGRES_DB_USER};
EOSQL