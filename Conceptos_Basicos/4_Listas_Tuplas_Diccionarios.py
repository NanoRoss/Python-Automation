#Lista = ["Mariano","Marcelo","Mauricio","Anita"]
#Tupla = ("Mariano",123,True,"Carlos")
#diccionario_PaisCapital= {"Alemania":"Berlin","Argentina":"Buenos Aires","Francia":"Pais"}


#---------------------------------------------------------------
#Listas


Lista_1 = ["Mariano","Marcelo","Mauricio","Anita"]

print(Lista_1)
#print(Lista_1[0:7]) #Desde/hasta cual queremos mostrar.

Lista_1.append("Carlos") #Agrego un elemento a la Lista.
print(Lista_1)

Lista_1.insert(0,"Ana") #Agrego un elemento a la Lista en una posicion determinada. 
print(Lista_1)

Lista_1.extend(["Alciro","Josefa"]) #Agrego varios elementos a la lista. 
print(Lista_1)

print(Lista_1.index("Carlos")) #Retorna la posicion/indice de un elemento en la lista.

print("------------")
Lista_2 = ["Mariano","Marcelo","Mauricio","Anita"] * 2 #Repito la lista n veces
print(Lista_2)

#---------------------------------------------------------------
#Tuplas: Las tuplas, son listas que no se pueden modificar.
print("------------")
Tupla1 = ("Mariano",123,True,"Carlos")
print(Tupla1)
Lista_Ex_Tupla = list(Tupla1) #Convierto mi tupla en Lista para poder modificarla.
Lista_Ex_Tupla.extend(["Agus","Luz"])


#---------------------------------------------------------------
#Diccionarios: 
#Estructura de datos que permite almacenar valores de diff tipos.
#Los datos se almacenan en pares clave:valor EJ: Pais->Capital
#El orden es indiferente en un diccionario.

diccionario_PaisCapital={"Alemania":"Berlin","Argentina":"Buenos Aires","Francia":"Pais"}

print(diccionario_PaisCapital)
print(diccionario_PaisCapital["Argentina"]) #Paso clave y obtengo Valor.






































