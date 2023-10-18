# Simple Python API v2
Adam Owada

## Description

A proof of concept Python API intended for demonstration purposes for Python 401 - Module 2. This would be great
starter code for students to modularize for their lab (maybe lab 06?). 

## Technologies Used

- Python's `http.server` module from the standard library
- SQLAlchemy ORM
- SQLite database

## Instructions

1. Create and start virtual environment, pip install from requirements.txt
2. Start the server `$ python server.py` (which creates the `users` table if not already present)
3. Make a POST curl request, for example:

`$ curl -X POST -H "Content-Type: application/json" -d '{"name": "Adam", "age": 34}' http://localhost:8000/create_user`

4. Option: View the `users` table using PyCharm

## Next Steps

- Modularize
- Write tests with `pytest` and `requests` libraries
- Create more tables
- Create more endpoints
- Full CRUD capabilities
- Deploy to AWS EC2 instance
