#!/usr/bin/env bash
source .env

docker build -t "$APP_NAME" .
