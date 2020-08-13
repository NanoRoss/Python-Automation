class Auto:
    def __init__(self,velocidad,marca,modelo,patente,velocidad_max):
        self.velocidad = velocidad
        self.marca = marca
        self.modelo = modelo
        self.patente = patente
        self.velocidad_max = velocidad_max
    color = ""

    def __str__(self): #Metodo para imprimir un Objeto entero cunado quiera con print(mi_objeto)
        return "Este es un auto Marca " +self.marca + " La velocidad Actual es: " + str(self.velocidad) + " La velocidad Maxima es de " + str(self.velocidad_max) + " El Modelo es: " + self.modelo + ",  la patente es " +self.patente + " y el color es: " + self.color


    def acelerar(self,velocidad):
        self.velocidad = self.velocidad + velocidad

        if self.velocidad > self.velocidad_max:
            self.velocidad = 200
            print("Se Alcanzo la Velocidad Maxima de 200 KMS/H")

        print("Se Acelero, la velocidad es:" + str(self.velocidad))




    def frenar(self,velocidad):
        self.velocidad = self.velocidad - velocidad

        if self.velocidad < 0:
            self.velocidad = 0
            print("Se Freno, la velocidad es:" + str(self.velocidad))


    def arrancar(self):
        print("Arrancando el Auto")

    def apagar(self):
        print("Apagando el Auto")


Auto_1 = Auto(0,"Ford","Taunus","AAA 111",200) #Le paso al constructor de la clase los parametros de mi Objeto.
print("Auto 1:")
Auto_1.arrancar()
print("La velocidad Inicial es:" + str(Auto_1.velocidad))
Auto_1.acelerar(int(input("Ingrese Velocidad de Aceleracion:")))
Auto_1.acelerar(int(input("Ingrese Velocidad de Aceleracion:")))
Auto_1.acelerar(int(input("Ingrese Velocidad de Aceleracion:")))
Auto_1.acelerar(int(input("Ingrese Velocidad de Aceleracion:")))
Auto_1.frenar(int(input("Ingrese Velocidad de Frenado:")))
print("La velocidad Final es:" + str(Auto_1.velocidad))
Auto_1.color = "Rojo"
print("El color del Auto 1 es:" + Auto_1.color)
Auto_1.apagar()
print(Auto_1) # Uso def __str__(self):


"""
print("-----------------------------------")
Auto_2 = Auto()
print("Auto 2:")
Auto_2.arrancar()
print("La velocidad es:" + str(Auto_2.velocidad))
Auto_2.acelerar(100)
Auto_2.frenar(10)
Auto_2.frenar(10)
Auto_2.frenar(10)
Auto_2.color = "Azul"
print("El color del Auto 2 es:" + Auto_2.color)
Auto_2.apagar()

"""