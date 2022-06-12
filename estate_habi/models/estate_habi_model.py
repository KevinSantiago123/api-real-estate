from estate_habi.utils.exceptions import ExceptionPersonalized
from estate_habi.conection_db.connection import ConnectionDB


class OperationDB():
    """
    Allows you to perform operations to query the databases
    """

    def __init__(self):
        self.conn = ConnectionDB()
        self.connection = self.conn.connect()

    def get_all_property(self):
        """
        Allows you to list all real estate
        """
        try:
            #Get Rows
            self.cursor = self.connection.cursor()
            self.cursor.execute("""SELECT property_f.id,
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
                                    ORDER BY property_f.id;""")
            data = self.cursor.fetchall()
            self.cursor.close()
            return data
        except Exception as e:
            self.connection.rollback()
            raise ExceptionPersonalized(
                "There was a database error")

    def queryContexto(self):
        """
        Permite realizar una consulta 
        """
        try:
            cursor = self.connection.cursor()

            # ejecutar la consulta
            cursor.execute(
                """SELECT * FROM "Transversal"."GEN_Contexto_copia" ;""")
            data = cursor.fetchall()
            cursor.close()

            return data

        except Exception as e:
            self.connection.rollback()
            raise ExceptionPersonalized(
                "Error al realizar la consulta SQL:::" + str(e))

    def queryAmenaza(self, id_riesgo, id_modulo, id_contexto, id_cultivo, id_amenaza=None):
        """
        Permite realizar una consulta 
        """
        try:
            query = """ SELECT 
                        a.id_amenaza,
                        a.amenaza,
                        p.periodo
                        FROM "Transversal"."GEN_Amenaza_copia" AS a 
                        LEFT JOIN  "Transversal"."GEN_Periodo" AS p ON p.id_periodo = a.id_periodo
                        WHERE a.id_riesgo = %s
                        AND a.id_modulo = %s
                        AND a.id_contexto = %s
                        AND a.id_sistema_productivo = %s
                     """ % (id_riesgo, id_modulo, id_contexto, id_cultivo)

            if id_amenaza:
                query = """ SELECT 
                            a.url_mosaico
                            FROM "Transversal"."GEN_Amenaza_copia" AS a
                            WHERE a.id_riesgo = %s
                            AND a.id_modulo = %s
                            AND a.id_contexto = %s
                            AND a.id_sistema_productivo = %s
                            AND a.id_amenaza = %s
                        """ % (id_riesgo, id_modulo, id_contexto, id_cultivo, id_amenaza)

            cursor = self.connection.cursor()

            # ejecutar la consulta
            cursor.execute(query)

            data = cursor.fetchall()

            cursor.close()

            return data

        except Exception as e:
            self.connection.rollback()
            raise ExceptionPersonalized(
                "Error al realizar la consulta SQL:::" + str(e))