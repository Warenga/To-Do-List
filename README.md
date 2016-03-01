
<strong># To Do List Application</strong>

A simple to do list application that allows management of tasks.

Written in <strong>python language</strong> using <strong>flask framework</strong>. The UI is <strong>Jinja2 templates</strong> incorporated in <strong>flask twitter-bootstrap</strong>. The database is <strong>SQLAlchemy</strong> in <stong>SQlite</stong>.


Click <a href="http://tolist-staging.herokuapp.com/"> here</a> to view the staged version.


### What it does
------------------------------------------------

	1. New User Registration
	2. User Sign In
	3. Allow user to create a list (Collection of Cards)
	4. User can add tasks to a list
	5. Tasks can be checked done

	### What needs to be added
	----------------------------------------------

		1. Login with Facebook or Twitter options
		2. Task reminder
		3. Sharing of tasks
		4. Sending tasks to email



### Run it locally
--------------------------------------------------
Have python 2.7 or 3 installed in your machine

<strong=>Clone this repository</strong>
	https://github.com/Warenga/To-Do-List.git

<strong>Create a virtualenv</strong>

<strong>Install the requirements</strong>

	```$pip install -r requirements.txt```

<strong>Initialize the database</strong>

	```$pip manage.py db init```

<strong>Construct and upgrade the database</strong>

	```$ python manage.py db upgrade```

<strong>Run the server</strong>

	```$ python manage.py runserver```

Enjoy!


		

