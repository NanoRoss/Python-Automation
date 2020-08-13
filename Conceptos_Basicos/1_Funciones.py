from src.functions.funciones_1 import LeoNumero_LoMultiplicox10yRetorno
from src.functions.funciones_1 import Datos_Personales

#--------------------------------------------------------------------------------------------------------
#Juego adivina Numero

"""
numerobuscado = input("Ingrese un numero A BUSCAR entre el 1 y 10:")
numeroingresado = input("Adivina el Numero entre 1 y 10:")

while numeroingresado != numerobuscado:  #Se ejecuta mientras la condicion sea true.

    if numeroingresado > numerobuscado:
        numeroingresado = input(" Casi! Pista: El numero es mas chico!! Intente nuevamente: -->")

    else:
        numeroingresado = input(" Casi! Pista: El numero es mas Grande!! Intente nuevamente: -->")

print("CORRECTO!, El numero era", numeroingresado)
"""


#--------------------------------------------------------------------------------------------------------

"""
print("llamo a la funcion LeoNumero_LoMultiplicox10yRetorno")
Numero_a_Multiplicar = input("Ingrese un numero a marultiplic x10:")
Numero_Multiplicado = LeoNumero_LoMultiplicox10yRetorno(Numero_a_Multiplicar)
print(Numero_Multiplicado)
#print(LeoNumero_LoMultiplicox10yRetorno(5))
"""

#--------------------------------------------------------------------------------------------------------

print("Datos Personales:")
datos = Datos_Personales() #Le paso a la variable datos el array de Datos.
print("El Nombre es:" + datos[0])
print("El Edad es:" + datos[1])
print("El Dni es:" + datos[2])



#--------------------------------------------------------------------------------------------------------