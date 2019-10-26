from app import create_app, db, cli
from app.models import User, Post

app = create_app()
cli.register(app)

# decorator defining what will be available for 'flask shell' (NB, inside the venv!)
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message, 'Notification': Notification}
