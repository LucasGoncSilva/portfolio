#!/bin/bash

pip3 install uv
python3 -m uv -h

uv sync --no-group dev

find manage.py

uv run manage.py collectstatic --no-input
uv run manage.py makemigrations
uv run manage.py migrate
