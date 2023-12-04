import mysql.connector


class CatalogoPlatos:
  def __init__(self, host, user, password, database):
   self.conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
   self.cursor = self.conn.cursor(dictionary=True)
   self.cursor.execute('''CREATE TABLE IF NOT EXISTS platos (
        nombre varchar(25),
        descripcion varchar(25),
        precio double,
        id int not null auto_increment,

    primary key (id))''')
   self.conn.commit()

   
  def agregar_platos(self,nombre, descripcion, precio,id):
      self.cursor.execute(f'select * from platos where id={id}')
      plato_existe=self.cursor.fetchone()
      if plato_existe:
        return False
     
      sql=f"insert into platos (nombre,descripcion,precio,id) values('{nombre}','{descripcion}',{precio},{id})"
      self.cursor.execute(sql)
      self.conn.commit()
      return True
  
  def consultar_plato(self,id):
     self.cursor.execute(f"select * from platos where id={id}")
     return self.cursor.fetchone()
  
  def modificar_plato(self, nuevo_nombre, nueva_descripcion,nuevo_precio,id):
    sql=f"update platos set nombre='{nuevo_nombre}',descripcion ='{nueva_descripcion}', precio={nuevo_precio} where id={id}"
    self.cursor.execute(sql)
    self.conn.commit()
    return self.cursor.rowcount>0
  
# Mostramos los datos de un producto a partir de su id

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

#Mostramos todos los productos de la tabla
  # ...

  def listar_platos(self):
    self.cursor.execute("select * from platos")
    platos = self.cursor.fetchall()  # Corregir aquí
    print("-" * 50)
    for plato in platos:
        print(f"Nombre....: {plato['nombre']}")
        print(f"Descripcion....: {plato['descripcion']}")
        print(f"Precio....: {plato['precio']}")
        print(f"Id....: {plato['id']}")
        print("-" * 50)

  def eliminar_plato(self, id):
# Eliminamos un producto de la tabla a partir de su código
      self.cursor.execute(f"DELETE FROM platos WHERE id =
{id}")
      self.conn.commit()
      return self.cursor.rowcount > 0

  

#---------------


class CatalogoBebidas :
     def __init__(self, host, user, password, database):
      self.conn = mysql.connector.connect(
       host=host,
       user=user,
       password=password,
       database=database
)
      self.cursor = self.conn.cursor(dictionary=True)
      self.cursor.execute('''CREATE TABLE IF NOT EXISTS bebidas (
       nombre varchar(25),
       precio double,
       tipo varchar(25),
       id int not null auto_increment,

       primary key (id))''')
      self.conn.commit()

     def agregar_bebidas(self, nombre, precio, tipo, id):
      self.cursor.execute(f'select * from bebidas where id={id}')
      bebida_existe=self.cursor.fetchone()
      if bebida_existe:
        return False
     
      sql=f"insert into bebidas (nombre, precio, tipo, id) values('{nombre}',{precio},'{tipo}',{id})"
      self.cursor.execute(sql)
      self.conn.commit()
      return True
     
     def consultar_bebida(self,id):
       self.cursor.execute(f"select * from bebidas where id={id}")
       return self.cursor.fetchone()
     
     def modificar_bebida(self, nuevo_nombre, nuevo_precio, nuevo_tipo, id):
      sql=f"update bebidas set nombre='{nuevo_nombre}',precio ={nuevo_precio},tipo='{nuevo_tipo}' where id={id}"
      self.cursor.execute(sql)
      self.conn.commit()
      return self.cursor.rowcount>0
     
     def mostrar_bebida(self, id):
        bebida = self.consultar_bebida(id)
        if bebida:
          print("-" * 40)
          print(f"Nombre.....: {bebida['nombre']}")
          print(f"Precio: {bebida['precio']}")
          print(f"Tipo..: {bebida['tipo']}")
          print(f"Id.....: {bebida['id']}")
        else:
          print("Bebida no encontrada.")

     def eliminar_bebida(self, id):

        self.cursor.execute(f"DELETE FROM bebidas WHERE id =
{id}")
        self.conn.commit()
        return self.cursor.rowcount > 0

 

     def listar_bebidas(self):
         self.cursor.execute("select * from bebidas")
         bebidas = self.cursor.fetchall() 
         print("-" * 50)
         for bebida in bebidas:
           print(f"Nombre....: {bebida['nombre']}")
           print(f"Precio...: {bebida['precio']}")
           print(f"Tipo...: {bebida['tipo']}")
           print(f"Id....: {bebida['id']}")
           print("-" * 50)


class CatalogoClientes:
     def __init__(self, host, user, password, database):
      
      self.conn = mysql.connector.connect(
       host=host,
       user=user,
       password=password,
       database=database
)
      self.cursor = self.conn.cursor(dictionary=True)
      self.cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
       nombre varchar(25),
       apellido varchar(25),
       email varchar(25),
       id int not null auto_increment,

       primary key (id))''')
      self.conn.commit()

     def agregar_clientes(self, nombre, apellido, email, id):
      self.cursor.execute(f'select * from clientes where id={id}')
      cliente_existe=self.cursor.fetchone()
      if cliente_existe:
        return False
     
      sql=f"insert into clientes (nombre, apellido, email, id) values('{nombre}','{apellido}','{email}',{id})"
      self.cursor.execute(sql)
      self.conn.commit()
      return True
     
     def consultar_cliente(self,id):
       self.cursor.execute(f"select * from clientes where id={id}")
       return self.cursor.fetchone()
     
     def modificar_cliente(self, nuevo_nombre, nuevo_apellido, nuevo_email, id):
      sql=f"update clientes set nombre='{nuevo_nombre}',apellido ='{nuevo_apellido}',email='{nuevo_email}' where id={id}"
      self.cursor.execute(sql)
      self.conn.commit()
      return self.cursor.rowcount>0
     
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

   # ...

     def listar_clientes(self):
         self.cursor.execute("select * from clientes")
         clientes = self.cursor.fetchall() 
         print("-" * 50)
         for cliente in clientes:
          print(f"Nombre....: {cliente['nombre']}")
          print(f"Apellido....: {cliente['apellido']}")
          print(f"Email....: {cliente['email']}")
          print(f"Id....: {cliente['id']}")
          print("-" * 50)

     def eliminar_cliente(self, id):
         self.cursor.execute(f"DELETE FROM clientes WHERE id =
{id}")
         self.conn.commit()
         return self.cursor.rowcount > 0


class CatalogoReservas:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor(dictionary=True)
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
            on update cascade)''')
        self.conn.commit()

    def agregar_reserva(self, id, id_cliente, id_plato, id_bebida, cantidad_personas, fecha, hora, turno):
        self.cursor.execute(f'select * from reservas where id={id}')
        reserva_existe = self.cursor.fetchone()
        if reserva_existe:
            return False

        sql = f"insert into reservas (id, id_cliente, id_plato, id_bebida, cantidad_personas, fecha, hora, turno) values({id},{id_cliente},{id_plato},{id_bebida},{cantidad_personas},'{fecha}','{hora}','{turno}')"
        self.cursor.execute(sql)
        self.conn.commit()
        return True

    def consultar_reserva(self, id):
        self.cursor.execute(f"select * from reservas where id={id}")
        return self.cursor.fetchone()

    def modificar_reserva(self, id, nuevo_id_cliente, nuevo_id_bebida, nuevo_id_plato, nueva_cant_personas, nueva_fecha,
                         nueva_hora, nuevo_turno):
        sql = f"update reservas set id_cliente={nuevo_id_cliente}, id_bebida={nuevo_id_bebida}, id_plato={nuevo_id_plato}, cantidad_personas={nueva_cant_personas}, fecha='{nueva_fecha}', hora='{nueva_hora}', turno='{nuevo_turno}' where id={id}"
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.rowcount > 0
    
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
       print("Plato no encontrado.")

    def listar_reservas(self):
        self.cursor.execute("select * from reservas")
        reservas=self.cursor.fetachall()
        print("-" * 50)
        for reserva in reservas:
          print(f"Id....: {reserva['id']}")
          print(f"Id cliente....: {reserva['id_cliente']}")
          print(f"Id plato....: {reserva['id_plato']}")
          print(f"Id bebida....: {reserva['id_bebida']}")
          print(f"Cantidad de personas....: {reserva['cantidad_personas']}")
          print(f"Fecha...: {reserva['fecha']}")
          print(f"Hora...: {reserva['hora']}")
          print(f"Turno....: {reserva['turno']}")
          print("-" * 50)
    
    def eliminar_reserva(self, id):
        self.cursor.execute(f"DELETE FROM reservas WHERE id =
{id}")
        self.conn.commit()
        return self.cursor.rowcount > 0
    
catalogoPlatos=CatalogoPlatos(host='localhost', user='root', password='root', database="tpfinalcodoacodo")
catalogoBebidas=CatalogoBebidas(host='localhost', user='root', password='root', database="tpfinalcodoacodo")
catalogoClientes=CatalogoClientes(host='localhost', user='root', password='root', database="tpfinalcodoacodo")
catalogoReservas=CatalogoReservas(host='localhost', user='root', password='root', database="tpfinalcodoacodo")

'''
catalogoPlatos.agregar_platos('Milanesas c/ pure','Vegetariana de berenjenas', 5000, 1)
catalogoBebidas.agregar_bebidas('cerveza',2000,'bebida c/alcohol 1.5lts', 1)
catalogoClientes.agregar_clientes('Gabriela','Pardo','gabriela@gmail.com',1)
catalogoReservas.agregar_reserva(1,1,1,1,3,'4/12','19hs','tarde')

# BUSCAMOS EL ITEM DE LA TABLA SEGUN ID

id_plato = int(input("Ingrese el id del plato: "))
platoI = catalogoPlatos.consultar_plato(id_plato)
if platoI:
 print(f"Plato encontrado: {platoI['id']} - \
{platoI['descripcion']}")
else:
 print(f'Plato {id_plato} no encontrado.')

id_bebida = int(input("Ingrese el id de la bebida: "))
bebidaI =catalogoBebidas.consultar_bebida(id_bebida)
if bebidaI:
 print(f"Bebida  encontrada: {bebidaI['id']} - \
{bebidaI['tipo']}")
else:
 print(f'bebida {id_bebida} no encontrado.')

id_cliente = int(input("Ingrese el id del cliente: "))
clienteI = catalogoClientes.consultar_cliente(id_cliente)
if clienteI:
 print(f"Cliente encontrado: {clienteI['id']} - \
{clienteI['apellido']}")
else:
 print(f'Cliente {id_cliente} no encontrado.')

id_reserva = int(input("Ingrese el id de la reserva: "))
reservaI = catalogoReservas.consultar_reserva(id_reserva)
if reservaI:
 print(f"Reserva encontrada: {reservaI['id']} - \
{reservaI['fecha']}")
else:
 print(f'Reserva {id_reserva} no encontrado.')
 

 #MOSTRAMOS Y MODIFICAMOS PRODUCTO

catalogoPlatos.mostrar_plato(1)
catalogoPlatos.modificar_plato('Milanesas c/ fritas','Suprema', 5000, 1)

catalogoBebidas.mostrar_bebida(1)
catalogoBebidas.modificar_bebida('vino',2000,'bebida c/alcohol 1.5lts', 1)

catalogoClientes.mostrar_cliente(1)
catalogoClientes.modificar_cliente('Gabriela Beatriz','Pardo','gabriela@gmail.com',1)

catalogoReservas.mostrar_reserva(1)
catalogoReservas.modificar_reserva(1,1,1,1,3,'4/12','13hs','mediodia')
'''
catalogoPlatos.listar_platos()
catalogoBebidas.listar_bebidas()
catalogoClientes.listar_clientes()
catalogoReservas.listar_reservas()
