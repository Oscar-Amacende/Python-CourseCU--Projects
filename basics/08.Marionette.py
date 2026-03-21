#Abrir una direccion en web desde un programa en python
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.google.com")
