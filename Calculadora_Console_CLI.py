import os
import json

datos_existentes = []

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def guardar_datos(text,Hiso):
    name_archive = "Historial.txt"
    texto = [Hiso]
    with open(name_archive, 'a', encoding='utf-8') as f:
        for item in text,texto:
            f.write(str(item) + '\n')
        

class calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def suma(self):
        limpiar()
        resultado = self.num1 + self.num2
        text = f"{self.num1} + {self.num2} = "
        print(f"El resultado es {resultado}")
        input("preciona enter para continuar...")
        text = f"{self.num1} + {self.num2} = "
        guardar_datos(text,resultado)
        
    def resta(self):
        limpiar()
        resultado = self.num1 - self.num2
        print(f"El resultado es {resultado}")
        input("preciona enter para continuar...")
        text = f"{self.num1} - {self.num2} = "
        guardar_datos(text,resultado)
        
    def multiplicacion(self):
        limpiar()
        resultado = self.num1 * self.num2
        print(f"El resultado es {resultado}")
        input("preciona enter para continuar...")
        text = f"{self.num1} * {self.num2} = "
        guardar_datos(text,resultado)
    def division(self):
        try:
            limpiar()
            resultado = self.num1 / self.num2
            print(f"El resultado es {resultado}")
            input("preciona enter para continuar...")
            text = f"{self.num1} / {self.num2} = "
            guardar_datos(text,resultado)
        except ZeroDivisionError:
            limpiar()
            print("intenta de nuevo")
            input("preciona enter para continuar...")
            
def Calculator():
    limpiar()
    print("--A continuación escribe los digitos pedidos--")
    numero1 = int(input("Escribe el primer numero: "))
    numero2 = int(input("Escribe el segundo numero: "))
    cac = calculadora(numero1, numero2)
    operador = int(input("Elije a continuacion un operador \n \n1. sumar \n2. restar \n3. multiplicar \n4. dividir \n0. Atras \nEscribe: "))
    match operador:
        case 1:
            cac.suma()
        case 2:
            cac.resta()
        case 3:
            cac.multiplicacion()
        case 4:
            cac.division()
        case _:
            print("ok")
def Historial():
    limpiar()
    #leer el historial
    name_archive = "Historial.txt"
    with open(name_archive, 'r', encoding='utf-8') as f:
        
         for lines in f.readlines():
             print(lines.strip())
    input("preciona una tecla")
    limpiar()
 
while True:
    print("--Calculadora en Terminal-- \n \n1. Calcular \n2. Ver historial \n3. Salir")
    elec = int(input("Escribe una opcion: "))
    match elec:
        case 1:
            Calculator()
        case 2:
            Historial()
        case 3:
            break
        case _:
            input("Intentalo de nuevo, preciona una tecla para continuar...")
            continue
    