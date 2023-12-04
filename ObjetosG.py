class CatalogoPlatos:
    platos=[]
    def agregar_platos(self,nombre, descripcion, precio,id):

     if self.consultar_plato(id):
        return False

     nuevo_plato = {
        'nombre': nombre,
        'descripcion' : descripcion,
        'precio' : precio,
        'id' : id
    }
     self.platos.append(nuevo_plato)
     return True

    def consultar_plato(self,id):
     for plato in self.platos :
      if plato ['id'] == id :
        return plato
      return False 
    def listar_platos(self):
       print("-" * 50)
    

    def modificar_plato(self, nuevo_nombre, nueva_descripcion,nuevo_precio,id):
     for plato in self.platos:
      if plato ['id'] == id :
       plato['nombre']= nuevo_nombre
       plato['descripcion']=nueva_descripcion
       plato['precio']=nuevo_precio
      return True
     return False     

    def eliminar_plato(self,id):
     for plato in self.platos:
      if plato['id']==id:
       self.platos.remove(plato)
      return True
     return False 


    def eliminar_plato(self, id):
# Eliminamos un producto de la tabla a partir de su código
       self.cursor.execute(f"DELETE FROM platos WHERE id =
{id}")
       self.conn.commit()
       return self.cursor.rowcount > 0
    
#BEBIDAS

class CatalogoBebidas:
    bebidas = []

    def agregar_bebidas(self, nombre, precio, tipo, id):
        if self.consultar_bebida(id):
            return False

        nueva_bebida = {
            'nombre': nombre,
            'precio': precio,
            'tipo': tipo,
            'id': id
        }
        self.bebidas.append(nueva_bebida)
        return True

    def consultar_bebida(self, id):
        for bebida in self.bebidas:
            if bebida['id'] == id:
                return bebida
        return False

    def listar_bebidas(self):
        print("-" * 50)
        for bebida in self.bebidas:
            print(f'Nombre....: {bebida["nombre"]}')
            print(f'Tipo....: {bebida["tipo"]}')
            print(f'Precio....: {bebida["precio"]}')
            print(f'Id....: {bebida["id"]}')
            print("-" * 50)

    def modificar_bebida(self, nuevo_nombre, nueva_precio, nuevo_tipo, id):
        for bebida in self.bebidas:
            if bebida['id'] == id:
                bebida['nombre'] = nuevo_nombre
                bebida['precio'] = nueva_precio
                bebida['tipo'] = nuevo_tipo
                return True
        return False

    def eliminar_bebida(self, id):
        for bebida in self.bebidas:
            if bebida['id'] == id:
                self.bebidas.remove(bebida)
                return True
        return False


class CatalogoClientes:
    clientes = []

    def agregar_clientes(self, nombre, apellido, email, id):
        if self.consultar_cliente(id):
            return False

        nuevo_cliente = {
            'nombre': nombre,
            'apellido': apellido,
            'email': email,
            'id': id
        }
        self.clientes.append(nuevo_cliente)
        return True

    def consultar_cliente(self, id):
        for cliente in self.clientes:
            if cliente['id'] == id:
                return cliente
        return False

    def listar_clientes(self):
        print("-" * 50)
        for cliente in self.clientes:
            print(f'Nombre....: {cliente["nombre"]}')
            print(f'Apellido....: {cliente["apellido"]}')
            print(f'Email....: {cliente["email"]}')
            print(f'Id....: {cliente["id"]}')
            print("-" * 50)

    def modificar_cliente(self, nuevo_nombre, nuevo_apellido, nuevo_email, id):
        for cliente in self.clientes:
            if cliente['id'] == id:
                cliente['nombre'] = nuevo_nombre
                cliente['apellido'] = nuevo_apellido
                cliente['email'] = nuevo_email
                return True
        return False

    def eliminar_cliente(self, _id):
        for cliente in self.clientes:
            if cliente['id'] == id:
                self.clientes.remove(cliente)
                return True
        return False

class CatalogoReservas:
    reservas = []

    def agregar_reserva(self, id, id_cliente, id_plato, id_bebida, cantidad_personas, fecha, hora, turno):
        if self.consultar_reserva(id):
            return False
        nueva_reserva = {
            'id': id,
            'id_cliente': id_cliente,
            'id_plato': id_plato,
            'id_bebida': id_bebida,
            'cantidad_personas': cantidad_personas,
            'fecha': fecha,
            'hora': hora,
            'turno': turno
        }
        self.reservas.append(nueva_reserva)
        return True

    def consultar_reserva(self, id):
        for reserva in self.reservas:
            if reserva['id'] == id:
                return reserva
        return False

    def listar_reservas(self):
        print("-" * 50)
        for reserva in self.reservas:
            print(f'Id....: {reserva["id"]}')
            print(f'Id cliente....: {reserva["id_cliente"]}')
            print(f'Id plato....: {reserva["id_plato"]}')
            print(f'Id bebida....: {reserva["id_bebida"]}')
            print(f'Cantidad de personas....: {reserva["cantidad_personas"]}')
            print(f'Fecha....: {reserva["fecha"]}')
            print(f'Hora....: {reserva["hora"]}')
            print(f'Turno....: {reserva["turno"]}')
            print("-" * 50)

    def modificar_reserva(self, id, nuevo_id_cliente, nuevo_id_bebida, nuevo_id_plato, nueva_cant_personas,
                          nueva_fecha, nueva_hora, nuevo_turno):
        for reserva in self.reservas:
            if reserva['id'] == id:
                reserva['id_cliente'] = nuevo_id_cliente
                reserva['id_plato'] = nuevo_id_plato
                reserva['id_bebida'] = nuevo_id_bebida
                reserva['cantidad_personas'] = nueva_cant_personas
                reserva['fecha'] = nueva_fecha
                reserva['hora'] = nueva_hora
                reserva['turno'] = nuevo_turno
                return True
        return False

    def eliminar_reserva(self, id):
        for reserva in self.reservas:
            if reserva['id'] == id:
                self.reservas.remove(reserva)
                return True
        return False


# PRINCIPAL
# Instanciamos cada clase creada junto a sus métodos
catalogoPlatos = CatalogoPlatos()
catalogoBebidas = CatalogoBebidas()
catalogoClientes = CatalogoClientes()
catalogoReservas = CatalogoReservas()

catalogoReservas.agregar_reserva(1, 1, 1, 1, 4, '2023-12-03', '12:00', 'Noche')
print()
print("Listado de reservas")
catalogoReservas.listar_reservas()
print()
print("Modificar reservas")
catalogoReservas.modificar_reserva(1, 2, 2, 2, 5, '2023-12-04', '13:00', 'Tarde')
print()
catalogoReservas.listar_reservas()
print()
catalogoReservas.eliminar_reserva(1)
print()
catalogoReservas.listar_reservas()

catalogoPlatos.agregar_platos()
print()
print("Listado de platos")
catalogoPlatos.listar_platos()
print()
print("Modificar platos")
catalogoPlatos.modificar_plato()
print()
catalogoPlatos.listar_platos()
print()
catalogoPlatos.eliminar_plato()
print()
catalogoPlatos.listar_platos()