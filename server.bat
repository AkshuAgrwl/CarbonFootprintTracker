@ECHO OFF

SET function=%1
SET environment=%2

IF "%function%" == "up" (
    GOTO :StartServer
) ELSE IF "%function%" == "down" (
    GOTO :StopServer
)

:StartServer
IF "%environment%" == "dev" (
    docker compose --env-file .env.dev -f docker-compose.yaml -f docker-compose.dev.yaml up
) ELSE IF "%environment%" == "prod" (
    docker compose --env-file .env.prod -f docker-compose.yaml -f docker-compose.prod.yaml up
)
EXIT /B 0

:StopServer
docker compose down
EXIT /B 0
