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

