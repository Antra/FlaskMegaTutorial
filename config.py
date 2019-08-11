import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or '\xe8\xbdmy\x85\x9f\x12o\xd6\x9c\xe4?JV\xf8\x89X\xba\xee\x87\xb2\x0e\xb7\xd9'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    # Signal the application every time a change is about to be done in the database?
    SQLALCHEMY_TRACK_MODIFICATIONS = False
