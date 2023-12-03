import mysql.connector

class Catalogo:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
    )
        self.cursor = self.conn.cursor(dictionary=True)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
            codigo INT,
            nombre varchar(255) NOT NULL,
            cantidad INT(4) NOT NULL,
            descripcion VARCHAR(255) NOT NULL,
            precio DECIMAL(10, 2) NOT NULL,
            tipo VARCHAR(255) NOT NULL,
            proveedor INT(2))''')
        
        self.conn.commit()
#----------------------------------------------------------
#Programa Principal
#----------------------------------------------------------
catalogo = Catalogo(host='localhost', user='root', password='',database='TpFinalCodoACodo')