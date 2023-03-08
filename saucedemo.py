import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin(unittest.TestCase):
    #setup browser yang dipakai / memanggil driver
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    #maintest 
    def test_success_login(self):
        driver = self.browser #launc browser
        driver.get("https://www.saucedemo.com/") #akses website
        driver.maximize_window() #membuat window full screen
        driver.implicitly_wait(10) #implicit wait
        driver.find_element(By.CSS_SELECTOR, "[data-test=username]").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test=error]"))) #explicit wait
        #response success login
        respon = driver.find_element(By.CLASS_NAME, "title").text 
        self.assertIn("Products", respon)
        url = driver.current_url
        self.assertEqual(url, "https://www.saucedemo.com/inventory.html")
        driver.minimize_window()

    def test_failed_login(self):
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        #response failed login
        response = driver.find_element(By.CSS_SELECTOR, "[data-test=error]").text 
        self.assertIn("Epic sadface: Sorry, this user has been locked out.", response)

    def tearDown(self):
        self.browser.close()
        
if __name__ == '__main__':
    unittest.main()