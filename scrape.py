# Use this module to update the dataset


import mysql.connector
import requests
import pandas
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

mydb = mysql.connector.connect(user='root', password='sh.bisto5',
                               host='localhost',
                               database='fin5_jadidb')
mycursor = mydb.cursor()

# scraping

def scrape(inp):
    # part 1 scraping
    c = 0
    PATH = 'C:\Program Files (x86)\chromedriver.exe'
    driver = webdriver.Chrome()
    driver.get('https://bama.ir/car?brand=pride&brand=renault,tondar90&brand=peugeot,206ir(type2,type3,type3panorama,type5,type6)&priced=1')

    time.sleep(1)
    for o in range(inp):
        f = o * 1080
        driver.execute_script(f"window.scrollTo({f}, {f + 1080})")
        time.sleep(0.25)
    time.sleep(2)
    # scraping car's details
    time.sleep(1)
    prices = driver.find_elements(By.CLASS_NAME,"bama-ad__price-holder")
    time.sleep(1)
    els = driver.find_elements(By.CLASS_NAME, "bama-ad__title")
    time.sleep(1)
    det = driver.find_elements(By.CLASS_NAME,'bama-ad__detail-row')
    for i in range(len(det)):
        s = det[i].text.split()

        # defining car's details
        price = prices[i].text
        name = els[i].text
        model = s[0]
        mileage = s[1] + ' ' + s[2]
        trim = ' '.join(s[3:])
        details = (name, mileage, model, trim)

        a = 0
        b = 0
        mycursor.execute("SHOW TABLES;")
        one = mycursor.fetchall()

        # Check if table already exist
        for i in one:
            if i == ('car',):
                a += 1
        if a == 0:
            mycursor.execute("CREATE TABLE car (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50),mileage VARCHAR(100),model VARCHAR(30),trim VARCHAR(100), price VARCHAR(100));")
            two = mycursor.fetchall()

        # check if the data is repetitious
        mycursor.execute("SELECT * FROM car;")
        three = mycursor.fetchall()
        for r in three:
            if r == details:
                b += 1
        if b == 0:
            # inserting data into table
            mycursor.execute("INSERT INTO car(name, mileage, model, trim, price) VALUES ('%s', '%s', '%s', '%s', '%s');" % (name, mileage, model, trim, price))
            four = mycursor.fetchall()

        mydb.commit()

    time.sleep(5)
    driver.quit()
    pass


# cleaning data for 206 

def peju206():
    c = 0
    id = []
    # drop the migration made table
    mycursor.execute('DROP TABLE IF EXISTS polls_p206_c')
    bb = mycursor.fetchall()
    # create the table again to insert cleaned data
    mycursor.execute(
        "CREATE TABLE polls_p206_c (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), mileage INT, model INT, trim INT, price INT)")
    Q = mycursor.fetchall()
    mycursor.execute("SELECT id,trim,model,mileage,price FROM car WHERE name = 'پژو، 206';")
    output = mycursor.fetchall()
    for i in output:
        id.append(i[0])
        c += 1

    for i in range(c):
        mycursor.execute("SELECT mileage FROM car WHERE id = %i" % id[i])
        p = mycursor.fetchall()
        mycursor.execute("SELECT trim FROM car WHERE id = %i" % id[i])
        t = mycursor.fetchall()
        mycursor.execute("SELECT price FROM car WHERE id = %i" % id[i])
        k = mycursor.fetchall()
        mycursor.execute("SELECT model FROM car WHERE id = %i" % id[i])
        m = mycursor.fetchall()

        tr = ''
        ml = ''
        if 'صفر' in p[0][0].split():
            ml = 0
        elif 'کارکرده' in p[0][0].split():
            ml = 100
        else:
            ml = p[0][0].split()[0].split(',')[0]

        try:
            if int(t[0][0].split()[1]) == 2:
                tr = 1
            elif int(t[0][0].split()[1]) == 6:
                tr = 2
            elif int(t[0][0].split()[1]) == 5:
                tr = 3
            elif int(t[0][0].split()[1]) == 3:
                tr = 4
        except :
            tr = 0

        # insert the cleaned data
        mycursor.execute("INSERT INTO polls_p206_c (name, mileage, model, trim, price) VALUES ('پژو، 206', '%s', '%s', '%s', '%s');" % ((int(ml)), (int(m[0][0]) - 1380) , int(tr) * 100, int(k[0][0].split(',')[0])))

        mydb.commit()
        pass


# cleaning data for l90

def l90():
    c = 0
    id = []
    mycursor.execute('DROP TABLE IF EXISTS polls_l90_c')
    bb = mycursor.fetchall()
    # create the table again to insert cleaned data
    mycursor.execute(
        "CREATE TABLE polls_l90_c (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), mileage INT, model INT, trim INT, price INT)")
    Q = mycursor.fetchall()
    mycursor.execute("SELECT id,trim,model,mileage,price FROM car WHERE name = 'رنو، تندر 90';")
    output = mycursor.fetchall()
    for i in output:
        id.append(i[0])
        c += 1

    for i in range(c):
        mycursor.execute("SELECT mileage FROM car WHERE id = %i" % id[i])
        p = mycursor.fetchall()
        mycursor.execute("SELECT trim FROM car WHERE id = %i" % id[i])
        t = mycursor.fetchall()
        mycursor.execute("SELECT price FROM car WHERE id = %i" % id[i])
        k = mycursor.fetchall()
        mycursor.execute("SELECT model FROM car WHERE id = %i" % id[i])
        m = mycursor.fetchall()

        tr = 200
        ml = ''
        if 'صفر' in p[0][0].split():
            ml = 0
        elif 'کارکرده' in p[0][0].split():
            ml = 100
        else:
            ml = p[0][0].split()[0].split(',')[0]

        try:
            if 'E0' in t[0][0]:
                tr = 1
            elif 'E1' in t[0][0]:
                tr = 2
            elif 'E2' in t[0][0]:
                tr = 3
            elif 'اتوماتیک' in t[0][0]:
                tr = 4
            elif 'پلاس دنده ای' in t[0][0]:
                tr = 5
            elif 'پلاس اتوماتیک' in t[0][0]:
                tr = 6
        except :
            tr = 0

        # insert the cleaned data
        mycursor.execute("INSERT INTO polls_l90_c (name, mileage, model, trim, price) VALUES ('رنو، تندر 90', '%s', '%s', '%s', '%s');" % ((int(ml)), (int(m[0][0]) - 1385) , int(tr) * 100, int(k[0][0].split(',')[0])))

        mydb.commit()

    pass

# cleaning data for pride

def pride():
    c = 0
    id = []
    mycursor.execute('DROP TABLE IF EXISTS polls_pride_c')
    bb = mycursor.fetchall()
    # create the table again to insert cleaned data
    mycursor.execute(
        "CREATE TABLE polls_pride_c (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), mileage INT, model INT, trim INT, price INT)")
    Q = mycursor.fetchall()
    mycursor.execute("SELECT id,trim,model,mileage,price FROM car WHERE name LIKE '%پراید%';")
    output = mycursor.fetchall()
    for i in output:
        id.append(i[0])
        c += 1

    for i in range(c):
        mycursor.execute("SELECT name FROM car WHERE id = %i" % id[i])
        n = mycursor.fetchall()
        mycursor.execute("SELECT mileage FROM car WHERE id = %i" % id[i])
        p = mycursor.fetchall()
        mycursor.execute("SELECT trim FROM car WHERE id = %i" % id[i])
        t = mycursor.fetchall()
        mycursor.execute("SELECT price FROM car WHERE id = %i" % id[i])
        k = mycursor.fetchall()
        mycursor.execute("SELECT model FROM car WHERE id = %i" % id[i])
        m = mycursor.fetchall()
        div = ''
        tr = 200
        ml = ''
        if 'صفر' in p[0][0].split():
            ml = 0
        elif 'کارکرده' in p[0][0].split():
            ml = 100
        else:
            ml = p[0][0].split()[0].split(',')[0]

        try:

            if '111' in n[0][0]:
                if 'SE' in t[0][0]:
                    tr = 6 + 5
                elif 'EX' in t[0][0]:
                    tr = 5 + 5
                elif 'TL' in t[0][0]:
                    tr = 4 + 5
                elif 'SX' in t[0][0]:
                    tr = 3 + 5
                elif 'LE' in t[0][0]:
                    tr = 2 + 5
                elif 'SL' in t[0][0]:
                    tr = 1 + 5
                else:
                    tr = 3 + 4
            elif '131' in n[0][0]:
                if 'SE' in t[0][0]:
                    tr = 6 + 3
                elif 'EX' in t[0][0]:
                    tr = 5 + 3
                elif 'TL' in t[0][0]:
                    tr = 4 + 3
                elif 'SX' in t[0][0]:
                    tr = 3 + 3
                elif 'LE' in t[0][0]:
                    tr = 2 + 3
                elif 'SL' in t[0][0]:
                    tr = 1 + 3
                else:
                    tr = 3 + 3
                div = 3
            elif '132' in n[0][0]:
                if 'SE' in t[0][0]:
                    tr = 6 + 2
                elif 'EX' in t[0][0]:
                    tr = 5 + 2
                elif 'TL' in t[0][0]:
                    tr = 4 + 2
                elif 'SX' in t[0][0]:
                    tr = 3 + 2
                elif 'LE' in t[0][0]:
                    tr = 2 + 2
                elif 'SL' in t[0][0]:
                    tr = 1 + 2
                else:
                    tr = 3 + 2
                div = 2
            elif '141' in n[0][0]:
                if 'SE' in t[0][0]:
                    tr = 6 + 1
                elif 'EX' in t[0][0]:
                    tr = 5 + 1
                elif 'TL' in t[0][0]:
                    tr = 4 + 1
                elif 'SX' in t[0][0]:
                    tr = 3 + 1
                elif 'LE' in t[0][0]:
                    tr = 2 + 1
                elif 'SL' in t[0][0]:
                    tr = 1 + 1
                else:
                    tr = 3 + 1
                div = 1
            elif '151' in n[0][0]:
                if 'SE' in t[0][0]:
                    tr = 6 + 4
                elif 'EX' in t[0][0]:
                    tr = 5 + 4
                elif 'TL' in t[0][0]:
                    tr = 4 + 4
                elif 'SX' in t[0][0]:
                    tr = 3 + 4
                elif 'LE' in t[0][0]:
                    tr = 2 + 4
                elif 'SL' in t[0][0]:
                    tr = 1 + 4
                else:
                    tr = 3 + 4
                div = 5
            elif 'صندوق دار' in n[0][0]:
                if 'SE' in t[0][0]:
                    tr = 6 + 4
                elif 'EX' in t[0][0]:
                    tr = 5 + 4
                elif 'TL' in t[0][0]:
                    tr = 4 + 4
                elif 'SX' in t[0][0]:
                    tr = 3 + 4
                elif 'LE' in t[0][0]:
                    tr = 2 + 4
                elif 'SL' in t[0][0]:
                    tr = 1 + 4
                else:
                    tr = 3 + 4
                div = 3
            else:
                div = 2 + 5
        except:
            div = 2
            tr = 3 + 2

        # insert the cleaned data
        mycursor.execute(
            "INSERT INTO polls_pride_c (name, mileage, model, trim, price) VALUES ('pride', '%s', '%s', '%s', '%s');" % (
            (int(ml)), (int(m[0][0]) - 1372), int(tr) * 10, int(k[0][0].split(',')[0])))

        mydb.commit()

    pass


scrape(300)
pride()
peju206()
l90()


# try:
#     main = WebDriverWait(els,5).until(EC.presence_of_element_located(By.CLASS_NAME,'kt-page-title__title kt-page-title__title--responsive-sized'))
# except:
#     driver.quit()

