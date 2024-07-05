from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient

client = MongoClient('mongodb+srv://satyakarthikvelivela:firescrim123@firescrim.wxzexrz.mongodb.net/')
db = client['registration']
collection = db['duopayments']


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.start_session


# phone_number = ['9381770156','6303060078','9390119720']
phone_numbers = [doc['phoneno'] for doc in collection.find({}, {'phoneno': 1, '_id': 0}) if 'phoneno' in doc]
messages = 'Hello, this is a test message!'


def send_msg_to_phone_number(i,message):
    url = f'https://web.whatsapp.com/send?phone=+91{i}&text={message}'
    driver.get(url)

    time.sleep(3)
    wait = WebDriverWait(driver, 200) 
    send_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')))
    send_button.click()
    
j=1
for i in phone_numbers:
    
    time.sleep(2)

    message = messages+str(j)
    j+=1
    send_msg_to_phone_number(i, message)
    print(message,i)

time.sleep(10)
driver.quit