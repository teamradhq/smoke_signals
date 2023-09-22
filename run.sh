#!/usr/bin/env bash
source .env

docker run \
    -e MOCK_GPIO="$MOCK_GPIO" \
    -v .:"$WORK_DIR" \
    -w "$WORK_DIR" \
    -it "$APP_NAME" python "run.py"
