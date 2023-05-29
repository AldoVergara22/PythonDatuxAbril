import re

def validar_numero(entrada):
    patron = r'^\d+$'
    coincidencia = re.match(patron, entrada)
    if coincidencia:
        print("La entrada es un número válido.")
    else:
        print("La entrada no es un número válido.")


def validar_email(entrada):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    coincidencia = re.match(patron, entrada)
    if coincidencia:
        print("La entrada es una dirección de correo electrónico válida.")
    else:
        print("La entrada no es una dirección de correo electrónico válida.")

def validar_celular(entrada):
    patron = r'^\d{9}$'
    coincidencia = re.match(patron, entrada)
    if coincidencia:
        print("La entrada es un número de teléfono celular válido.")
    else:
        print("La entrada no es un número de teléfono celular válido.")

# Ejemplos de uso
validar_numero("12345")  # Válido
validar_numero("abc123")  # No válido

validar_email("correo@example.com")  # Válido
validar_email("correo@example")  # No válido

validar_celular("987654321")  # Válido
validar_celular("12345")  # No válido
