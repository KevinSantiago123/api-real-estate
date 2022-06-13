from estate_habi.utils.exceptions import ExceptionPersonalized
from estate_habi.conection_db.connection import ConnectionDB
from server.response import Response

__author__ = 'kcastanedat'


class OperationDB:
    """
    Allows you to perform operations to query the databases
    """

    def __init__(self):
        self.conn = ConnectionDB()
        self.connection = self.conn.connect()
        self.query = """
                        SELECT property_f.id,
                            property_f.address,
                            property_f.city,
                            status.name AS status,
                            property_f.price,
                            property_f.description
                        FROM habi_db.property AS property_f
                        INNER JOIN
                        (SELECT property_id,
                                status_id,
                                max(update_date) AS update_date
                        FROM status_history
                        GROUP BY property_id) AS tbl_inter ON tbl_inter.property_id = property_f.id
                        INNER JOIN status ON (tbl_inter.status_id = status.id)
                        WHERE status.name IN ('pre_venta',
                                            'en_venta',
                                            'vendido')
                        AND property_f.address <> ''
                        AND property_f.city <> ''
                        AND property_f.description <> ''
                    """

    def get_all_property(self):
        """Allows you to list all real estate"""
        try:
            # Get Rows
            self.cursor = self.connection.cursor()
            self.cursor.execute(self.query)
            data = self.cursor.fetchall()
            self.cursor.close()
            return data
        except Exception as e:
            self.connection.rollback()
            raise ExceptionPersonalized(
                "There was an error in the database listing all real estate")

    def get_property_by_filter(self, request):
        """Allows filters by parameters"""
        try:
            self.__query_filter = {
                'status': "AND status.name = '%s'",
                'year': "AND property_f.year = %s",
                'city': "AND property_f.city = '%s'"
            }
            for key, value in request.items():
                if self.__query_filter.get(key) is not None:
                    self.query = f"{self.query} {self.__query_filter.get(key)}" % (
                        value)

            self.cursor = self.connection.cursor()
            self.cursor.execute(self.query)
            data = self.cursor.fetchall()
            self.cursor.close()
            return data

        except Exception as e:
            self.connection.rollback()
            raise ExceptionPersonalized(
                f"There was a database error filtering real estate {e}")


class Validations:
    """Perform validations on input parameters."""

    def __init__(self, request):
        self.request = request.args.to_dict(flat=True)
        self.params_type = {
            'year': int,
            'city': str,
            'status': ['pre_venta',
                       'en_venta',
                       'vendido']
        }
        self.message = ''

    def request_is_not_valid(self):
        """Validate the parameters, their length and data type in the request"""
        if len(self.request.keys()) > 0:
            # return False, {'ppp':'Hello!'}
            for key, value in self.request.items():
                self.valid_keys(key)
                self.valid_year(key, value)
                self.valid_status(key, value)
                if len(self.message) > 0:
                    return True
            return False
        return False

    def valid_keys(self, key):
        """Validate Keys of request"""
        try:
            if self.params_type.get(key) is None:
                self.message = f"The key: '{key}' is not a valid parameter"
        except Exception as e:
            print(e)

    def valid_year(self, key, value):
        """Validate value of year"""
        try:
            if key == 'year' and value.isnumeric() is not True:
                self.message = f"The value of key: '{key}' is not positive"
        except Exception as e:
            print(e)

    def valid_status(self, key, value):
        """Validate value of status"""
        try:
            if key == 'status' and value not in self.params_type.get(key):
                self.message = f"The possible values for the key: '{key}' are {self.params_type.get(key)}"
        except Exception as e:
            print(e)

    def errors(self):
        """Return error in validations"""
        return Response.status(400, self.message)
