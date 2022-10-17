from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def main():
    driver = webdriver.Chrome()
    driver.get("https://create.roblox.com/docs/reference/engine")
    element = driver.find_element(By.ID, "tree-/Classes/Accessory")

    print(element)
