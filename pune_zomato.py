from ast import IsNot
from unicodedata import name
from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import google_sheet_api

from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get("https://www.zomato.com/pune")
time.sleep(5)
driver.maximize_window()
time.sleep(6)




# s = Service("/home/zec/Downloads/chromedriver")
# driver = webdriver.Chrome(service=s)

# driver.get("https://www.zomato.com/pune")
# time.sleep(5)
# driver.maximize_window()
# time.sleep(6)


links_list = []




main_link_list = []
def get_links():

    # for i in range(30):

    #     driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    #     time.sleep(10)

    #     print(i)

    

    #     if(i==5 or i==10 or i==15 or i==20 or i==25):
    #         driver.execute_script('scrollTo(0,700)')
    #         time.sleep(5)


    time.sleep(5)
    driver.execute_script('scrollTo(0,700)')
    
    time.sleep(8)
    links = driver.find_elements(By.CLASS_NAME,'jumbo-tracker a')
    print(len(links))
   
    for i in links:
        link = i.get_attribute("href")
        links_list.append(link)
    
        print(link)
    print(len(links_list))

    sub='https://www.zomato.com/pune/restaurants?'
    for k in links_list:
        if sub in k:
            continue
        elif k not in main_link_list:
            main_link_list.append(k)
    print(len(main_link_list))
    print("Get link")
    click()

 

def Data():

    try:
        name = driver.find_element(By.CLASS_NAME,'sc-7kepeu-0.sc-eilVRo.eAhpQG').text
        # Names.append(name.text)
        print("Name => ",name)
    except:
        # Names.append("None")
        name = None

    try:
        address = driver.find_element(By.CLASS_NAME,'sc-cpmLhU.fDVcNc').text
        print("Address name => ",address)
        # Address_names.append(address.text)
    except:
        # Address_names.append("None")
        address = None

    # try:
    #     addlink = address.get_attribute('href')
    #     # Address_links.append(addlink)
    #     print("Address link = > ",addlink)
    # except:
    #     # Address_links.append("None")
    #     addlink = None

    try:
        times = driver.find_element(By.CLASS_NAME,'sc-fhYwyz.fRKkxr').text
        time1 = times.split('(')
        print("Time => ",time1[0])
        time2 = time1[0]
        # Times.append(time1[0])
    except:
        # Times.append("None")
        time2 = None

    try:
        dining_reviews = driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/section[3]/section/section/div/div/div/section/div[1]/div[1]/div/div/div[1]').text
        # Dining_Reviews.append(dining_reviews)
        print("dining_reviews => ",dining_reviews)
    except:
        # Dining_Reviews.append("None")
        dining_reviews = None


    try:
        delivery_reviews = driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/section[3]/section/section/div/div/div/section/div[3]/div[1]/div/div/div[1]').text
        # Delivery_Reviews.append(delivery_reviews)
        print("delivery_reviews => ",delivery_reviews)
    except:
        # Delivery_Reviews.append("None")
        delivery_reviews = None



    driver.execute_script('scrollTo(0,1000)')
    time.sleep(5)
    m=[]
    D_Name = []
    divs = driver.find_elements(By.CLASS_NAME,'sc-1s0saks-17.bGrnCu')
    for div in divs:
        Down_list = []
        try:
            Dname = div.find_element(By.CLASS_NAME,'sc-1s0saks-15.iSmBPS').text
            Down_list.append(Dname)
            print("Dname => ",Dname)
        except:
            Dname = None
            Down_list.append(Dname)

        try:
            Dvotes = div.find_element(By.CLASS_NAME,'sc-z30xqq-4.hTgtKb').text
            Down_list.append(Dvotes)
            print("votes => ",Dvotes)
        except:
            Dvotes = None
            Down_list.append(Dvotes)

        try:
            Dprice = div.find_element(By.CLASS_NAME,'sc-17hyc2s-1.cCiQWA').text
            Down_list.append(Dprice)
            print("Dprice => ",Dprice)
        except:
            Dprice = None
            Down_list.append(Dprice)

        try:
            Ddiscrib = div.find_element(By.CLASS_NAME,'sc-1s0saks-12.hcROsL').text
            Down_list.append(Ddiscrib)
            print("Ddiscrib => ",Ddiscrib)
        except:
            Ddiscrib = None
            Down_list.append(Ddiscrib)
        D_Name.append(Down_list)


    for i, n in enumerate(D_Name):
        if n not in m:
            m.append(n)

    f_D_data = []

    f_D_data.append(m)
    print(len(m))
    print(len(D_Name))  
    # print(m)  
    value1 = [name, address, time2, dining_reviews, delivery_reviews, str(f_D_data)]
    google_sheet_api.append_googlesheet1(value1)



    


def click():

    for i in main_link_list:
        driver.get(i)
        time.sleep(5)
       
    
        Data()
   


get_links()




driver.close()







