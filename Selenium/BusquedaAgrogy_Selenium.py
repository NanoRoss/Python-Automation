
import unittest  #Libreria necesaria para que el IDE interprete que estamos escribiendo una prueba
from selenium import webdriver  #Importo el driver para poder interactuar con los navegadores.
from selenium.webdriver.common.keys import Keys #Librerias para enviar teclas
import time #Libreria para Pausas
from Selenium.Pages.Page_BusquedaAgrogy_Selenium import Page_test_Ejemplo_Selenium

#---------------------------------------

class SetAgrofyMP(unittest.TestCase): # Declaro una clase de tipo unittest. Esto hace que python entienda que es un test.

    def setUp(self): #Declaro UNA función setUp para inicializar el driver. Self es el retorno de la funcion que luego utilizan los test.
        self.driver = webdriver.Chrome(executable_path=r'C:\drivers\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get("https://www.google.com/")
        self.page_test_Ejemplo_Selenium = Page_test_Ejemplo_Selenium(self.driver)




    def test_1_BuscarAgrofyCosechadoras_yValidar1erResultado(self):
        #self.driver.find_element_by_xpath("//input[@name='q']").send_keys("Agrofy")
        self.driver.find_element_by_name("q").send_keys("Agrofy")
        self.driver.find_element_by_xpath("//input[@name='q']").send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath("//h3[contains(text(),'Agrofy, el mercado online de la agroindustria | Pr')]").click()

        self.page_test_Ejemplo_Selenium.SearchinAgrofy("Tractor Pauny 280A")

        time.sleep(5)
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/a[1]").click()


        self.driver.find_element_by_xpath("/html[1]").click()


        asserttext = (self.driver.find_element_by_xpath("//h1[@class='font-28 ng-binding']").text)
        print("El texto del objeto es:"+ asserttext)
        self.assertEqual(asserttext,"Tractor Pauny 280A Centro Cerrado")
        time.sleep(5)



    def tearDown(self):  #Cosas que yo quiero que pasen al finalizar el test.
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print("Hora del Test--> "+ current_time)
        self.driver.close()

    


