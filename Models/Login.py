from config.conexion import execute_query

class Usuario:
    def login(self, usu_correo, usu_pass):
        query = "SELECT * FROM usuarios WHERE usu_correo=%s AND usu_password=%s"
        values = (usu_correo, usu_pass)

        resultado = execute_query(query, values, fetchone=True)

        if resultado:
            return {
                'usu_id': resultado[0],
                'usu_correo': resultado[1],
                'usu_password': resultado[2]
            }
        else:
            return None


