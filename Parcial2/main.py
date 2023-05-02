# main para verificar el proyecto en un contexto global 
from datetime import datetime

from model.cliente import Cliente
from model.producto import Producto
from model.producto_control import ProductoControl
from model.antibiotico import Antibiotico
from model.pedido import Pedido
from model.factura import Factura
from model.producto_control import ControlPlagas
from model.producto_control import ControlFertilizantes

cliente = Cliente(nombre="Juan", cedula="123456")
fecha = datetime.now()
productos = [
    Producto(nombre="Producto 1", precio=5),
    Producto(nombre="Producto 2", precio=7.5),
    Producto(nombre="Producto 3", precio=3.5)
]
control_plagas = ControlPlagas(ica="5678", nombre="Control de plagas", frecuencia_aplicacion=15, valor=8.5, periodo_carencia=7)
control_fertilizantes = ControlFertilizantes(ica="9012", nombre="Fertilizante", frecuencia_aplicacion=30, valor=10.5, fecha_ultima_aplicacion=datetime.now())
antibiotico = Antibiotico(nombre="Antibiotico 1", precio=20, dosis=500, tipo_animal="Bovinos")
pedido = Pedido(cliente=cliente, fecha=fecha, productos=productos)
pedido.productos.append(control_plagas)
pedido.productos.append(control_fertilizantes)
pedido.productos.append(antibiotico)


numero_factura = 1
fecha_factura = datetime.now()
factura = Factura(cliente=pedido.cliente, productos=pedido.productos, numero=numero_factura, fecha=fecha_factura)


print("Número de factura:", factura.numero)
print("Fecha de la factura:", factura.fecha)
print("Nombre del cliente:", factura.cliente.nombre)
print("Productos comprados:")
for producto in factura.productos:
    print(producto.nombre, "-", producto.precio)
print("Valor total de la factura:", factura.valor_total)
