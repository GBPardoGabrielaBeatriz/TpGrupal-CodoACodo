#Programa Principal
#--------------------------
#Programa Principal

#Bebidas
def agregar_bebida(nombre, precio, tipo, proveedor, descripcion, cantidad, codigo):

    if consultar_bebida(codigo):
       return False
    nueva_bebida = {
        'codigo': codigo,
        'descripcion': descripcion,
        'cantidad': cantidad,
        'precio': precio,
        'nombre': nombre,
        'proveedor': proveedor,
        'tipo': tipo   
    }
    bebidas.append(nueva_bebida)
    return True

def consultar_bebida(codigo):
    for bebida in bebidas:
        if bebida['codigo'] == codigo:
            return bebida
    return False

#platos nombre, descripcion, precio
def agregar_plato(nombre, precio, descripcion,codigo):

    if consultar_plato(codigo):
       return False
    nuevo_plato = {
        'codigo': codigo,
        'descripcion': descripcion,
        'precio': precio,
        'nombre': nombre,   
    }
    platos.append(nuevo_plato)
    return True

def consultar_plato(codigo):
    for plato in platos:
        if plato['codigo'] == codigo:
            return plato
    return False


#clientes nombre, apellido, email
def agregar_cliente(nombre, apellido, email):

    if consultar_cliente(nombre):
       return False
    nuevo_cliente = {
        'nombre': nombre,
        'apellido': apellido,
        'email': email   
    }
    clientes.append(nuevo_cliente)
    return True

def consultar_cliente(codigo):
    for cliente in clientes:
        if cliente['codigo'] == codigo:
            return cliente
    return False

#reservas codigo cliente  plato bebida cantidad_personas fecha hora turno 

def agregar_reserva(codigo, cliente, plato, bebida,cantidad_personas,fecha, hora,turno):

    if consultar_reserva(codigo):
       return False
    nueva_reserva = {
        'codigo': codigo,
        'cliente': cliente,
        'plato': plato,
        'bebida': bebida,
        'cantidad_personas': cantidad_personas,
        'fecha': fecha,
        'hora': hora,    
        'turno': turno,  
    }
    reservas.append(nueva_reserva)
    return True

def consultar_reserva(codigo):
    for reserva in reservas:
        if reserva['codigo'] == codigo:
            return reserva
    return False

#--------------------------
## Definimos una lista de diccionarios para almacenar las bebidas.
bebidas = []
platos = []
clientes = []
reservas = []
## Definimos una lista de diccionarios para almacenar las bebidas.


# MODIFICAR
# Bebida
def modificar_bebida(codigo, nueva_descripcion, nueva_cantidad,
nuevo_precio, nuevo_nombre, nuevo_proveedor, nuevo_tipo):
    for producto in bebidas:
        if producto['codigo'] == codigo:
            producto['descripcion'] = nueva_descripcion
            producto['cantidad'] = nueva_cantidad
            producto['precio'] = nuevo_precio
            producto['nombre'] = nuevo_nombre
            producto['proveedor'] = nuevo_proveedor
            producto['tipo'] = nuevo_tipo
        return True
    return False
  
#platos nombre, descripcion, precio
def modificar_plato(codigo, nuevo_nombre, nuevo_precio, nueva_descripcion):
    for producto in platos:
        if producto['codigo'] == codigo:
            producto['descripcion'] = nueva_descripcion
            producto['precio'] = nuevo_precio
            producto['nombre'] = nuevo_nombre
        return True
    return False
#clientes 
def modificar_cliente(codigo, nuevo_nombre, nuevo_apellido, nuevo_email):
    for producto in platos:
        if producto['codigo'] == codigo:
            producto['nombre'] = nuevo_nombre
            producto['apellido'] = nuevo_apellido
            producto['email'] = nuevo_email
           
        return True
    return False

#reservas
def modificar_reserva(codigo, nuevo_cliente, nuevo_plato, nueva_bebida,  nueva_cantidad_personas,nueva_fecha, nueva_hora, nuevo_turno ):
    for producto in platos:
        if producto['codigo'] == codigo:
            producto['cliente'] = nuevo_cliente
            producto['plato'] = nuevo_plato
            producto['bebida'] = nueva_bebida
            producto['cantidad_personas'] = nueva_cantidad_personas
            producto['fecha'] = nueva_fecha
            producto['hora'] = nueva_hora
            producto['turno'] = nuevo_turno
           
        return True
    return False

#LISTAR
def listar_bebidas():
    print("-" * 50)
    for bebida in bebidas:
        print(f"Código.....: {bebida['codigo']}")
        print(f"Nombre: {bebida['nombre']}")
        print(f"Precio...: {bebida['precio']}")
        print(f"Tipo.....: {bebida['tipo']}")
        print(f"Descripción.....: {bebida['proveedor']}")
        print(f"Descripcion..: {bebida['descripcion']}")
        print(f"Cantidad..: {bebida['cantidad']}")
        print("-" * 50)

def listar_platos():
    print("-" * 50)
    for plato in platos:
        print(f"Código.....: {plato['codigo']}")
        print(f"Nombre: {plato['nombre']}")
        print(f"Precio...: {plato['precio']}")
        print(f"Tipo.....: {plato['tipo']}")
        print(f"Descripcion..: {plato['descripcion']}")
        print("-" * 50)
#clientes 
def listar_clientes():
    print("-" * 50)
    for cliente in clientes:
        print(f"Nombre: {cliente['nombre']}")
        print(f"Apellido...: {cliente['apellido']}")
        print(f"Email.....: {cliente['email']}") 
        print("-" * 50)
#reservas codigo cliente  plato bebida cantidad_personas fecha hora turno 
def listar_reservass():
    print("-" * 50)
    for reserva in reservas:
        print(f"Código.....: {reserva['codigo']}")
        print(f"Cliente: {reserva['cliente']}")
        print(f"Plato...: {reserva['plato']}")
        print(f"Bebida.....: {reserva['bebida']}")
        print(f"Cantidad de Personas.....: {reserva['cantidad_personas']}")
        print(f"Fecha..: {reserva['fecha']}")
        print(f"Hora..: {reserva['hora']}")
        print(f"Turno..: {reserva['turno']}")
        print("-" * 50)
#eliminar
def eliminar_bebida(codigo):
    for bebida in bebidas:
        if bebida['codigo'] == codigo:
            bebidas.remove(bebida)
        return True
    return False

def eliminar_plato(codigo):
    for plato in platos:
        if plato['codigo'] == codigo:
            platos.remove(plato)
        return True
    return False

def eliminar_cliente(codigo):
    for cliente in clientes:
        if cliente['codigo'] == codigo:
            clientes.remove(cliente)
        return True
    return False

def eliminar_reserva(codigo):
    for reserva in reservas:
        if reserva['codigo'] == codigo:
            reservas.remove(reserva)
        return True
    return False