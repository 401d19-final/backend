# Code Overflow- backend
## Team Members
- Ben Small
- Yu-Wei Hsieh
- Shade Greene
- Alec Torres
- Ryan McMillan
- Rui Guo

## Start the APP
Run ``python manage.py runserver`` to start the APP.

## APIs
- ``http://127.0.0.1:8000/question`` Get/Create all questions data
- ``http://127.0.0.1:8000/question/<int: pk>/`` Update/Delete specific question data
- ``http://127.0.0.1:8000/comment/<int: pk>/`` Get/Update/Delete specific comment
- ``http://127.0.0.1:8000/question/<int: pk>/comment`` Get/Create specific comment for a question
- ``http://127.0.0.1:8000/comment/<int: pk>/`` Create a specific user
- ``http://127.0.0.1:8000/comment/<int: pk>/`` Get/Update/Delete a user