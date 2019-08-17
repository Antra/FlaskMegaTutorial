# FlaskMegaTutorial
Following the Flask Mega Tutorial by Miguel Grinberg
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

## Python mailserver
For debugging purposes, it can be handy to let Python listen for mailserver requests, e.g. to listen on port 8025:

```python -m smtpd -n -c DebuggingServer localhost:8025```

# Other notes
## VS Code re-breaks import statements
Fix for VS Code moving ```from app import routes, models``` up to the top of the file.

Add ```"python.formatting.autopep8Args": ["--ignore","E402"]``` to the settings.json (either user or workspace), [Source](https://stackoverflow.com/questions/54015604/disable-python-import-sorting-in-vscode/54016555#54016555)

## VS Code reports SQLAlchemy issues
Fix for VS Code reporting e.g.:```Instance of 'SQLAlchemy' has no 'Column' member```.

Install pylint-flask: ```pip install pylint-flask```

Then ensure VS Code runs with pylink using pylint-flask; add ```"python.linting.pylintArgs": ["--load-plugins", "pylint_flask"]``` to settings.json (either user or workspace), [Source](https://stackoverflow.com/questions/28193025/pylint-cant-find-sqlalchemy-query-member)

Alternatively; ignore the error (caused by the classes inheriting from db.Model not having a query member until the code runs).