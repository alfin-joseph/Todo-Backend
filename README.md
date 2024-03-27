Django REST Application
This Django application serves as a RESTful API backend for managing todos.

Installation
Requirements
Python 3.x
Django
Django REST Framework
Other dependencies (listed in requirements.txt)
Installation Steps

Installation Steps

1 .Clone the repository:
git clone https://github.com/yourusername/django-rest-todo.git

2. Navigate to the project directory:
cd django-rest-todo

3.Create a virtual environment (optional but recommended):
python3 -m venv venv

4.Activate the virtual environment:
venv\Scripts\activate

5.Install dependencies:
pip install -r requirements.txt

6.Apply migrations:
python manage.py migrate

7.Create super user
pyhton manage.py createsuperuser 

8.Start the Django development server:
python manage.py runserver

ALL the end points of this application can be view at http://localhost:8000/swagger/
