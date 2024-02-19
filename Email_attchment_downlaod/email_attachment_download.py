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
password_get.send_keys("farhatfalak@123")
time.sleep(5)
password_login=driver.find_element("xpath","""/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div/div[2]/div/div[5]/div/div/div/div/input""")
password_login.click()

time.sleep(15)
#==============================Aggrement Accept Button===================================================
term_and_condition=driver.find_element("xpath", """/html/body/div[1]/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/div/form/div[3]/div[2]/div/div[2]/button""")
term_and_condition.click()
time.sleep(20)


#=====================read mail data and extract========================================================
full_inbox=driver.find_element("xpath", """/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div""")
time.sleep(5)
read_msg_onebyone=full_inbox.find_elements(By.CLASS_NAME, "EeHm8")
inbox_msg_Length=len(read_msg_onebyone)

count=-1

for msgs in read_msg_onebyone:
    count+=1
    if count==0:
        continue
    else:
        msgs.click()
        time.sleep(60)
        try:
            attachment_arrow=driver.find_element(By.CSS_SELECTOR,"#ConversationReadingPaneContainer > div > div > div:nth-child(3) > div.aVla3 > div > div > div > div > div.l8Tnu.T3idP > div > div > div > div > div > div > div.o4euS > button > span")
            attachment_arrow.click()
            time.sleep(10)
            download_button=driver.find_element(By.CSS_SELECTOR,"#fluent-default-layer-host > div:nth-child(4) > div > div > div > div > div > div > ul > li:nth-child(3) > button > div > i")
            download_button.click()
            time.sleep(10)
        except Exception as e:
            print("An error occurred:", e)