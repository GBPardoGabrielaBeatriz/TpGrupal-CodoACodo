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

#reservas

#--------------------------
## Definimos una lista de diccionarios para almacenar las bebidas.
bebidas = []
platos = []
clientes = []
