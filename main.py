from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
class TestReg(unittest.TestCase):
    def test_reg1(self):
        browser = webdriver.Chrome()
        browser.get(link1)
        input1 = browser.find_element(By.XPATH, "/html/body/div[1]/form/div[1]/div[1]/input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "/html/body/div[1]/form/div[1]/div[2]/input")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "/html/body/div[1]/form/div[1]/div[3]/input")
        input3.send_keys("Smolensk@mail.ru")
        button = browser.find_element(By.XPATH, "/html/body/div[1]/form/button").click()
        time.sleep(1)
        welcome_text_elem = browser.find_element(By.XPATH, "/html/body")
        welcome_text = welcome_text_elem.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        browser.quit()
    def test_reg2(self):
        browser = webdriver.Chrome()
        browser.get(link2)
        input1 = browser.find_element(By.XPATH, "/html/body/div[1]/form/div[1]/div[1]/input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "/html/body/div[1]/form/div[1]/div[2]/input")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "/html/body/div[1]/form/div[1]/div[3]/input")
        input3.send_keys("Smolensk@mail.ru")
        button = browser.find_element(By.XPATH, "/html/body/div[1]/form/button").click()
        time.sleep(1)
        welcome_text_elem = browser.find_element(By.XPATH, "/html/body")
        welcome_text = welcome_text_elem.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        browser.quit()
if __name__ == '__main__':
    unittest.main(warnings='ignore') # for PyTest input "pytest main.py" in Terminal 