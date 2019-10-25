# FlaskMegaTutorial
Following the Flask Mega Tutorial by Miguel Grinberg
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

## Python mailserver
For debugging purposes, it can be handy to let Python listen for mailserver requests, e.g. to listen on port 8025:

```
python -m smtpd -n -c DebuggingServer localhost:8025
```

## PyBabel translations
Mark all the source code and HTML templates with ```_()``` and ```_l()```.
Then, with babel.cfg in place, create messages.pot:

```
pybabel extract -F babel.cfg -k _l -o messages.pot .
```

Then generate the translations for the individual languages (Babel expects to find them in ```app/translations```):
```
pybabel init -i messages.pot -d app/translations -l es
```

When the translations are added to the ```messages.po``` file for that language, then it needs to be compiled:
```
pybabel compile -d app/translations
```

Which will create a ```messages.mo``` file, which is what Babel uses to load the translations.

If you miss any texts, they'll remain in English. Locate the missing texts and wrap them in ```_()``` and ```_l()```, then run an update:
```
pybabel extract -F babel.cfg -k _l -o messages.pot .
pybabel update -i messages.pot -d app/translations
```

# Other notes
## User accounts
*all passwords are: ```cat```*
- antra
- susan
- 1

## VS Code re-breaks import statements
Fix for VS Code moving ```from app import routes, models``` up to the top of the file.

Add ```"python.formatting.autopep8Args": ["--ignore","E402"]``` to the settings.json (either user or workspace), [Source](https://stackoverflow.com/questions/54015604/disable-python-import-sorting-in-vscode/54016555#54016555)

## VS Code reports SQLAlchemy issues
Fix for VS Code reporting e.g.: ```Instance of 'SQLAlchemy' has no 'Column' member```.

Install pylint-flask: ```pip install pylint-flask```

Then ensure VS Code runs with pylink using pylint-flask; add ```"python.linting.pylintArgs": ["--load-plugins", "pylint_flask"]``` to settings.json (either user or workspace), [Source](https://stackoverflow.com/questions/28193025/pylint-cant-find-sqlalchemy-query-member)

Alternatively; ignore the error (caused by the classes inheriting from db.Model not having a query member until the code runs).

## ElasticSearch
Uses [ElasticSearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/zip-windows.html#install-windows) for searching.

run with e.g. ```C:/Utils/elasticsearch-7.4.1/bin/elasticsearch.bat```, can also run as a service with ```bin/elasticsearch-service.bat install|remove|start|stop|manager```.

Configuration files are stored in ```config/elasticsearch.yml```.

## Creating secret keys
One option is to UUIDs, e.g. ```python -c "import uuid; print(uuid.uuid4().hex)"```.

Never-ever-ever store the secret keys directly in the application -- utilise the .env (and ```from dotenv import load_dotenv```) to hold the key -- and obviously don't put the .env files in Git. ;)