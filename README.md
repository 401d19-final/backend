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
- ``~/question`` GET/CREATE all questions data
- ``~/question/<int: pk>/`` UPDATE/DELETE specific question data
- ``~/comment/<int: pk>/`` GET/UPDATE/DELETE specific comment
- ``~/question/<int: pk>/comment`` GET/CREATE specific comment for a question
- ``~/user/create/`` CREATE a specific user
- ``~/user/<int: pk>`` GET/UPDATE/DELETE a user
