class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        pais, lote, año = self.codigo.split('-')
        return f"Nombre: {self.nombre}\nCódigo: {self.codigo}\nPaís de origen: {pais}\nNúmero de lote: {lote}"

# Ejecutamos el programa principal
 
if __name__ == "__main__":
   producto = Producto("ProductoA", "CHILE-0001-2013")
# Tener cuidado con la identación
# Imprimir el objeto de forma literal
print(producto)