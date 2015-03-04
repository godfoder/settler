from migrate.versioning import api

import os.path
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from app import db
from app.config import SQLALCHEMY_DATABASE_URI
from app.config import SQLALCHEMY_MIGRATE_REPO
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print('Current database version: ' + str(v))