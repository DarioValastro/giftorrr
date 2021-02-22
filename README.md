# Giftor

## Installation Procedures

Following the next steps to run the code of Giftor on your device

* Clone GitHub project on your device through this link: https://github.com/DarioValastro/giftorrr.git 

* Create your environment using Virtualenv within the project folder with Python as base interpreter (interpreter during implementation was Python 3.8) 

* Install all required modules given in the file requirements.txt through Python Terminal thank to pip package installer 

* Log the giftor.sql in MySQL Workbench or something like that to copy the DB in your PC and set name of DB, password and user's name 

* Modify, in the app.py file, the line 32
	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:' +os.environ['pass_db']+'@localhost/Giftor'
The root is the name of the user for DB
+ "Password of DB" set by the user 
/name_of_DB

* Modify the os.environ --> edit configurations and modify the password for DB and for Gmail 
	The Gmail's password is the Google password's app set for the device by the Gmail security services


