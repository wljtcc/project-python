APP_NAME = 'dev'
FLASK_ENV = 'development'
SECRET_KEY = 'jfw6G4ZurxOb3ph2uH+CEQbRM0sPdz1/5sK2w6RfF8w='
DEBUG = True

# App Config Connection
HOST='0.0.0.0'
PORT=9000

# Database Config Connection
SQLALCHEMY_DATABASE_URI = 'postgresql://flask:flask@127.0.0.1/flask'
SQLALCHEMY_TRACK_MODIFICATIONS = True
# Postgres(postgresql://scott:tiger@localhost/mydatabase)
# MySQL(mysql://scott:tiger@localhost/mydatabase)
# Oracle(oracle://scott:tiger@127.0.0.1:1521/sidname)
