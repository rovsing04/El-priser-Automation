import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

web = "https://www.energifyn.dk/kundeservice/kundeservice-el/faq-el/hvad-er-prisen-pa-el/"


def best_of_24_hours():
    driver = webdriver.Chrome()
    driver.get(web)
    driver.minimize_window()

    try:
        wait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "graph-bar__tooltip"))
        )
    except:
        driver.quit()
        print("Prøv igen!")

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

    final = str(round(list[0] / 100, 2)).replace(".", ",")
    print("")
    print("################################################")
    print("Det billigeste idag bliver kl " + kl[0] + " med " + final + "kr")
    print("################################################")
    print("")

    driver.quit()

def best_of_12_hours():
    driver = webdriver.Chrome()
    driver.get(web)
    driver.minimize_window()

    try:
        wait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "graph-bar__tooltip"))
        )
    except:
        driver.quit()
        print("Prøv igen!")
    time.sleep(3)

    list = []
    kl = ["06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00",
          "18:00", "19:00", "20:00", "21:00", "22:00"]

    for y in range(0, 6):
        rem = driver.find_element(By.CLASS_NAME, 'graph-bar__tooltip')
        driver.execute_script("""
            var element = arguments[0];
            element.parentNode.removeChild(element);
            """, rem)

    for x in range(0, 18):
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

    for x in range(0, 16):
        if list[0] < list[1]:
            del list[1]
            del kl[1]
        else:
            del list[0]
            del kl[0]

    final = str(round(list[0] / 100, 2)).replace(".", ",")
    print("")
    print("################################################")
    print("Det billigeste idag bliver kl " + kl[0] + " med " + final + "kr")
    print("################################################")
    print("")

    driver.quit()

def best_under_x():
    print("")
    print(" Hvor meget vil du maks have?")
    print("")
    INP = input("-> ")

    if "," in INP:
        INP = INP.replace(",", ".")
    INP = float(INP)
    INP = INP * 100


    driver = webdriver.Chrome()
    driver.get(web)
    driver.minimize_window()

    try:
        wait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "graph-bar__tooltip"))
        )
    except:
        driver.quit()
        print("Prøv igen!")

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
    de = []
    for x in range(0, 24):
        if list[x] >= INP:
            de.append(x)
    de.reverse()
    for x in range(0, 24):
        try:
            del list[de[0]]
            del kl[de[0]]
            try:
                del de[0]
            except:
                pass

        except:
            pass

    print("")
    print("################################################")
    for x in range(0, 23):
        try:
            final = str(round(list[x] / 100, 2)).replace(".", ",")
            print(kl[x] + " med " + final + "kr")
        except:
            pass
    print("################################################")
    print("")

    driver.quit()

def see_all():
    driver = webdriver.Chrome()
    driver.get(web)
    driver.minimize_window()

    try:
        wait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "graph-bar__tooltip"))
        )
    except:
        driver.quit()
        print("Prøv igen!")

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

    print("")
    print("################################################")
    for x in range(0, 24):
        try:
            final = str(round(list[x] / 100, 2)).replace(".", ",")
            print(kl[x] + " med " + final + "kr")
        except:
            pass
    print("################################################")
    print("")

    driver.quit()

def see_mid():
    driver = webdriver.Chrome()
    driver.get(web)
    driver.minimize_window()

    try:
        wait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "graph-bar__tooltip"))
        )
    except:
        driver.quit()
        print("Prøv igen!")

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

    sum = math.fsum(list)/100
    sum = round(sum / 24, 2)

    print("")
    print("################################################")
    print("Gennemsnittet for idag bliver " + str(sum) + "kr")
    print("################################################")
    print("")

    driver.quit()

def menu():
    print("")
    print(" EL priser i Odense")
    print("")
    print(" 1) Bedste pris på 24 timer      4) Se alle priser")
    print(" 2) Bedste prist på dagen        5) Se gennemsnit")
    print(" 3) Pris under x")
    print("")
    print(" q) Luk Programmet")
    print("")


def main_functions():
    while True:

        menu()
        PEIN = input("Vælg: ")
        if PEIN == "1":
            best_of_24_hours()
            break
        elif PEIN == "q":
            break
        elif PEIN == "2":
            best_of_12_hours()
            break
        elif PEIN == "3":
            best_under_x()
            break
        elif PEIN == "4":
            see_all()
            break
        elif PEIN == "5":
            see_mid()
            break
        else:
            print("")
            print("Det er ikke en valgmulighed!")
            print("")


see_mid()