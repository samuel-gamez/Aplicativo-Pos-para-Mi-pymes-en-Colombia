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
    def registro(self, usu_nom, usu_apep, usu_apem, usu_ced, usu_tel, usu_sex, usu_correo, usu_password):
        query = "INSERT INTO usuarios (usu_nom, usu_apep, usu_apem, usu_ced, usu_tel, usu_sex, usu_correo, usu_password, est) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, 1)"
        values = (usu_nom, usu_apep, usu_apem, usu_ced, usu_tel, usu_sex, usu_correo, usu_password)

        try:
            execute_query(query, values)
            return True

        except Exception as e:
            print(f"Error durante el registro de usuario: {e}")
            return False


