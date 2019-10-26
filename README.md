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

### Flask tricks
There is a set of command line arguments that can exected from the shell (defined in ```cli.py```), for using PyBabel translations:
- ```flask translate init``` which initialises a new language
- ```flask translate update``` which extracts new text strings from an existing language
- ```flask translate init``` which compiles all updated language files

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

## Docker
### Building image
I needed to clean up the requirements.txt a bit because VS Code auto-installs linters etc. which ended up poluting the image and giving problems.
Other than that, just build with ```docker build -t microblog:latest .```

Doing a recursive chown for the whole directory is making the building process rather slow (as in minutes), whereas adding the --chown flag to COPY only takes a few seconds.

### Running image
Run the built image with e.g.```docker run --name microblog -d -p 8000:5000 --rm microblog:latest```, where -p <1>:<2> describes 1: host port, 2: container port (so 2 needs to match what is exposed in the dockerfile)

The ```--rm``` options removes the container after it has been terminated.

Feed the environment variables in either in the build process or (for the secret stuff) add it at run time with ```-e SECRET_KEY=my_secret_key -e MAIL_SERVER=smtp.googlemail.com```.

Link it to another container (e.g. running MySQL) with ```--link name:hostname-for-container```.


#### Full run example
```
docker run --name microblog -d -p 8000:5000 --rm -e SECRET_KEY=my-secret-key -e MAIL_SERVER=smtp.googlemail.com -e MAIL_PORT=587 -e MAIL_USE_TLS=true -e MAIL_USERNAME=<your-gmail-username> -e MAIL_PASSWORD=<your-gmail-password> --link mysql:dbserver -e DATABASE_URL=mysql+pymysql://microblog:<database-password>@dbserver/microblog --link elasticsearch:elasticsearch -e ELASTICSEARCH_URL=http://elasticsearch:9200 --link redis:redis-server -e REDIS_URL=redis://redis-server:6379/0 microblog:latest
```

### Troubleshooting
Getting an error along the lines of ```standard_init_linux.go:211: exec user process caused "no such file or directory"``` is probably caused by Windows vs UNIX line endings (i.e. CRLF vs LF).

Make sure the entrypoint file is *UNIX* formatted (VS Code has a setting for it down near the language menu).


It takes ~30-40 seconds before the container is available on the given host port.

### Docker logs
Get the logs with ```docker logs containername```.

## Supporting Docker images
### MySQL
There's a MySQL image maintained by the MySQL team.

Run it with
```
docker run --name mysql --rm -d -e MYSQL_RANDOM_ROOT_PASSWORD=yes -e MYSQL_DATABASE=microblog -e MYSQL_USER=microblog -e MYSQL_PASSWORD=<database-password> mysql/mysql-server:5.7
```

### ElasticSearch
The [ElasticSearch documentation for Docker](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html) describes how to run as single-node for development and two-node for production.

Run it with
```
docker run --name elasticsearch -d -p 9200:9200 -p 9300:9300 --rm -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch-oss:6.1.1
```

### Redis
There are official Redis images as well for instance based on alpine.

Run it with
```
docker run --name redis -d -p 6379:6379 redis:3-alpine
```