import os


class Config(object):
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or '\xe8\xbdmy\x85\x9f\x12o\xd6\x9c\xe4?JV\xf8\x89X\xba\xee\x87\xb2\x0e\xb7\xd9'
