# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys

# import time

# class EmailAttachmentDownload:
#     def __init__(self, email, password):
#         self.email = email
#         self.password = password
#         self.driver = None

#     def setup_driver(self):
#         options = webdriver.ChromeOptions()
#         options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2")
#         self.driver = webdriver.Chrome(options=options)

#     def login(self):
#         self.driver.get("https://www.microsoft.com/en-us/microsoft-365/outlook/log-in")
#         sign_in_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//html/body/div[3]/div/div[1]/div[1]/div/div/header/div/div/div[4]/div[2]/div/a/div")))
#         sign_in_button.click()

#         input_email = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]')))
#         input_email.send_keys(self.email)

#         button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div[3]/div/div/div/div[4]/div/div/div/div/input')))
#         button.click()

#         password_get = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input')))
#         password_get.send_keys(self.password)

#         password_login = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div/div[2]/div/div[5]/div/div/div/div/input')))
#         password_login.click()

#         WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/div/form/div[3]/div[2]/div/div[2]/button'))).click()        

#     def unread_mail_filter(self):
#         filter_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="txtSch"]')))
#         filter_input.send_keys("unread")
#         filter_input.send_keys(Keys.ENTER)
#         time.sleep(500000)
#         unread_messages = self.driver.find_elements(By.CLASS_NAME, "lvw")
#         count=-1
#         for message in unread_messages:
#             count+=1
#             if count==0:
#                 continue
#             else:
#                 try:
#                     message.click()
#                     attachment = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="spnAtmt"]')))
#                     attachment_name = attachment.text
#                     print(attachment_name)

#                     attachment.click()
#                 except EC.TimeoutException:
#                     print("Attachment not found")
#                 except Exception as e:
#                     print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     email = "mdshoaibhabibAI@outlook.com"
#     password = "farhatfalak@123"
#     obj = EmailAttachmentDownload(email, password)
#     obj.setup_driver()
#     obj.login()
#     obj.unread_mail_filter()



# # from selenium import webdriver
# # import time
# # from selenium.webdriver.firefox.service import Service
# # from webdriver_manager.chrome import ChromeDriverManager
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as ec
# # from selenium.webdriver.common.by import By


# # class Email_Attachment_Download:

# #     def __init__(self,email,password):
# #         self.email=email
# #         self.password=password

# #         self.options = webdriver.ChromeOptions()
# #         self.options.add_argument("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2")
# #         self.driver = webdriver.Chrome(options=self.options)
# #     # Initialize a Chrome web browser
# #     # driver = webdriver.Chrome()

# #     # Open Google
# #     def mail_page(self):
# #         self.driver.get("https://www.microsoft.com/en-us/microsoft-365/outlook/log-in")

# #         self.sign_in=self.driver.find_element("xpath","//html/body/div[3]/div/div[1]/div[1]/div/div/header/div/div/div[4]/div[2]/div/a/div")
# #         self.sign_in.click()
# #         time.sleep(5)
# # #====================================insert email working==========================================
# #     def mail_login(self):
# #         input_email=self.driver.find_element("xpath","""/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]""")
# #         input_email.click()
# #         input_email.send_keys(self.email)
# #         time.sleep(5)

# # #==============================submit Email========================================================
# #         button=self.driver.find_element("xpath","""/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div[3]/div/div/div/div[4]/div/div/div/div/input""")
# #         button.click()
# #         time.sleep(5)

# # #=============================Insert Password and submit===========================================
# #         password_get=self.driver.find_element("xpath","""/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input""")
# #         password_get.click()
# #         password_get.send_keys(self.password)
# #         time.sleep(5)
# #         password_login=self.driver.find_element("xpath","""/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div/div[2]/div/div[5]/div/div/div/div/input""")
# #         password_login.click()

# #         time.sleep(15)
# # #=========================Aggrement Accept Button===================================================
# #         term_and_condition=self.driver.find_element("xpath", """/html/body/div[1]/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/div/form/div[3]/div[2]/div/div[2]/button""")
# #         term_and_condition.click()
# #         time.sleep(25)

# # #===============unread mail data and extract========================================================

# #     def unread_mail_filter(self):
# #         filter_button=self.driver.find_element(By.CSS_SELECTOR,"#mailListFilterMenu > span > i")
# #         time.sleep(3)
# #         filter_button.click()
# #         time.sleep(5)
# #         filter_button_click=self.driver.find_element(By.CSS_SELECTOR, "body > div.___1uxlrft.f1euv43f.f15twtuk.f1vgc2s3.f1e31b4d.f494woh > div > div > div:nth-child(3) > span.fui-MenuItem__icon.r9c34qo.fui-MenuItemRadio__icon > i")
# #         time.sleep(2)
# #         filter_button_click.click()
# #         time.sleep(10)

# #         unread_msg_read_onebyone=self.driver.find_elements(By.CLASS_NAME,"EeHm8")
# #         count=-1
# #         for message in unread_msg_read_onebyone:
# #             count+=1
# #             if count==0:
# #                 continue
# #             else:
# #                 try:
# #                     message.click()
# #                     time.sleep(10)

# #                     attachment_name_extract=self.driver.find_element(By.XPATH, """//*[@id="ConversationReadingPaneContainer"]/div/div/div[3]/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div/div[1]/div/div/div[1]""")

# #                     print(attachment_name_extract.text)

# #                     time.sleep(10)

# #                     # attachment_download_button=driver.find_element(By.CSS_SELECTOR, "#ConversationReadingPaneContainer > div > div > div:nth-child(3) > div.aVla3 > div > div > div > div > div.l8Tnu.T3idP > div > div > div > div > div > div > div.o4euS > button > span")
# #                     # attachment_download_button.click()
# #                     # time.sleep(5)

# #                     # attachment_download=driver.find_element(By.CSS_SELECTOR,"#fluent-default-layer-host > div:nth-child(4) > div > div > div > div > div > div > ul > li:nth-child(5) > button > div > i")
# #                     # attachment_download.click()
# #                     # time.sleep(7)
# #                     # print("successfully found")

# #                 except:
# #                     print("not found")

# # if __name__=="__main__":
# #     email="mdshoaibhabibAI@outlook.com"
# #     password="farthatfalak2@123"
# #     obj=Email_Attachment_Download(email,password)
# #     obj.mail_page()
# #     obj.mail_login()
# #     obj.unread_mail_filter()








# from selenium import webdriver
# import time
# from selenium.webdriver.firefox.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.common.by import By


# options = webdriver.ChromeOptions()
# options.add_argument("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2")
# driver = webdriver.Chrome(options=options)
# # Initialize a Chrome web browser
# # driver = webdriver.Chrome()

# # Open Google
# driver.get("https://www.microsoft.com/en-us/microsoft-365/outlook/log-in")

# sign_in=driver.find_element("xpath","//html/body/div[3]/div/div[1]/div[1]/div/div/header/div/div/div[4]/div[2]/div/a/div")
# sign_in.click()
# time.sleep(5)
# #=========================================insert email working==========================================
# input_email=driver.find_element("xpath","""/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]""")
# input_email.click()
# input_email.send_keys(f"mdshoaibhabibAI@outlook.com")
# time.sleep(5)

# #===================================submit Email========================================================
# button=driver.find_element("xpath","""/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div[3]/div/div/div/div[4]/div/div/div/div/input""")
# button.click()
# time.sleep(5)

# #==================================Insert Password and submit===========================================
# password_get=driver.find_element("xpath","""/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input""")
# password_get.click()
# password_get.send_keys(",,,,,")
# time.sleep(5)
# password_login=driver.find_element("xpath","""/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div/div[2]/div/div[5]/div/div/div/div/input""")
# password_login.click()

# time.sleep(5)
# #==============================Aggrement Accept Button===================================================
# term_and_condition=driver.find_element("xpath", """/html/body/div[1]/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/div/form/div[3]/div[2]/div/div[2]/button""")
# term_and_condition.click()
# time.sleep(20)

# #=====================read mail data and extract========================================================
# # full_inbox=driver.find_element("xpath", """/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div""")
# # time.sleep(5)
# # read_msg_onebyone=full_inbox.find_elements(By.CLASS_NAME, "EeHm8")
# # inbox_msg_Length=len(read_msg_onebyone)

# # count=-1

# # for msgs in read_msg_onebyone:
# #     count+=1
# #     if count==0:
# #         continue
# #     else:
# #         msgs.click()
# #         time.sleep(15)
# #         try:
# #             all_attachment=driver.find_elements(By.CLASS_NAME,"o4euS")
# #             for attachment in all_attachment:
# #                 attachment_arrow=driver.find_element(By.CSS_SELECTOR,"#ConversationReadingPaneContainer > div > div > div:nth-child(3) > div.aVla3 > div > div > div > div > div.l8Tnu.T3idP > div > div > div > div > div > div > div.o4euS > button > span")
# #                 attachment_arrow.click()
# #                 time.sleep(10)
# #                 download_button=driver.find_element(By.CSS_SELECTOR,"#fluent-default-layer-host > div:nth-child(4) > div > div > div > div > div > div > ul > li:nth-child(3) > button > div > i")
# #                 download_button.click()
# #                 time.sleep(10)
# #         except Exception as e:
# #             print("An error occurred:", e)

# #=====================Download all attachment========================================================
# full_inbox=driver.find_element("xpath", """/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div""")
# time.sleep(5)
# read_msg_onebyone=full_inbox.find_element("xpath","""/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div""")
# read_msg_onebyone.click()
# time.sleep(15)
# # data=driver.find_element("xpath","""/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[3]/div/div/div[3]/div/div/div/div/div/div/div/div[3]/div[1]/div/div/div/div/div[2]""")
# # time.sleep(5)
# download_btton=driver.find_elements(By.CLASS_NAME,"o4euS")
# time.sleep(5)
# for button in download_btton:
#     try:
#         button.click()
#         # print(button.get_attribute("innerHTML"))
#         time.sleep(7)
#         download_attachments=driver.find_element("xpath","""/html/body/div[2]/div[4]/div/div/div/div/div/div/ul/li[5]/button/div """)
#         #     print("Downlaod attachment--->",download_attachments)
#         # print("===============================================================")
#         download_attachments.click()
#         time.sleep(7)
#     except:
#         print("Not found")
# # print("Successfull")
# # # time.sleep(5)
# # # for button in download_btton:
# # #     button.click()
# # #     time.sleep(5)
# # #     download_attachments=driver.find_element(By.CSS_SELECTOR,"#fluent-default-layer-host > div:nth-child(4) > div > div > div > div > div > div > ul > li:nth-child(3) > button > div > span")
# # #     time.sleep(5)



# #             # o4euS img
# #             # o4euS img
# #             #o4euS pdf

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class OutlookAttachmentDownloader:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.driver = None

    def setup_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2")
        self.driver = webdriver.Chrome(options=options)

    def login(self):
        self.driver.get("https://www.microsoft.com/en-us/microsoft-365/outlook/log-in")

        sign_in_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//html/body/div[3]/div/div[1]/div[1]/div/div/header/div/div/div[4]/div[2]/div/a/div")))
        sign_in_button.click()

        input_email = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="loginfmt"]')))
        input_email.send_keys(self.email)

        next_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@value="Next"]')))
        next_button.click()

        input_password = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="passwd"]')))
        input_password.send_keys(self.password)

        sign_in_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@value="Sign in"]')))
        sign_in_button.click()
        time.sleep(5000)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Accept"]'))).click()

    def download_attachments(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.o365cs-nav-branding'))).click()  # Navigate to Inbox
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[text()="Attachments"]'))).click()  # Navigate to Attachments tab

        attachments = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//button[@aria-label="Download"]')))
        
        for attachment in attachments:
            try:
                attachment.click()
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Download"]'))).click()
            except Exception as e:
                print(f"Failed to download attachment: {e}")

    def close_driver(self):
        self.driver.quit()

if __name__ == "__main__":
    email = "mdshoaibhabibAI@outlook.com"
    password = "farhatfalak@123"
    downloader = OutlookAttachmentDownloader(email, password)
    downloader.setup_driver()
    downloader.login()
    downloader.download_attachments()
    downloader.close_driver()
