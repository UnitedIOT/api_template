# coding=utf-8
# *****************************
# Environment specific settings
# *****************************

# DO NOT use "DEBUG = True" in production environments

import os

env_dist = os.environ

CURRENT_WORK_DIR = os.getcwd()

DEBUG = True

DB_CTS = 'ctsdb'
DB_TDS = 'tdsdb'

# DO NOT use Unsecure Secrets in production environments
# Generate a safe one with:
#     python -c "import os; print repr(os.urandom(24));"
SECRET_KEY = b'\xc9\xf6&\x1c\xfeD\x1f\xee~\xa3P\xf6\x0b\xf3\x1b\xe2\xb8\xe9\x01\xdb3\x0e\xac\x10'

DB_PWD = env_dist.get("DB_PWD") if env_dist.get("DB_PWD") is not None else 'good'
DB_PORT = env_dist.get("DB_PORT") if env_dist.get("DB_PORT") is not None else '3306'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:' + DB_PWD + '@127.0.0.1:' + DB_PORT + '/' + DB_TDS + '?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = False    # Avoids a SQLAlchemy Warning
SQLALCHEMY_ECHO = False
