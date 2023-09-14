FROM node:20-slim as node-base


FROM node-base as builder-base
WORKDIR /app/frontend
COPY package*.json .

RUN npm install --omit=dev


FROM node-base as dev-stage
COPY --from=builder-base /app/frontend /app/frontend

WORKDIR /app/frontend
COPY . .
RUN npm install --include=dev


FROM node-base as prod-stage
COPY --from=builder-base /app/frontend /app/frontend

WORKDIR /app/frontend
RUN npm ci --only=production
