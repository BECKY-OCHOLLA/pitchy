from app import create_app,db


app = create_app()

from app.models import User
@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User )

if __name__=='__main__':
    app.run(debug = True)