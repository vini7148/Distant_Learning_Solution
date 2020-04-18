@echo off

env/Scripts/activate

cd main

python manage.py runserver
