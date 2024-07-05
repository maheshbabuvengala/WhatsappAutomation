from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
# driver.maximize_window()
driver.start_session

phone_number = ['9381574024','9866810344','7702420478','6303060078','9182086295','7981663360','8498821093']
messages = 'Hello, this is a test message!'


def send_msg_to_phone_number(i,message):
    url = f'https://web.whatsapp.com/send?phone=+91{i}&text={message}'
    driver.get(url)

    time.sleep(10)
    wait = WebDriverWait(driver, 250) 
    send_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')))
    send_button.click()
    
j=1
for i in phone_number:
    
    time.sleep(10)

    message = messages+str(j)
    j+=1
    send_msg_to_phone_number(i, message)
    print(message,i)

driver.quit