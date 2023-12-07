from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

class CatalogoPlatos:
    def __init__(self, host, user, database):
        self.conn = mysql.connector.connect(host=host, user=user)
        self.cursor = self.conn.cursor()

        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS platos (
            nombre varchar(25),
            descripcion varchar(25),
            precio double,
            id int not null auto_increment,
            primary key (id)
        )''')
        self.conn.commit()

        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)

    def listar_platos(self):
        self.cursor.execute("SELECT * FROM platos")
        platos = self.cursor.fetchall()
        return platos

    def consultar_plato(self, id):
        self.cursor.execute(f"SELECT * FROM platos WHERE id={id}")
        return self.cursor.fetchone()
    
    def agregar_plato(self, datos_plato):
        self.cursor.execute("""
            INSERT INTO platos (nombre, descripcion, precio)
            VALUES (%(nombre)s, %(descripcion)s, %(precio)s)
        """, datos_plato)
        self.conn.commit()
        return self.cursor.lastrowid

    def modificar_plato(self, id, nuevos_datos):
        self.cursor.execute("""
            UPDATE platos
            SET nombre=%(nombre)s, descripcion=%(descripcion)s, precio=%(precio)s
            WHERE id=%(id)s
        """, {'id': id, **nuevos_datos})
        self.conn.commit()

    def eliminar_plato(self, id):
        self.cursor.execute("DELETE FROM platos WHERE id=%s", (id,))
        self.conn.commit()

class CatalogoBebidas:
    def __init__(self, host, user, database):
        self.conn = mysql.connector.connect(host=host, user=user)
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
        self.cursor = self.conn.cursor(dictionary=True)
 
         
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

    def __init__(self, host, user, database):
        self.conn = mysql.connector.connect(host=host, user=user)
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
        self.cursor = self.conn.cursor(dictionary=True)

    def listar_clientes(self):
        self.cursor.execute("SELECT * FROM clientes")
        clientes = self.cursor.fetchall()
        return clientes

    def consultar_cliente(self, id):
        self.cursor.execute(f"SELECT * FROM clientes WHERE id={id}")
        return self.cursor.fetchone()

    def agregar_cliente(self, nombre, apellido, email):
        sql = f"INSERT INTO clientes (nombre, apellido, email) VALUES ('{nombre}', '{apellido}', '{email}')"
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.lastrowid

    def modificar_cliente(self, id, nuevo_nombre, nuevo_apellido, nuevo_email):
        sql = f"UPDATE clientes SET nombre='{nuevo_nombre}', apellido='{nuevo_apellido}', email='{nuevo_email}' WHERE id={id}"
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.rowcount > 0

    def eliminar_cliente(self, id):
        self.cursor.execute(f"DELETE FROM clientes WHERE id={id}")
        self.conn.commit()
        return self.cursor.rowcount > 0

class CatalogoReservas:
    def __init__(self, host, user, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
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
            id int auto_increment,
            id_cliente int,
            nombre_cliente varchar(50),
            correo_cliente varchar(50),
            sucursal varchar(20),
            fecha varchar(10),
            cantidad_personas int,
            restricciones varchar(50),
            primary key (id),
            foreign key (id_cliente)
                references clientes (id)
                on update cascade
                on delete cascade
        )''')
        self.conn.commit()

        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)

    def listar_reservas(self):
        self.cursor.execute("select * from reservas")
        reservas = self.cursor.fetchall()
        return reservas

    def consultar_reserva(self, id):
        self.cursor.execute(f"select * from reservas where id={id}")
        return self.cursor.fetchone()

    def mostrar_reserva(self, id):
        reserva = self.consultar_reserva(id)
        if reserva:
            print("-" * 40)
            print(f"Id.....: {reserva['id']}")
            print(f"Id cliente: {reserva['id_cliente']}")
            print(f"Nombre cliente: {reserva['nombre_cliente']}")
            print(f"Correo cliente: {reserva['correo_cliente']}")
            print(f"Sucursal: {reserva['sucursal']}")
            print(f"Fecha: {reserva['fecha']}")
            print(f"Cantidad de personas: {reserva['cantidad_personas']}")
            print(f"Restricciones: {reserva['restricciones']}")
        else:
            print("Reserva no encontrada.")

    def agregar_reserva(self, datos_reserva):
        self.cursor.execute("""
            INSERT INTO reservas (id_cliente, nombre_cliente, correo_cliente, sucursal, fecha, cantidad_personas, restricciones)
            VALUES (%(id_cliente)s, %(nombre_cliente)s, %(correo_cliente)s, %(sucursal)s, %(fecha)s, %(cantidad_personas)s, %(restricciones)s)
        """, datos_reserva)
        self.conn.commit()
        return self.cursor.lastrowid

    def modificar_reserva(self, id, nuevos_datos):
        self.cursor.execute("""
            UPDATE reservas
            SET id_cliente=%(id_cliente)s, nombre_cliente=%(nombre_cliente)s, correo_cliente=%(correo_cliente)s,
                sucursal=%(sucursal)s, fecha=%(fecha)s, cantidad_personas=%(cantidad_personas)s, restricciones=%(restricciones)s
            WHERE id=%(id)s
        """, {'id': id, **nuevos_datos})
        self.conn.commit()

    def eliminar_reserva(self, id):
        self.cursor.execute("DELETE FROM reservas WHERE id=%s", (id,))
        self.conn.commit()
#-------------------------------------------RUTAS------------------------------------------------#
platos = CatalogoPlatos(host='tpcodoacodo.mysql.pythonanywhere-services.com', user='rootroot', database='tpfinalcodoacodo')
bebidas = CatalogoBebidas(host='tpcodoacodo.mysql.pythonanywhere-services.com', user='rootroot', database='tpfinalcodoacodo')
clientes = CatalogoClientes(host='tpcodoacodo.mysql.pythonanywhere-services.com', user='rootroot', database='tpfinalcodoacodo')
reservas = CatalogoReservas(host='tpcodoacodo.mysql.pythonanywhere-services.com', user='rootroot', database='tpfinalcodoacodo')

# Ruta principal
@app.route("/")
def index():
    return render_template("index.html")

# Rutas para Platos
@app.route("/platos")
def gestion_platos():
    return render_template("platos.html")

@app.route("/platos/listar")
def listar_platos():
    platos_listados = platos.listar_platos()
    return render_template("listar_platos.html", platos=platos_listados)

@app.route("/platos/agregar", methods=["GET", "POST"])
def agregar_plato():
    if request.method == "POST":
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        platos.agregar_plato(nombre, descripcion, precio)
        return redirect(url_for('listar_platos'))
    return render_template("agregar_plato.html")

@app.route("/platos/modificar/<int:id>", methods=["GET", "POST"])
def modificar_plato(id):
    plato = platos.obtener_plato_por_id(id)
    if request.method == "POST":
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        platos.modificar_plato(id, nombre, descripcion, precio)
        return redirect(url_for('listar_platos'))
    return render_template("modificar_plato.html", plato=plato)

@app.route("/platos/eliminar/<int:id>")
def eliminar_plato(id):
    platos.eliminar_plato(id)
    return redirect(url_for('listar_platos'))

#Bebidas
@app.route("/bebidas", methods=["GET"])
def listar_bebidas():
    bebidas_listadas = bebidas.listar_bebidas()
    return render_template("bebidas.html", bebidas=bebidas_listadas)

@app.route("/bebidas/<int:id>", methods=["GET"])
def mostrar_bebida(id):
    bebida = bebidas.consultar_bebida(id)
    if bebida:
        return render_template("detalle_bebida.html", bebida=bebida)
    else:
        return "Bebida no encontrada", 404

@app.route("/bebidas", methods=["POST"])
def agregar_bebida():
    datos_bebida = request.json

    nuevo_id = bebidas.agregar_bebida({
        'nombre': datos_bebida.get('nombre'),
        'precio': datos_bebida.get('precio'),
        'tipo': datos_bebida.get('tipo'),
    })

    return jsonify({"id": nuevo_id}), 201

@app.route("/bebidas/<int:id>", methods=["PUT"])
def modificar_bebida(id):
    nuevos_datos = request.json
    bebidas.modificar_bebida(id, nuevos_datos)
    return jsonify({"mensaje": "Bebida modificada correctamente"}), 200

@app.route("/bebidas/<int:id>", methods=["DELETE"])
def eliminar_bebida(id):
    bebidas.eliminar_bebida(id)
    return jsonify({"mensaje": "Bebida eliminada correctamente"}), 200

#Clientes
@app.route("/clientes", methods=["GET"])
def listar_clientes():
    clientes_listados = clientes.listar_clientes()
    return jsonify(clientes_listados)

@app.route("/clientes/<int:id>", methods=["GET"])
def mostrar_cliente(id):
    cliente = clientes.consultar_cliente(id)
    if cliente:
        return jsonify(cliente)
    else:
        return "Cliente no encontrado", 404

@app.route("/clientes", methods=["POST"])
def agregar_cliente():
    datos_cliente = request.form.to_dict()

    nuevo_id = clientes.agregar_cliente(
        nombre=datos_cliente.get('nombre'),
        apellido=datos_cliente.get('apellido'),
        email=datos_cliente.get('email')
    )

    return jsonify({"id": nuevo_id}), 201

@app.route("/clientes/<int:id>", methods=["PUT"])
def modificar_cliente(id):
    nuevos_datos = request.json
    exito = clientes.modificar_cliente(
        id,
        nuevo_nombre=nuevos_datos.get('nombre'),
        nuevo_apellido=nuevos_datos.get('apellido'),
        nuevo_email=nuevos_datos.get('email')
    )

    if exito:
        return jsonify({"mensaje": "Cliente modificado correctamente"}), 200
    else:
        return jsonify({"mensaje": "No se pudo modificar el cliente"}), 500

@app.route("/clientes/<int:id>", methods=["DELETE"])
def eliminar_cliente(id):
    exito = clientes.eliminar_cliente(id)

    if exito:
        return jsonify({"mensaje": "Cliente eliminado correctamente"}), 200
    else:
        return jsonify({"mensaje": "No se pudo eliminar el cliente"}), 500

#Reservas
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
    ruta_destino = './static/imagenes/'  # Ajusta la ruta según tu estructura de archivos
    app.run(debug=True)