import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from TestCases import test_login, test_checkout
import HTMLRunner.HTMLTestRunner as HTMLTestRunner


class PythonOrg(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        time.sleep(3)

    def test1_login(self):
        mainPage = test_login.MainPage(self.driver)
        mainPage.LoginApp()

    def test2_checkout(self):
        mainPage = test_login.MainPage(self.driver)
        mainPage.LoginApp()
        mainPage = test_checkout.MainPage(self.driver)
        mainPage.CheckoutItem()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Completed")

if __name__ == "__main__":
    with open('report.html', 'w') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title='Test Report',
            description='Test Report'
        )
        unittest.main(testRunner=runner)