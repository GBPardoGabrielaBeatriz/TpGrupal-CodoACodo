class Catalogo:
    bebidas = []
    platos = []
    clientes = []
    reservas = []

    def agregar_bebida(self, nombre, precio, tipo, proveedor, descripcion, cantidad, codigo):

        if self.consultar_bebida(codigo):
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
        self.bebidas.append(nueva_bebida)
        return True

def consultar_bebida(self,codigo):
    for bebida in self.bebidas:
        if bebida['codigo'] == codigo:
            return bebida
    return False

#platos nombre, descripcion, precio
def agregar_plato(self,nombre, precio, descripcion,codigo):

    if self.consultar_plato(codigo):
       return False
    nuevo_plato = {
        'codigo': codigo,
        'descripcion': descripcion,
        'precio': precio,
        'nombre': nombre,   
    }
    self.platos.append(nuevo_plato)
    return True

def consultar_plato(self,codigo):
    for plato in self.platos:
        if plato['codigo'] == codigo:
            return plato
    return False


#clientes nombre, apellido, email
def agregar_cliente(self, nombre, apellido, email):

    if self.consultar_cliente(nombre):
       return False
    nuevo_cliente = {
        'nombre': nombre,
        'apellido': apellido,
        'email': email   
    }
    self.clientes.append(nuevo_cliente)
    return True

def consultar_cliente(self, codigo):
    for cliente in self.clientes:
        if cliente['codigo'] == codigo:
            return cliente
    return False

#reservas codigo cliente  plato bebida cantidad_personas fecha hora turno 

def agregar_reserva(self, codigo, cliente, plato, bebida,cantidad_personas,fecha, hora,turno):

    if self.consultar_reserva(codigo):
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
    self.reservas.append(nueva_reserva)
    return True

def consultar_reserva(self, codigo):
    for reserva in self.reservas:
        if reserva['codigo'] == codigo:
            return reserva
    return False

#LISTAR 
def listar_bebidas(self):
    print("-" * 50)
    for bebida in self.bebidas:
        print(f"Código.....: {bebida['codigo']}")
        print(f"Nombre: {bebida['nombre']}")
        print(f"Precio...: {bebida['precio']}")
        print(f"Tipo.....: {bebida['tipo']}")
        print(f"Descripción.....: {bebida['proveedor']}")
        print(f"Descripcion..: {bebida['descripcion']}")
        print(f"Cantidad..: {bebida['cantidad']}")
        print("-" * 50)

def listar_platos(self):
    print("-" * 50)
    for plato in self.platos:
        print(f"Código.....: {plato['codigo']}")
        print(f"Nombre: {plato['nombre']}")
        print(f"Precio...: {plato['precio']}")
        print(f"Tipo.....: {plato['tipo']}")
        print(f"Descripcion..: {plato['descripcion']}")
        print("-" * 50)
#clientes 
def listar_clientes(self):
    print("-" * 50)
    for cliente in self.clientes:
        print(f"Nombre: {cliente['nombre']}")
        print(f"Apellido...: {cliente['apellido']}")
        print(f"Email.....: {cliente['email']}") 
        print("-" * 50)
#reservas 
def listar_reservass(self):
    print("-" * 50)
    for reserva in self.reservas:
        print(f"Código.....: {reserva['codigo']}")
        print(f"Cliente: {reserva['cliente']}")
        print(f"Plato...: {reserva['plato']}")
        print(f"Bebida.....: {reserva['bebida']}")
        print(f"Cantidad de Personas.....: {reserva['cantidad_personas']}")
        print(f"Fecha..: {reserva['fecha']}")
        print(f"Hora..: {reserva['hora']}")
        print(f"Turno..: {reserva['turno']}")
        print("-" * 50)

    # MODIFICAR
# Bebida
def modificar_bebida(self, codigo, nueva_descripcion, nueva_cantidad,
nuevo_precio, nuevo_nombre, nuevo_proveedor, nuevo_tipo):
    for producto in self.bebidas:
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
def modificar_plato(self, codigo, nuevo_nombre, nuevo_precio, nueva_descripcion):
    for producto in self.platos:
        if producto['codigo'] == codigo:
                producto['descripcion'] = nueva_descripcion
                producto['precio'] = nuevo_precio
                producto['nombre'] = nuevo_nombre
        return True
        return False
    #clientes 
def modificar_cliente(self, codigo, nuevo_nombre, nuevo_apellido, nuevo_email):
        for producto in self.platos:
            if producto['codigo'] == codigo:
                producto['nombre'] = nuevo_nombre
                producto['apellido'] = nuevo_apellido
                producto['email'] = nuevo_email
            
            return True
        return False

    #reservas
def modificar_reserva(self, codigo, nuevo_cliente, nuevo_plato, nueva_bebida,  nueva_cantidad_personas,nueva_fecha, nueva_hora, nuevo_turno ):
        for producto in self.platos:
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

#Programa Principal: 
catalogo = Catalogo()
catalogo.agregar_bebida('Agua mineral.', 1000, 'Bebida sin alcohol 600cc',1)
catalogo.agregar_plato('Agua mineral.', 1000, 'Bebida sin alcohol 600cc',1)
print()
print("Listado de platos:")
catalogo.listar_platos()
print()
print("Datos de una reserva:")
catalogo.mostrar_reserva(1)
catalogo.eliminar_plato(1)
print()
print("Listado de bebidas:")
catalogo.listar_bebidas()