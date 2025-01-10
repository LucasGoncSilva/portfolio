pip3 install uv

bash -c "uv sync --no-group dev; uv run manage.py collectstatic --no-input; uv run manage.py makemigrations; uv run manage.py migrate;"
