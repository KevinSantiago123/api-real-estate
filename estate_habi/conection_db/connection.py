import pymysql

from server.envs import HOST_DB, PORT_DB, USER_DB, PASSWORD_DB, SCHEMA_DB
from estate_habi.utils.exceptions import ExceptionPersonalized

__author__ = 'kcastanedat'


class ConnectionDB:
    """Allows connection to a database Mysql"""

    def connect(self):
        try:
            self.connection = pymysql.connect(
                host=HOST_DB,
                port=PORT_DB,
                user=USER_DB,
                password=PASSWORD_DB,
                db=SCHEMA_DB
            )
            return self.connection

        except (Exception) as e:
            raise ExceptionPersonalized(
                "Error connecting to DB")
