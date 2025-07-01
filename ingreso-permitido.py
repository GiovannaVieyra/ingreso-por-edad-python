# Paso 1: Pedir al usuario que ingrese la edad del cliente

edad = int(input ("Por favor, ingrese la edad del cliente: "))

# Paso 2: Verificar si la edad ingresada cumple con el requisito para ingresar al boliche

permitido = True if edad >= 18 else False

# Paso 3: Mostrar al usuario si el cliente puede o no entrar al boliche 

if permitido:
    print("!El cliente puede ingresar!")
else: 
    print("El cliente no puede ingresar")
