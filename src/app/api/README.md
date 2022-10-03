# Requirements
This is a python web-based API. In order to run this you will need a Python 3.7 version or later.

## Python Version
Windows/Bash:
```bash
$ python --version
Python 3.10.2
```
MacOs/Linux:
```terminal
$ python3 --version
Python 3.8.10
```

## FastAPI installation
```bash
$ pip install fastapi
...
$ pip install uvicorn
...
$ pip install starlette
```
These are the three main packages you will need to use the API. If you are coding in Pycharm or another text editer you can go to the requirements.txt and click install all.

## Windows/Bash Set Up:
```bash
$ cd src

$ export PYTHONPATH="$PWD/app/api/routes"

$ python uvicorn -m app.api.routes.controller:app --reload
```

After running the above commands you should be able to access the web-api using (this link)[http://localhost:8000/docs#/] as long as the port number was not changed. If you changes the port number user the port tag.

## MacOS/Linux Set Up:
```terminal
$ cd src

$ python3 uvicorn -m app.api.routes.controller:app --reload
```
If you get a path not found error you may have to declare the PYTHONPATH environment variable. Otherwise the link to the webapi should be your http://{<b>your_ip_address</b>}:8000/docs#/. This assumes you did not change the port.

## How To Use:
Any changes made to the backend of the API do not automatically translate to the API. Remember to always reload the the page as soon as you make a change. Also check the [documentation for FastAPI](https://fastapi.tiangolo.com/) for information on how to fill out the API.
