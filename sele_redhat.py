from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

options = Options()
options.headless = False
driver = webdriver.Chrome(options=options, executable_path='chromedriver')
driver.get("https://catalog.redhat.com/software/containers/ubi8/ubi/5c359854d70cc534b3a3784e?gti-tabs=unauthenticated")
time.sleep(10)
print("Headless Chrome Initialized")
page = driver.page_source
driver.quit()
soup = BeautifulSoup(page, 'html.parser')
print(soup.find('div', {'id': 'root'}))
