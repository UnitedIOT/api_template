# coding=utf-8
"""This file sets up a command line manager.

Use "python manage.py" for a list of available commands.
Use "python manage.py runserver" to start the development web server on localhost:5000.
Use "python manage.py runserver --help" for a list of runserver options.
"""

from flask_script import Manager

from api import create_app
from api.commands import SampleCommand


# Setup Flask-Script with command line commands

manager = Manager(create_app)
manager.add_command('sample_cmd', SampleCommand)

if __name__ == "__main__":
    # python manage.py                      # shows available commands
    # python manage.py runserver --help     # shows available runserver options
    manager.run()
