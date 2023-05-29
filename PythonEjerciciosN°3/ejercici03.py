# Definimos la función dividir en el codigo
def dividir(n1, n2):
   if n2!=0:
      div = n1 / n2
      return div 
   else:
       print("No existe, No se puede dividir entre cero.")
        
# Ejecución de la funcion principal
if __name__ == "__main__":
    opcion = ""
    while opcion != "2":
        print("        <<<MENU>>> \n")
        print("----------------------")
        print("1. Dividir dos números")
        print("2. Salir")
        print("----------------------\n")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            n1 = float(input("Digite el 1er número: "))
            n2 = float(input("Digite el 2do número: "))
            div = dividir(n1, n2)
            if div is not None:
                print(f"El resultado de la división es: {div}")
        elif opcion != "2":
            print("Opción no válida.")