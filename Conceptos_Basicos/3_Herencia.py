class Vehiculo:
    def __init__(self,velocidad,marca,modelo,color,velocidad_max):
        self.velocidad = velocidad
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad_max = velocidad_max

    def acelerar(self,velocidad):
        self.velocidad = self.velocidad + velocidad

        if self.velocidad > self.velocidad_max:
            print("Se Alcanzo la Velocidad Maxima del Vehiculo: " + str(self.velocidad_max))
            self.velocidad = self.velocidad_max

        else: print("Se Acelero, la velocidad es:" + str(self.velocidad))



    def frenar(self,velocidad):
        self.velocidad = self.velocidad - velocidad

        if self.velocidad < 0:
            self.velocidad = 0
            print("Se Freno, la velocidad es:" + str(self.velocidad))



#----------------------------------------------------------------------------------------

class Auto(Vehiculo):
    def __init__(self,velocidad,marca,modelo,color,velocidad_max,patente,ruedas): #Paso propiedades padres+propias
        self.patente = patente
        self.ruedas = ruedas
        super().__init__(velocidad,marca,modelo,color,velocidad_max) #Paso Propiedades Padre

    def arrancar(self):
        print("Arrancando el Auto")

    def apagar(self):
        print("Apagando el Auto")


#----------------------------------------------------------------------------------------

class Moto(Vehiculo):
    def __init__(self,velocidad,marca,modelo,color,velocidad_max,patente,color_casco): #Paso propiedades padres+propias
        self.patente = patente
        self.color_casco = color_casco
        super().__init__(velocidad,marca,modelo,color,velocidad_max) #Paso Propiedades Padre

    def arrancar(self):
        print("Arrancando La Moto")

    def apagar(self):
        print("Apagando La Moto")

    def HacerWilly(self):
        print("Yeah! Estoy haciendo Willy!!")

#----------------------------------------------------------------------------------------

# Creo Objeto Auto que va a heredar propiedades y metodos de la clase Auto y su clase Padre Vehiculos.
Auto_1 = Auto(0,"Ford","Taunus","Azul",150,"AAA111",4) #Le paso al constructor de la clase los parametros de mi Objeto de clase Padre + Hija.
print("Auto 1:")
Auto_1.arrancar()
print("La velocidad Inicial es:" + str(Auto_1.velocidad))
Auto_1.acelerar(int(input("Ingrese Velocidad de Aceleracion:")))
Auto_1.acelerar(int(input("Ingrese Velocidad de Aceleracion:")))
Auto_1.acelerar(int(input("Ingrese Velocidad de Aceleracion:")))
Auto_1.frenar(int(input("Ingrese Velocidad de Frenado:")))
print("La velocidad Final es:" + str(Auto_1.velocidad))
Auto_1.color = "Rojo"
print("El color del Auto 1 es:" + Auto_1.color)
Auto_1.apagar()

#----------------------------------------------------------------------------------------

# Creo Objeto Moto que va a heredar propiedades y metodos de la clase Moto y su clase Padre Vehiculos.

Moto_1 = Moto(0,"yamaha","SZ-RR 2017","Azul",300,"AAA111","Amarillo") #Le paso al constructor de la clase los parametros de mi Objeto de clase Padre + Hija.
print("Moto 1:")
Moto_1.arrancar()
print("La velocidad Inicial es:" + str(Moto_1.velocidad))
Moto_1.acelerar(int(input("Ingrese Velocidad de Aceleracion:")))
Moto_1.acelerar(int(input("Ingrese Velocidad de Aceleracion:")))
Moto_1.acelerar(int(input("Ingrese Velocidad de Aceleracion:")))
Moto_1.HacerWilly()
Moto_1.frenar(int(input("Ingrese Velocidad de Frenado:")))
print("La velocidad Final es:" + str(Moto_1.velocidad))
print("El color de la Moto 1 es:" + Moto_1.color)
Moto_1.apagar()
