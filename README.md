# PythonDataBackend
Server for fetching and inputting football records written using Django

1. To run this server you will need pip first and foremost
> http://pip.readthedocs.org/en/stable/installing/#python-os-support

2. You will preferably want a virtual python environment (in case you have other python projects that have other dependencies):
 ```sh
 $ cd <my_project_folder>
 $ virtualenv venv
 $ source activate venv #If this doesn't work on mac try 'source venv/bin/activate' on windows...you're SOL
 ```
 
More details about the process can be found here:
> http://docs.python-guide.org/en/latest/dev/virtualenvs/

3. Next you will need to install django-restframework specific dependencies: 
 ```sh
 $ pip install django
 $ pip install djangorestframework
 $ pip install pygments
 $ pip install django-filter
 ```

4. To run the server AFTER setting up dependencies, switch to the tutorial directory:
 ```sh
 $ python manage.py runserver
 ``` 
