from selenium import webdriver  # Importo el driver para poder interactuar con los navegadores.
from selenium.webdriver.chrome.options import Options as OpcionesChrome
import time  # Libreria para Pausas
from random import randint, uniform,random



def GenerarCuit_xWeb():
    CuitAleatoreo = "Error: no verifica!"
    while CuitAleatoreo == "Error: no verifica!":
        DNIAleatoreo = randint(32000000, 50999999)
        driver_cuit = webdriver.Chrome(executable_path=r'C:\drivers\chromedriver.exe')
        driver_cuit.minimize_window()
        driver_cuit.get("http://www0.unsl.edu.ar/~jolguin/cuit.php")
        time.sleep(5)
        driver_cuit.find_element_by_xpath("/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/form[1]/table[1]/tbody[1]/tr[1]/td[2]/font[1]/input[1]").send_keys(DNIAleatoreo)
        time.sleep(1)
        driver_cuit.find_element_by_xpath("//input[@name='Calcula']").click()
        time.sleep(1)
        CuitAleatoreo = (driver_cuit.find_element_by_name("cuit")).get_attribute("value")
        print(CuitAleatoreo)
        time.sleep(1)
    driver_cuit.close()
    return CuitAleatoreo

cuit = GenerarCuit_xWeb()
print(cuit)

