# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException

class EasySelenium():
    build = "XXX项目 xxx 版本"
    url = ""
    desired_cap = {}
    wait_seconds = 0

    def setUp(self):
        self.result = ""

    def tearDown(self):
        self.driver.save_screenshot('screenshot.png')
        self.driver.close()

    def remoteDriver(self, url):
        EasySelenium.desired_cap["project"] = project
        EasySelenium.desired_cap["build"] = EasySelenium.build
        self.driver = webdriver.Remote(url, desired_capabilities = EasySelenium.desired_cap)
        self.wait = WebDriverWait(self.driver, EasySelenium.wait_seconds)

    def ChromeDriver(self):
        self.driver = webdriver.Chrome();
        self.wait = WebDriverWait(self.driver, EasySelenium.wait_seconds)

    def waitPage(self, title):
        self.wait.until(EC.title_is(title))

    def switchToWindow(self, title):
        handles = self.driver.window_handles
        while len(handles) == 1:
            handles = self.driver.window_handles
        self.driver.switch_to_window(handles[len(handles) - 1])
        try:
            self.waitPage(title)
        except TimeoutException:
            self.driver.switch_to_window(handles[len(handles) - 2])

    def switchToLightbox(self, path):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, path)))

    def switchToFrame(self, name):
        self.wait.until(EC.visibility_of_element_located((By.ID, name)))
        self.driver.switch_to_frame(name)

    def click(self, path):
        if EasySelenium.wait_seconds > 0:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, path))).click()
        else:
            self.driver.find_element_by_xpath(path).click()

    def rightClick(self, path):
        ActionChains(driver).context_click(self.driver.find_element_by_xpath(path)).perform()

    def doubleClick(self, path):
        ActionChains(driver).double_click(self.driver.find_element_by_xpath(path)).perform()

    def drag(self, sourcePath, targetPath):
        source = self.driver.find_element_by_xpath(sourcePath)
        target = self.driver.find_element_by_xpath(targetPath)
        ActionChains(driver).drag_and_drop(source, target).perform()

    def select(self, path, index):
        if EasySelenium.wait_seconds > 30:
            self.clickElement(path)
            Select(self.driver.find_element_by_xpath(path)).select_by_index(index)
        elif EasySelenium.wait_seconds > 20:
            Select(self.wait.until(EC.visibility_of_element_located((By.XPATH, path)))).select_by_index(index)
        else:
            Select(self.driver.find_element_by_xpath(path)).select_by_index(index)

    def input(self, path, text):
        if EasySelenium.wait_seconds > 0:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, path))).send_keys(text)
        else:
            self.driver.find_element_by_xpath(path).send_keys(text)

    def getText(self, path):
        if EasySelenium.wait_seconds > 0:
            return self.wait.until(EC.presence_of_element_located((By.XPATH, path))).text
        else:
            return self.driver.find_element_by_xpath(path).text

    def pressCtrlX(self, key):
        ActionChains(driver).key_down(Keys.CONTROL).send_keys(key).key_up(Keys.CONTROL).perform()

    def selectAll(self):
        pressCtrlX('a')

    def copy(self):
        pressCtrlX('c')

    def paste(self):
        pressCtrlX('v')
