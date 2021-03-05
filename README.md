### Steps to run the application
* Make sure Python and PIP is installed. 
* Open terminal and run command
`pip install -r requirements.txt`
* Once the packages are installed, run command to create database
  `python manage.py migrate`
* Once the DB is created start the server using command `python manage.py runserver`
* Open browser and hit url `http:\\127.0.0.1:8000\`