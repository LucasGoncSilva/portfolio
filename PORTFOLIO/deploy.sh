#!/bin/bash

pip3 install uv

exec $SHELL

uv sync --no-group dev

uv run manage.py collectstatic --no-input
uv run manage.py makemigrations
uv run manage.py migrate
