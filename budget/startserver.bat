@ECHO OFF
REM activate the budget virtual environment and start the development server

workon moneyhog & cd C:\Users\sjbober\Documents\Projects\moneyhog & py manage.py runserver
PAUSE