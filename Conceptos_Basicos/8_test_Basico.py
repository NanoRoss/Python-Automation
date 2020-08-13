
import unittest  #Libreria necesaria para que el IDE interprete que estamos escribiendo una prueba
import time

#---------------------------------------

class ClaseTest(unittest.TestCase): # Declaro una clase de tipo unittest. Esto hace que python entienda que es un test.

    def setUp(self): #Declaro UNA función setUp para inicializar el driver. Self es el retorno de la funcion que luego utilizan los test.
        pass


    def test_1_Print_Hola(self):
        a = 3
        b = 4
        y = a + b 
        print("El valor de y es:" + y)

    
    def test_2_Print_Hola(self):
        print("22222222222222222222")

    
    def test_3_Print_Hola(self):
        print("333333333333333")


    def test_4_PrintSarasa(self):
        print("444444444444444")

    
    
    def test_5_PrintSarasa(self):
        print("asdsadasdsadas")

    
 


    def tearDown(self):  #Cosas que yo quiero que pasen al finalizar el test.
        print("Terminaron todas las pruebas")
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print("Hora del Test--> "+ current_time)
        
   
   
   