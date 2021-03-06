# Social todo number 2!

This app was written using Django and, consequently, Python.

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

To access the functioning website, go to

```
https://social-todo-part-2-gabrielmosquera1.c9users.io
```
If the link is not working, please email gabriel.simoes@yale.edu

The app should pass all tests but, sometimes, it fails the "name too short test"

for no apparent reason. If you try manually, you'll see the right tag.
