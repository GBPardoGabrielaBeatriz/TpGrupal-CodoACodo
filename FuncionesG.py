#CREATE CON CADA UNA DE LAS TABLAS

def agregar_platos(nombre, descripcion, precio,id):

  if consultar_plato(id):
    return False

    nuevo_plato = {
        'nombre': nombre,
        'descripcion' : descripcion,
        'precio' : precio,
        'id' : id
    }
    platos.append(nuevo_plato)
    return True

def consultar_plato(id):
  for plato in platos :
    if plato ['id'] == id :
        return plato
    return False 

def agregar_bebidas(nombre,precio,tipo,id):
  
  if consultar_bebida(id):
    return False
  
  nueva_bebida={
    'nombre':nombre,
    'precio':precio,
    'tipo':tipo,
    'id':id
  }
  bebidas.append(nueva_bebida)
  return True

def consultar_bebida(id):
    for bebida in bebidas:
        if bebida['id'] == id:
            return bebida
    return False

def agregar_clientes(nombre, apellido, email, id):
  if consultar_cliente(id):
    return False
  
  nuevo_cliente={
    'nombre':nombre,
    'apellido':apellido,
    'email' : email,
    'id':id
  }
  clientes.append(nuevo_cliente)
  return True

  def consultar_cliente(id):
    for cliente in clientes:
        if cliente['id'] == id:
            return cliente
    return False

    
def agregar_reserva(id,id_cliente,id_plato,id_bebida,cantidad_personas,fecha,hora,turno):
  if consultar_reserva(id):
    return False
  nueva_reserva={
'id':id,
'id_cliente':id_cliente,
'id_plato':id_plato,
'id_bebida':id_bebida,
'cantidad_personas':cantidad_personas,
'fecha':fecha,
'hora':hora,
'turno':turno
  }
  reservas.append(nueva_reserva)
  return True

  def consultar_reserva(id):
    for reserva in reservas:
      if reserva['id'] == id :
        return reserva
      return False



#LISTAR CADA UNA DE LAS TABLAS

def listar_platos():
  print("-" * 50)
  for plato in platos:
    print(f'Nombre....: {plato['nombre']}')
    print(f'Descripcion....: {plato['descripcion']}')
    print(f'Precio....: {plato['precio']}')
    print(f'Id....: {plato['id']}')
    print("-" * 50)

def listar_bebidas():
  print("-" * 50)
  for bebida in bebidas:
    print(f'Nombre....: {bebida['nombre']}')
    print(f'Tipo....: {bebida['tipo']}')
    print(f'Precio....: {bebida['precio']}')
    print(f'Id....: {bebida['id']}')
    print("-" * 50)

def listar_clientes():
  print("-" * 50)
  for cliente in clientes:
    print(f'Nombre....: {cliente['nombre']}')
    print(f'Apellido....: {cliente['apellido']}')
    print(f'Email....: {cliente['email']}')
    print(f'Id....: {cliente['id']}')
    print("-" * 50)

def listar_reservas():
  print("-" * 50)
  for reserva in reservas:
    print(f'Id....: {reserva['id']}')
    print(f'Id cliente....: {reserva['id_cliente']}')
    print(f'Id plato....: {reserva['id_plato']}')
    print(f'Id bebida....: {reserva['id_bebida']}')
    print(f'Cantidad de personas....: {reserva['cantidad_personas']}')
    print(f'Fecha....: {reserva['fecha']}')
    print(f'Hora....: {reserva['hora']}')
    print(f'Turno....: {reserva['turno']}')
    print("-" * 50)


# MODIFICAR TABLAS

def modificar_plato(nuevo_nombre, nueva_descripcion,nuevo_precio,id):
  for plato in platos:
    if plato ['id'] == id :
      plato['nombre']= nuevo_nombre
      plato['descripcion']=nueva_descripcion
      plato['precio']=nuevo_precio
      return True
    return False
  
def modificar_bebida(nuevo_nombre, nueva_precio,nuevo_tipo,id):
  for bebida in bebidas:
    if bebida['id'] == id :
      bebida['nombre']= nuevo_nombre
      bebida['precio']=nueva_precio
      bebida['tipo']=nuevo_tipo
      return True
    return False
  
def modificar_cliente(nuevo_nombre, nuevo_apellido,nuevo_email,id):
  for cliente in clientes:
    if cliente ['id'] == id :
      cliente['nombre']= nuevo_nombre
      cliente['apellido']=nuevo_apellido
      cliente['email']=nuevo_email
      return True
    return False
  
def modificar_reserva(id, nuevo_id_cliente,nuevo_id_bebida,nuevo_id_plato,nueva_cant_personas,nueva_fecha,nueva_hora,nuevo_turno):
  for reserva in reservas:
    if reserva ['id'] == id :
      reserva['id_cliente']= nuevo_id_cliente
      reserva['id_plato']=nuevo_id_plato
      reserva['id_bebida']=nuevo_id_bebida
      reserva['cantidad_personas']= nueva_cant_personas
      reserva['fecha']=nueva_fecha
      reserva['hora']=nueva_hora
      reserva['turno']=nuevo_turno
      return True
    return False
  
# ELIMINAR TABLAS

def eliminar_plato(id):
  for plato in platos:
    if plato['id']==id:
      platos.remove(plato)
      return True
    return False
  
def eliminar_bebida(id):
  for bebida in bebidas:
    if bebida['id']==id:
      bebidas.remove(bebida)
      return True
    return False
  
def eliminar_cliente(id):
  for cliente in clientes:
    if cliente['id']==id:
      clientes.remove(cliente)
      return True
    return False
  
def eliminar_reserva(id):
  for reserva in reservas:
    if reserva['id']==id:
      reservas.remove(reserva)
      return True
    return False


# PRINCIPAL--------------------------------------
platos = []
bebidas=[]
clientes =[]
reservas=[]
agregar_platos('Pastel de papa','Version vegetariana',3000,1)

print(platos)

id_platoI =int(input("Ingrese el Id del plato :"))
plato=consultar_plato(id_platoI)

id_bebidaI =int(input("Ingrese el Id de la bebida :"))
bebida=consultar_plato(id_bebidaI)

id_clienteI =int(input("Ingrese el Id del cliente :"))
cliente=consultar_cliente(id_clienteI)

id_reservaI =int(input("Ingrese el Id de la reserva :"))
reserva=consultar_reserva(id_reservaI)


if plato:
   print(f'Plato encontrado : {plato['nombre']} - {plato['id']}')
else :
  print(f'Plato {id}no encontrado')
 
if bebida:
   print(f'Bebida encontrada : {bebida['nombre']} - {bebida['id']}')
else :
  print(f'Bebida {id}no encontrada')

if cliente:
   print(f'Cliente  encontrado : {cliente['nombre']}-{cliente['apellido']} - {cliente['id']}')
else :
  print(f'Cliente {id}no encontrado')
  
if reserva:
   print(f'Reserva encontrada : {reserva['fecha']} - {reserva['id']}')
else :
  print(f'Reserva{id}no encontrado')






    