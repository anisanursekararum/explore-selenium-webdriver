import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class DemoQA(unittest.TestCase):
    #setup browser yang dipakai / memanggil driver
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    #maintest 
    def test_switch_tab(self):
        driver = self.browser
        driver.get("https://demoqa.com/browser-windows")
        driver.maximize_window()
        driver.find_element(By.ID, "tabButton").click()
        driver.switch_to.window(driver.window_handles[1])
        url = driver.current_url
        self.assertEqual(url, "https://demoqa.com/sample")
    
    def test_select_menu(self):
        driver = self.browser
        driver.get("https://demoqa.com/select-menu")
        driver.maximize_window()
        select = Select(driver.find_element(By.ID, "oldSelectMenu"))
        select.select_by_value('9')
        
if __name__ == '__main__':
    unittest.main()