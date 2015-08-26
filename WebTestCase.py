# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import unittest
from easyselenium import EasySelenium

class WebTestCase(unittest.TestCase):
    build = "XXX项目 xxx 版本"
    url = ""
    desired_cap = {}
    wait_seconds = 0

    def setUp(self):
        self.result = ""
        self.driver = EasySelenium.ChromeDriver()

    def tearDown(self):
        self.driver.save_screenshot('screenshot.png')
        self.driver.quit()

    def testChrome(self):
        WebTestCase.wait_seconds = 30
        WebTestCase.desired_cap = desired_cap = {'browser': 'Chrome', 'browser_version': '32.0', 'os': 'OS X', 'os_version': 'Lion', 'resolution': '1024x768'}
        self.start()

    def testFireFox(self):
        WebTestCase.wait_seconds = 30
        WebTestCase.desired_cap = {'browser': 'Firefox', 'browser_version': '26.0', 'os': 'OS X', 'os_version': 'Lion', 'resolution': '1024x768'}
        self.start()

    def testIE8(self):
        WebTestCase.wait_seconds = 40
        WebTestCase.desired_cap = {'browser': 'IE', 'browser_version': '8.0', 'os': 'Windows', 'os_version': '7', 'resolution': '1024x768'}
        self.start()

    def testIE10(self):
        WebTestCase.wait_seconds = 40
        WebTestCase.desired_cap = {'browser': 'IE', 'browser_version': '10.0', 'os': 'Windows', 'os_version': '7', 'resolution': '1024x768'}
        self.start()

    def testSafari(self):
        WebTestCase.wait_seconds = 30
        WebTestCase.desired_cap = {'browser': 'Safari', 'browser_version': '7.0', 'os': 'OS X', 'os_version': 'Mavericks', 'resolution': '1024x768'}
        self.start()

    def testAndroid(self):
        WebTestCase.wait_seconds = 60
        WebTestCase.desired_cap = {'browserName': 'android', 'platform': 'ANDROID', 'device': 'Samsung Galaxy S III'}
        self.start()

    def testiPhone(self):
        WebTestCase.wait_seconds = 20
        WebTestCase.desired_cap = {'browserName': 'iPhone', 'platform': 'MAC', 'device': 'iPhone 5'}
        self.start()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(WebTestCase("testChrome"))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
