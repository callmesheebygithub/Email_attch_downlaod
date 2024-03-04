from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from excel_sheet_title_format import title_list
import time


download_directory = "/home/muhammadshoaib/Desktop/Arcano_working"

# Set up Chrome options to disable prompting for download location
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_directory,
    "download.prompt_for_download": False,  # Disable prompting for download location
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})
# Provide the path to your Chrome webdriver
# webdriver_service = Service('/path/to/chromedriver')

# Initialize the Chrome browser with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the webpage where you want to download the file
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-xls-download/")

# Locate and click the download button
download_button = driver.find_element(By.XPATH, """//*[@id="table-files"]/tbody/tr[1]/td[5]/a""")
time.sleep(2)
download_button.click()
time.sleep(50)
print("successfully click")

text="JAZZ_AC_PO"
text1="JAZZ_CO_PO"
text2="JAZZ_HS_PO"
text3="JAZZ_SC_PO"
text4="JAZZ_SIM_PO"
if text in download_button:
    download_directory = "/home/muhammadshoaib/Desktop/Arcano_working/JAZZ_AC_PO"

# Set up Chrome options to disable prompting for download location
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_directory,
        "download.prompt_for_download": False,  # Disable prompting for download location
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

elif text1 in download_button:
    download_directory = "/home/muhammadshoaib/Desktop/Arcano_working/JAZZ_CON_PO"

# Set up Chrome options to disable prompting for download location
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_directory,
        "download.prompt_for_download": False,  # Disable prompting for download location
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
elif text2 in download_button:
    download_directory = "/home/muhammadshoaib/Desktop/Arcano_working/JAZZ_HS_PO"

# Set up Chrome options to disable prompting for download location
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_directory,
        "download.prompt_for_download": False,  # Disable prompting for download location
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

elif text3 in download_button:
    download_directory = "/home/muhammadshoaib/Desktop/Arcano_working/JAZZ_SC_PO"

# Set up Chrome options to disable prompting for download location
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_directory,
        "download.prompt_for_download": False,  # Disable prompting for download location
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

else:
    download_directory = "/home/muhammadshoaib/Desktop/Arcano_working/JAZZ_SIM_PO"

# Set up Chrome options to disable prompting for download location
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_directory,
        "download.prompt_for_download": False,  # Disable prompting for download location
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })