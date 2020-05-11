@ECHO OFF
REM activate the budget virtual environment and start the development server

workon budget & cd C:\Users\sjbober\Documents\Projects\budget\budgetme & py manage.py runserver
PAUSE