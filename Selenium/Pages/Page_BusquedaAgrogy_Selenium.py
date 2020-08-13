from selenium.webdriver.common.keys import Keys


class Page_test_Ejemplo_Selenium():

    def __init__(self, mydriver):
        self.driver = mydriver
        self.SearchElement_xpath = "//input[@placeholder='Buscar...']"

    def SearchinAgrofy(self,texto):
        self.driver.find_element_by_xpath(self.SearchElement_xpath).send_keys(texto)
        self.driver.find_element_by_xpath(self.SearchElement_xpath).send_keys(Keys.ENTER)
        return


