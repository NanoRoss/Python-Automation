#Las exepciones son errores en ejecucion.

def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):

	try:
		return num1/num2
	except:
		return "Error al dividir, valide numeros"



while True: #Bucle Infinito hasta llegar al break.
	try:
		op1 = (int(input("Introduce el primer número: ")))
		op2 = (int(input("Introduce el segundo número: ")))
		break
	except ValueError:
		print("Los valores Ingresados Son Incorrectos")



operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecúción del programa ")