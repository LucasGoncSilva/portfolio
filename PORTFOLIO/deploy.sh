#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate

pip3 install uv
uv sync --no-group dev; uv run manage.py collectstatic --no-input; uv run manage.py makemigrations; uv run manage.py migrate
