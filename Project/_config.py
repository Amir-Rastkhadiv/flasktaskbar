
import os
# grab the folder when this script live
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskbar.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'Daniel3456789'

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

