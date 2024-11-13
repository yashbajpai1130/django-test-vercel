echo "Building files -------"
python3 -m pip install -r requirements.txt

echo "Migrating -------"
python3 manage.py makemigrations
python3 manage.py migrate