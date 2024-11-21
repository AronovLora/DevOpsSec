from selenium import webdriver
from time import sleep


d=webdriver.Chrome()
d.get("file:///C:/Users/asafa/Downloads/tip_calc/tip_calc/index.html")
d.find_element(by="id", value="billamt").send_keys("100")
d.find_element(by="xpath",value="/html/body/div/div[1]/form/p[4]/select/option[3]").click()
d.find_element(by="id",value="peopleamt").send_keys("5")
sleep(10)





