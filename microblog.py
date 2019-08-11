from app import app, db
from app.models import User, Post


# decorator defining what will be available for 'flask shell' (NB, inside the venv!)
@app.shell_context_processor
def make_shell_context():
    return {'db': db,
            'User': User,
            'Post': Post}


if __name__ == '__main__':
    app.run()
