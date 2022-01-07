from webdrivers.path import path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
import time

'''
For deployment on heroku.app
# chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--no-sandbox")
# driver = webdriver.Chrome(service=Service(os.environ.get("CHROMEDRIVER_PATH")), options=chrome_options)
'''

"""
Allows Chrome to download pdf files on headless mode
"""
def enable_download_headless(browser, download_dir: str):
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--verbose")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-software-rasterizer')
chrome_options.add_argument("--disable-notifications")
PDF_PATH = f"{os.getcwd()}"
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": "C:\\Users\\brend\\wsl\\Emoji", #Change default directory for downloads
    "download.prompt_for_download": False, #To auto download the file
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True, #It will not show PDF directly in chrome
    "safebrowsing_for_trusted_sources_enabled": False,
    "safebrowsing.enabled": False
})
print(f"{os.getcwd()}")

def scihub(doi: str):
    try:
        PATH = str(path) + "/chromedriver.exe"
        service = Service(PATH)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        enable_download_headless(driver, "C:\\Users\\brend\\wsl\\Emoji")
        driver.get(f"https://sci.bban.top/pdf/{doi}.pdf")
        time.sleep(3)
        driver.quit()
        return True
    except Exception as e:
        print(e)
        return False

# print(scihub("10.1145/1721654.1721659"))