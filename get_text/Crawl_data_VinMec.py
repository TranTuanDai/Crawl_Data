from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

pd.set_option('display.max_columns',40)
options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
options.add_argument("--disable-gpu")

driver = webdriver.Chrome()
service = Service('/ChromeDriver/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=service,options=options)

columns_name=['Tên dược chất','Dạng bào chế - biệt dược','Nhóm thuốc-Tác dụng','Chỉ định','Chống chỉ định','Thận trọng','Liều và cách dùng','Phụ nữ có thai','Phụ nữ cho con bú','Tài liệu tham khảo']
p_values=[]

for page in range(1):
    url = f'https://www.vinmec.com/vi/thuoc/?page={page}'
    driver.get(url)
    time.sleep(5)
    div_content=driver.find_element(By.CLASS_NAME,'content')
    tags=driver.find_element(By.TAG_NAME,'section')
    ul_tags=tags.find_element(By.TAG_NAME,'ul')
    li_tags=ul_tags.find_elements(By.TAG_NAME,'li')
    for i in range(1,len(li_tags)+1):
    

        items = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/section/ul/li[{}]'.format(i)).click()
        time.sleep(3)

        main=driver.find_element(By.XPATH,'/html/body/div[2]')
        h1=main.find_element(By.TAG_NAME,'h1').text
        p_values.append(h1)

        drug_body=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div[2]')
        p_tags=drug_body.find_elements(By.TAG_NAME,'p')
        

        for i in range(len(p_tags)):
            p_values.append(p_tags[i].text)
            print(p_values)
            
        time.sleep(3)
        driver.back()
