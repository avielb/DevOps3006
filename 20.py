from selenium import webdriver
from time import sleep
my_driver = webdriver.Chrome()
my_driver.get("file:///Users/avielb/Downloads/tip_calc%204/index.html")
my_driver.find_element(by="id", value="billamt").send_keys("100")
my_driver.find_element(by="xpath", value='//*[@id="serviceQual"]/option[4]').click()
my_driver.find_element(by="id", value="peopleamt").send_keys("5")
my_driver.find_element(by="id", value="musicamt").send_keys("5")
my_driver.find_element(by="id", value="calculate").click()
expected = "8.00"
actual = my_driver.find_element(by="id", value="tip").text

assert expected != actual
