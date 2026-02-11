# join-backend
Join is a task management system. This is the backend part with Django Rest Framework an Python. You'll find the frontend part in my repositories:

https://github.com/Rebell180/join-frontend

Setup: 

To start with this project you have to do some steps. 
Open the console (Ctrl + ö).

Step 1: 
Install all required libraries. 

pip install -r requirements.txt


Step 2:
Initialize database.

python migrate


Step 3: 
Fill in the required data to '.env.template' and rename it to '.env'.


Step 4: 
create an superuser for django admin panel. Enter the following code into command line and fill up the requested data.

python manage.py createsuperuser


Step 5:
Start the backend server.

python manage.py runserver