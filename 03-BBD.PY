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
    def agregar_bebida(self, nombre, precio, tipo, proveedor, descripcion, cantidad, codigo):
#-----------------------Verificar si el producto ya existe -----------------------------------
            self.cursor.execute(f"SELECT * FROM bebidas WHERE codigo = {codigo}")
            bebida_existe = self.cursor.fetchone()
            if bebida_existe:
               return False
#-----------------------Cuandpo el producto no existe -------------------------------            
            sql = f"INSERT INTO bebida \
                (codigo,nombre, descripcion, cantidad, precio, tipo, proveedor) 
            VALUES \ ({codigo}, '{descripcion}', {cantidad}, {precio},'{nombre}', {tipo},'{proveedor}')"
            self.cursor.execute(sql)
            self.conn.commit()
            return True
#----------------------------------------------------------
#Programa Principal
#----------------------------------------------------------
catalogo = Catalogo(host='localhost', user='root', password='',database='TpFinalCodoACodo')
#----------------------------------------------------------
#Agregamos Bebidas
catalogo.agregar_bebida(1,'Agua mineral.', 100, 'Bebida sin alcohol 600cc',1000,'Pepsico')
catalogo.agregar_bebida(2,'Gaseosa.', 6000, 'Bebida sin alcohol 3L',2500, 'Pepsico')
catalogo.agregar_bebida(3,'Soda.', 50, 'Bebida sin alcohol 450cc',750, 'Pepsico')