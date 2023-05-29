class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("profesion:",self.profesion)
        print("--------------------")
        
# Ejecución del programa principal
if __name__ == "__main__":
    # Crear una lista para almacenar las personas
    personas = []

    # Solicitar los datos y crear instancias de la clase Persona
    while True:
        nombre = input("Ingrese el nombre (o 'salir' para finalizar): ")
        if nombre.lower() == 'finalizar':
            break
        edad = input("Ingrese la edad: ")
        profesion = input("Ingrese profesion: ")
        persona = Persona(nombre, edad, profesion)
        personas.append(persona)

    # Mostrar los datos almacenados de las personas
    print("Datos de las personas:")
    for persona in personas:
        persona.mostrar()
