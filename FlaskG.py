#--------------------------------------------------------------------
# Instalar con pip install Flask
from flask import Flask, request, jsonify
from flask import request
# Instalar con pip install flask-cors
from flask_cors import CORS
# Instalar con pip install mysql-connector-python
import mysql.connector
# Si es necesario, pip install Werkzeug
from werkzeug.utils import secure_filename
# No es necesario instalar, es parte del sistema standard de Python
import os
import time

app = Flask(__name__)
CORS(app) # Esto habilitará CORS para todas las rutas

class CatalogoPlatos:
# Constructor de la clase
     def __init__(self, host, user, password, database):
# Primero, establecemos una conexión sin especificar la base de datos
         self.conn = mysql.connector.connect(
             host=host,
             user=user,
             password=password
        )
         self.cursor = self.conn.cursor()
# Intentamos seleccionar la base de datos
         try:
          self.cursor.execute(f"USE {database}")
         except mysql.connector.Error as err:
# Si la base de datos no existe, la creamos
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err
# Una vez que la base de datos está establecida, creamos la tabla si no existe
         self.cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                nombre varchar(25),
                apellido varchar(25),
                email varchar(25),
                id int not null auto_increment,

                primary key (id))''')
         self.conn.commit()
# Cerrar el cursor inicial y abrir uno nuevo con el parámetro
         self.cursor.close()
         self.cursor=self.conn.cursor(dictionary=True) # Aca le decimos que la consulta que haga la devuelva en diccionario, que despues vamos a convertir a JSON para poder acceder a ellos por el front

#---------------     
     def listar_platos(self):
             self.cursor.execute("select * from platos")
             platos = self.cursor.fetchall()  
             return platos
   
     def consultar_plato(self,id):
             self.cursor.execute(f"select * from platos where id={id}")
             return self.cursor.fetchone()
         
     def mostrar_plato(self, id):
             plato = self.consultar_plato(id)
             if plato:
                print("-" * 40)
                print(f"Nombre.....: {plato['nombre']}")
                print(f"Descripción: {plato['descripcion']}")
                print(f"Precio..: {plato['precio']}")
                print(f"Id.....: {plato['id']}")
             else:
                print("Plato no encontrado.")

                

class CatalogoBebidas:

     def __init__(self, host, user, password, database):
         self.conn = mysql.connector.connect(
             host=host,
             user=user,
             password=password
        )
         self.cursor = self.conn.cursor()

         try:
          self.cursor.execute(f"USE {database}")
         except mysql.connector.Error as err:

            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err

         self.cursor.execute('''CREATE TABLE IF NOT EXISTS bebidas (
                nombre varchar(25),
                precio double,
                tipo varchar(25),
                id int not null auto_increment,

                primary key (id)
                )''')
         self.conn.commit()

         self.cursor.close()
         self.cursor=self.conn.cursor(dictionary=True) 

#---------------     
     def listar_bebidas(self):
             self.cursor.execute("select * from bebidas")
             bebidas = self.cursor.fetchall()  
             return bebidas
   
     def consultar_bebida(self,id):
             self.cursor.execute(f"select * from bebidas where id={id}")
             return self.cursor.fetchone()
         
     def mostrar_bebida(self, id):
             bebida = self.consultar_bebida(id)
             if bebida:
                print("-" * 40)
                print(f"Nombre.....: {bebida['nombre']}")
                print(f"Precio: {bebida['precio']}")
                print(f"Tipo..: {bebida['tipo']}")
                print(f"Id.....: {bebida['id']}")
             else:
                print("Bebida no encontrado.")

class CatalogoClientes:

     def __init__(self, host, user, password, database):
         self.conn = mysql.connector.connect(
             host=host,
             user=user,
             password=password
        )
         self.cursor = self.conn.cursor()

         try:
          self.cursor.execute(f"USE {database}")
         except mysql.connector.Error as err:

            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err

         self.cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                nombre varchar(25),
                apellido varchar(25),
                email varchar(25),
                id int not null auto_increment,

                primary key (id)

                )''')
         self.conn.commit()

         self.cursor.close()
         self.cursor=self.conn.cursor(dictionary=True) 

#---------------     
     def listar_clientes(self):
             self.cursor.execute("select * from clientes")
             clientes = self.cursor.fetchall()  
             return clientes
   
     def consultar_clientea(self,id):
             self.cursor.execute(f"select * from clientes where id={id}")
             return self.cursor.fetchone()
         
     def mostrar_cliente(self, id):
             cliente = self.consultar_cliente(id)
             if cliente:
                print("-" * 40)
                print(f"Nombre.....: {cliente['nombre']}")
                print(f"Apellido: {cliente['apellido']}")
                print(f"Email..: {cliente['email']}")
                print(f"Id.....: {cliente['id']}")
             else:
                print("Cliente no encontrado.")

class CatalogoReservas:

     def __init__(self, host, user, password, database):
         self.conn = mysql.connector.connect(
             host=host,
             user=user,
             password=password
        )
         self.cursor = self.conn.cursor()

         try:
          self.cursor.execute(f"USE {database}")
         except mysql.connector.Error as err:

            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err

         self.cursor.execute('''CREATE TABLE IF NOT EXISTS reservas (
                id int,
                id_cliente int,
                id_plato int, 
                id_bebida int,
                cantidad_personas int,
                fecha varchar(10),
                hora varchar(10),
                turno varchar(10),

                primary key (id),
                foreign key (id_cliente)
                references clientes (id)
                on update cascade
                on delete cascade,
                foreign key (id_plato)
                references platos(id)
                on update cascade
                on delete cascade,
                foreign key (id_bebida)
                references bebidas (id)
                on delete cascade
                on update cascade
                )''')
         self.conn.commit()

         self.cursor.close()
         self.cursor=self.conn.cursor(dictionary=True) 

#---------------     
     def listar_reservas(self):
             self.cursor.execute("select * from reservas")
             reservas = self.cursor.fetchall()  
             return reservas
   
     def consultar_reserva(self,id):
             self.cursor.execute(f"select * from reservas where id={id}")
             return self.cursor.fetchone()
         
     def mostrar_reserva(self, id):
             reserva = self.consultar_reserva(id)
             if reserva:
                print("-" * 40)
                print(f"Id.....: {reserva['id']}")
                print(f"Id cliente: {reserva['id_cliente']}")
                print(f"Id plato..: {reserva['id_plato']}")
                print(f"Id bebida.....: {reserva['id_bebida']}")
                print(f"Cantidad de personas.....: {reserva['cantidad_personas']}")
                print(f"Fecha: {reserva['fecha']}")
                print(f"Hora..: {reserva['hora']}")
                print(f"Turno.....: {reserva['turno']}")
             else:
                print("Reserva no encontrada.")

def agregar_reserva(self, datos_reserva):
        self.cursor.execute("""
            INSERT INTO reservas (id_cliente, id_plato, id_bebida, cantidad_personas, fecha, hora, turno)
            VALUES (%(id_cliente)s, %(id_plato)s, %(id_bebida)s, %(cantidad_personas)s, %(fecha)s, %(hora)s, %(turno)s)
        """, datos_reserva)
        self.conn.commit()
        return self.cursor.lastrowid

def modificar_reserva(self, id, nuevos_datos):
        self.cursor.execute("""
            UPDATE reservas
            SET id_cliente=%(id_cliente)s, id_plato=%(id_plato)s, id_bebida=%(id_bebida)s,
                cantidad_personas=%(cantidad_personas)s, fecha=%(fecha)s, hora=%(hora)s, turno=%(turno)s
            WHERE id=%(id)s
        """, {'id': id, **nuevos_datos})
        self.conn.commit()

def eliminar_reserva(self, id):
        self.cursor.execute("DELETE FROM reservas WHERE id=%s", (id,))
        self.conn.commit()                
   
'''''
#--------------------------------------------------------------------
# Cuerpo del programa
#--------------------------------------------------------------------
# Crear una instancia de la clase Catalogo
platos = CatalogoPlatos(host='localhost', user='root', password='root', database='tpfinalcodoacodo')
# Carpeta para guardar las imagenes
ruta_destino = './static/imagenes/'

@app.route("/platos", methods=["GET"])
def listar_platos():
     platosListados = platos.listar_platos()
     return jsonify(platosListados)

@app.route("/platos/<int:id>", methods=["GET"])
def mostrar_plato(id):
    plato = platos.consultar_plato(id)
    if plato:
       return jsonify(plato)
    else:
        return "Plato no encontrado", 404

if __name__ == "__main__":
  app.run(debug=True)


bebidas = CatalogoBebidas(host='localhost', user='root', password='root', database='tpfinalcodoacodo')
# Carpeta para guardar las imagenes
ruta_destino = './static/imagenes/'

@app.route("/bebidas", methods=["GET"])
def listar_bebidas():
     bebidasListadas = bebidas.listar_bebidas()
     return jsonify(bebidasListadas)

@app.route("/bebidas/<int:id>", methods=["GET"])
def mostrar_bebida(id):
    bebida = bebidas.consultar_bebida(id)
    if bebida:
       return jsonify(bebida)
    else:
        return "Bebida no encontrada", 404

if __name__ == "__main__":
  app.run(debug=True)
  

clientes = CatalogoClientes(host='localhost', user='root', password='root', database='tpfinalcodoacodo')
# Carpeta para guardar las imagenes
ruta_destino = './static/imagenes/'

@app.route("/clientes", methods=["GET"])
def listar_clientes():
     clientesListados = clientes.listar_clientes()
     return jsonify(clientesListados)

@app.route("/clientes/<int:id>", methods=["GET"])
def mostrar_cliente(id):
    cliente = clientes.consultar_cliente(id)
    if cliente:
       return jsonify(cliente)
    else:
        return "Cliente no encontrado", 404

if __name__ == "__main__":
  app.run(debug=True)
  '''
reservas = CatalogoReservas(host='localhost', user='root', password='root', database='tpfinalcodoacodo')
# Carpeta para guardar las imagenes
ruta_destino = './static/imagenes/'

@app.route("/reservas", methods=["GET"])
def listar_reservas():
     reservasListadas = reservas.listar_reservas()
     return jsonify(reservasListadas)

@app.route("/reservas/<int:id>", methods=["GET"])
def mostrar_reserva(id):
    reserva = reservas.consultar_reserva(id)
    if reserva:
       return jsonify(reserva)
    else:
        return "Reserva no encontrada", 404

@app.route("/reservas", methods=["POST"])
def agregar_reserva():
    datos_reserva = request.json
    nuevo_id = reservas.agregar_reserva(datos_reserva)
    return jsonify({"id": nuevo_id}), 201

@app.route("/reservas/<int:id>", methods=["PUT"])
def modificar_reserva(id):
    nuevos_datos = request.json
    reservas.modificar_reserva(id, nuevos_datos)
    return jsonify({"mensaje": "Reserva modificada correctamente"}), 200

@app.route("/reservas/<int:id>", methods=["DELETE"])
def eliminar_reserva(id):
    reservas.eliminar_reserva(id)
    return jsonify({"mensaje": "Reserva eliminada correctamente"}), 200        

if __name__ == "__main__":
  app.run(debug=True)
