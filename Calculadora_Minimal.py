while True:
    cuestion = int(input("Seleciona una de las opciones.\n0-Salir\n1-sumar\n2-restar\n3-multiplicar\nRespuesta: "))
    numero1 = int(input("Escribe el primer número: "))
    numero2 = int(input("Escribe el segundo número: "))

    resultado = {
         1 : (numero1) + (numero2),
         2 : (numero1) - (numero2),
         3 : (numero1) * (numero2)
    }

    if cuestion == 0:
        exit()
    print(f"Tu resultado es: {resultado[cuestion]}")
