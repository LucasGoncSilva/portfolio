# Installs uv
pip3 install uv

# Sync dependencies
uv sync --no-group dev

# Collects staticfiles
uv run manage.py collectstatic --no-input

# Handles DB migrations
uv run manage.py makemigrations
uv run manage.py migrate
