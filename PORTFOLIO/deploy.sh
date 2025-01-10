#!/bin/bash

pip3 install uv
python3 -m uv sync --no-group dev
python3 -m uv run manage.py collectstatic --no-input
python3 -m uv run manage.py makemigrations
python3 -m uv run manage.py migrate
python3 -m uv pip compile pyproject.toml -o requirements.txt
