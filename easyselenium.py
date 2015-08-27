# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException

build = "XXX项目 xxx 版本"
url = ""
desired_cap = {}
wait_seconds = 0

def remoteDriver(url):
    desired_cap["project"] = project
    desired_cap["build"] = build
    driver = webdriver.Remote(url, desired_capabilities = desired_cap)
    wait = WebDriverWait(driver, wait_seconds)

def ChromeDriver():
    driver = webdriver.Chrome();
    wait = WebDriverWait(driver, wait_seconds)

def goto(url):
    driver.get(url)

def waitPage(title):
    wait.until(EC.title_is(title))

def switchToWindow(title):
    handles = driver.window_handles
    while len(handles) == 1:
        handles = driver.window_handles
    driver.switch_to_window(handles[len(handles) - 1])
    try:
        waitPage(title)
    except TimeoutException:
        driver.switch_to_window(handles[len(handles) - 2])

def switchToLightbox(path):
    wait.until(EC.visibility_of_element_located((By.XPATH, path)))

def switchToFrame(name):
    wait.until(EC.visibility_of_element_located((By.ID, name)))
    driver.switch_to_frame(name)

def getXPathByDynamicId(tag, value):
    return '//' + tag + '[contains(@id, ' + value +')]'

def getXPathByText(tag, value):
    return '//' + tag + '[contains(., ' + value +')]'

def click(path):
    if wait_seconds > 0:
        wait.until(EC.element_to_be_clickable((By.XPATH, path))).click()
    else:
        driver.find_element_by_xpath(path).click()

def rightClick(path):
    ActionChains(driver).context_click(driver.find_element_by_xpath(path)).perform()

def doubleClick(path):
    ActionChains(driver).double_click(driver.find_element_by_xpath(path)).perform()

def drag(sourcePath, targetPath):
    source = driver.find_element_by_xpath(sourcePath)
    target = driver.find_element_by_xpath(targetPath)
    ActionChains(driver).drag_and_drop(source, target).perform()

def select(path, index):
    if wait_seconds > 30:
        clickElement(path)
        Select(driver.find_element_by_xpath(path)).select_by_index(index)
    elif wait_seconds > 20:
        Select(wait.until(EC.visibility_of_element_located((By.XPATH, path)))).select_by_index(index)
    else:
        Select(driver.find_element_by_xpath(path)).select_by_index(index)

def inputText(path, text):
    if wait_seconds > 0:
        wait.until(EC.visibility_of_element_located((By.XPATH, path))).send_keys(text)
    else:
        driver.find_element_by_xpath(path).send_keys(text)

def getText(path):
    if wait_seconds > 0:
        return wait.until(EC.presence_of_element_located((By.XPATH, path))).text
    else:
        return driver.find_element_by_xpath(path).text

def pressCtrlX(key):
    ActionChains(driver).key_down(Keys.CONTROL).send_keys(key).key_up(Keys.CONTROL).perform()

def selectAll():
    pressCtrlX('a')

def copy():
    pressCtrlX('c')

def paste():
    pressCtrlX('v')
