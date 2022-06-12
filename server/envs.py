import os
from dotenv import load_dotenv

__author__ = 'kcastanedat'

# Uncomment in case you run on Ios operating system
"""
PORT = os.environ['PORT']
URL = os.environ['URL']
HOST_DB = os.environ("HOST_DB")
PORT_DB = os.environ("PORT_DB")
SCHEMA_DB = os.environ("SCHEMA_DB")
USER_DB = os.environ("USER_DB")
PASSWORD_DB = os.environ("PASSWORD_DB")
"""

# Uncomment in case you run on Windows operating system
load_dotenv()
PORT = os.getenv("PORT")
URL = os.getenv("URL")
HOST_DB = os.getenv("HOST_DB")
PORT_DB = int(os.getenv("PORT_DB"))
SCHEMA_DB = os.getenv("SCHEMA_DB")
USER_DB = os.getenv("USER_DB")
PASSWORD_DB = os.getenv("PASSWORD_DB")