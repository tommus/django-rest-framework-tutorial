# Django REST Framework tutorial

Tutorial walk-through.

## Backend management

1. Create virtual environment:

    > virtualenv venv -p python3

2. Activate virtual environment:

    > source venv/bin/activate

3. Install requirements

    > pip install -r requirements.txt

## Database synchronization

1. When executing server for the first time, you have to synchronize database (and execute migrations):

    > python manage.py migrate

## Running server

1. Make sure the virtual environment has been activated:

    > source venv/bin/activate

2. Start server by typing:

    > python manage.py runserver \<address\>:\<port\>

- I.e. start server at port 8000 to listen for connections from whatever source:

    > python manage.py runserver 0.0.0.0:8000

## Credentials

Example credentials for superuser:

| Login    | Password      |
| -------- | ---------- |
| admin    | quickstart |
| user     | quickstart |
