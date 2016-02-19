# Social todo Django starter code

We wrote this in office hours. It defines the models for tasks,
migrations, etc. It is based on the 
[Django tutorial](https://docs.djangoproject.com/en/1.9/intro/).

To install this on c9, clone the repository. Then, before you run it
for the first time, you'd do

```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
This installs your Python dependencies. Then you need to run your database
migrations with 

```
python manage.py migrate
```

This will create a file called `db.sqlite3`, which is ignored in your
`.gitignore` file. 

Now you're ready to run the application.Then you can run it with the following

```
python manage.py runserver 0.0.0.0:$PORT
```

Then you can click "Preview" in the c9 interface to see your running application.