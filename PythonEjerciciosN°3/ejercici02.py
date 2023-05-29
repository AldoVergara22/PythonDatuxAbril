# Creamos la clase producto
class Producto:
    def __init__(self, nombre, codigo, precio):
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio
# Creamos la clase catalogo
class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        self.productos.append(producto)

    def mostrar(self):
        for producto in self.productos:
            print(f"{producto.nombre} ({producto.codigo}): ${producto.precio}")

# ejercici02 = catalogo de productos
# Ejecución del programa principal
if __name__ == "__main__":
    ejercici02 = Catalogo()
    ejercici02.agregar(Producto("Bateria", "BT01", 2500))
    ejercici02.agregar(Producto("Frenos", "FR01", 500))
    ejercici02.agregar(Producto("Llanta", "LT01", 800))
    ejercici02.mostrar()