from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import numpy as np
import time

options = Options()

# options.add_argument('--headless')
options.add_argument("--no-sandbox")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-browser-side-navigation")
options.add_argument("--disable-gpu")
options.add_argument('--incognito')
options.add_argument("start-maximized")
options.add_argument("enable-automation")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

filepath = input('Save file to: ') + '/'

url_list = ['https://www.healthhub.sg/directory/clinics-and-polyclinics',
            'https://www.healthhub.sg/directory/hospitals',
            'https://www.healthhub.sg/directory/retail-pharmacies',
            'https://www.healthhub.sg/directory/nursing-homes']

for i in url_list:

    driver.get(i)

    filename = i[i.find('directory/'):].replace('directory/','')

    time.sleep(3)

    number_of_pages = int(driver.find_elements_by_xpath('//ul[@class="pagination"]/li')[-5].text)
    page_counter = 1

    name_list = []
    address_list = []
    postal_list = []

    while page_counter <= number_of_pages:

        temp_list_name = [x.text[:x.text.find('\n')] for x in driver.find_elements_by_xpath('//span[@class="app_ment"]')]
        name_list = name_list + temp_list_name

        temp_list_add = [x.text for x in driver.find_elements_by_xpath('//span[@class="add_sign"]')]
        address_list = address_list + temp_list_add

        temp_list_postal = [x[-6:] for x in temp_list_add]
        postal_list = postal_list + temp_list_postal

        driver.find_elements_by_xpath('//ul[@class="pagination"]/li/a')[-4].click()
        page_counter += 1
        time.sleep(2)

    temp_df = pd.DataFrame(data=list(zip(name_list, address_list, postal_list)), columns=['name', 'address', 'postal'])
    temp_df['postal'] = temp_df['postal'].astype(str)
    temp_df.to_csv('{0}{1}.csv'.format(filepath,filename), index=False)

driver.quit()
