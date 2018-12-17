import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask.ext.wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from flask_session import Session
from csh import cread_info
app,db=cread_info()
manager=Manager(app=app)
Migrate(app=app,db=db)
manager.add_command(MigrateCommand)

@app.route('/')

def hello_world():

    return 'Hello World!'


if __name__ == '__main__':

    manager.run()