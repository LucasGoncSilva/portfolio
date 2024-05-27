# Sets to exit on error
set -o errexit

# Installs dependencies
pip3 install -r requirements.txt

# Collects staticfiles
python3 manage.py collectstatic --no-input

# Handles DB migrations
python3 manage.py makemigrations
python3 manage.py migrate


# set -o errexit; pip install -r requirements.txt; python manage.py collectstatic --no-input; python manage.py makemigrations; python manage.py migrate

