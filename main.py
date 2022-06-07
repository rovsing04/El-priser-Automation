from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

web = "https://www.energifyn.dk/kundeservice/kundeservice-el/faq-el/hvad-er-prisen-pa-el/"


driver = webdriver.Chrome()
driver.get(web)


try:
    wait = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "graph-bar__tooltip"))
    )
except:
    driver.quit()
    print("Didn't find text")
print("Found text")

list = []
kl = ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00",
      "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"]

for x in range(0, 24):
    data = driver.find_element(By.CLASS_NAME, 'graph-bar__tooltip').get_attribute("textContent")
    data = data.replace("øre/kWh", "")
    data = data.replace("\n    ", "")
    data = data.replace(",", ".")
    list.append(float(data))
    data = driver.find_element(By.CLASS_NAME, 'graph-bar__tooltip')
    driver.execute_script("""
    var element = arguments[0];
    element.parentNode.removeChild(element);
    """, data)

for x in range(0, 23):
    if list[0] < list[1]:
        del list[1]
        del kl[1]
    else:
        del list[0]
        del kl[0]

final = str(list[0]/100).replace(".", ",")
print("Det billigeste idag bliver kl " + kl[0] + " med " + final + "kr")

driver.quit()
