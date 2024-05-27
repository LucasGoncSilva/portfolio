# Installs dependencies
pip3 install -r requirements.txt

# Collects staticfiles
python3 manage.py collectstatic --no-input

# Handles DB migrations
python3 manage.py makemigrations
python3 manage.py migrate
