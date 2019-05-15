import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from appium import webdriver


class SearchProductsOnAndroid(unittest.TestCase):

    def setUp(self):

        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'dea66a407d73',
            'platformVersion': '6.0.1',
            'browserName': 'Chrome'
        }

        # To connect to Appium server use RemoteWebDriver and pass desired capabilities
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.get("http://google.com")

    def test_search(self):

        self.driver.find_element_by_name('q').send_keys('Appium')
        self.driver.find_element_by_name('q').send_keys(Keys.RETURN)
        self.driver.implicitly_wait(10)

    def tearDown(self):

        self.driver.close()


if __name__=='__main__':
    unittest.main(verbosity=2)


