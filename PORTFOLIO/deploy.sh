#!/bin/bash

pip3 install uv

exec uv sync --no-group dev
exec uv run manage.py collectstatic --no-input
exec uv run manage.py makemigrations
exec uv run manage.py migrate
