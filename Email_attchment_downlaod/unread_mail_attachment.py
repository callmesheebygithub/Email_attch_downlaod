from selenium import webdriver
import time
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2")
driver = webdriver.Chrome(options=options)
# Initialize a Chrome web browser
# driver = webdriver.Chrome()

# Open Google
driver.get("https://www.microsoft.com/en-us/microsoft-365/outlook/log-in")

sign_in=driver.find_element("xpath","//html/body/div[3]/div/div[1]/div[1]/div/div/header/div/div/div[4]/div[2]/div/a/div")
sign_in.click()
time.sleep(5)
#=========================================insert email working==========================================
input_email=driver.find_element("xpath","""/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]""")
input_email.click()
input_email.send_keys(f"mdshoaibhabibAI@outlook.com")
time.sleep(5)

#===================================submit Email========================================================
button=driver.find_element("xpath","""/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div[3]/div/div/div/div[4]/div/div/div/div/input""")
button.click()
time.sleep(5)

#==================================Insert Password and submit===========================================
password_get=driver.find_element("xpath","""/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input""")
password_get.click()
password_get.send_keys("")
time.sleep(5)
password_login=driver.find_element("xpath","""/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div/div[2]/div/div[5]/div/div/div/div/input""")
password_login.click()

time.sleep(15)
#==============================Aggrement Accept Button===================================================
term_and_condition=driver.find_element("xpath", """/html/body/div[1]/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/div/form/div[3]/div[2]/div/div[2]/button""")
term_and_condition.click()
time.sleep(25)

#===================unread mail data and extract========================================================
filter_button=driver.find_element(By.CSS_SELECTOR,"#mailListFilterMenu > span > i")
time.sleep(3)
filter_button.click()
time.sleep(5)
filter_button_click=driver.find_element(By.CSS_SELECTOR, "body > div.___1uxlrft.f1euv43f.f15twtuk.f1vgc2s3.f1e31b4d.f494woh > div > div > div:nth-child(3) > span.fui-MenuItem__icon.r9c34qo.fui-MenuItemRadio__icon > i")
time.sleep(2)
filter_button_click.click()
time.sleep(10)

unread_msg_read_onebyone=driver.find_elements(By.CLASS_NAME,"EeHm8")
count=-1
for message in unread_msg_read_onebyone:
    count+=1
    if count==0:
        continue
    else:
        try:
            message.click()
            time.sleep(10)

            attachment_name_extract=driver.find_element(By.XPATH, """//*[@id="ConversationReadingPaneContainer"]/div/div/div[3]/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div/div[1]/div/div/div[1]""")

            print(attachment_name_extract.text)

            time.sleep(10)

            # attachment_download_button=driver.find_element(By.CSS_SELECTOR, "#ConversationReadingPaneContainer > div > div > div:nth-child(3) > div.aVla3 > div > div > div > div > div.l8Tnu.T3idP > div > div > div > div > div > div > div.o4euS > button > span")
            # attachment_download_button.click()
            # time.sleep(5)

            # attachment_download=driver.find_element(By.CSS_SELECTOR,"#fluent-default-layer-host > div:nth-child(4) > div > div > div > div > div > div > ul > li:nth-child(5) > button > div > i")
            # attachment_download.click()
            # time.sleep(7)
            # print("successfully found")

        except:
            print("not found")

