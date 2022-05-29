from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
import webbrowser

#Info:
#CS Courses Button by selector: body > form > table > tbody > tr:nth-child(4) > td:nth-child(3) > select
#CS Courses Button by XPath: /html/body/form/table/tbody/tr[4]/td[3]/select 
# /html/body/form/p[2]/input[1]
def crawl():

    driver = webdriver.Chrome(ChromeDriverManager().install())
    wait = WebDriverWait(driver, 10)
    driver.set_page_load_timeout(10)

    try:
        driver.get("https://www.reg.uci.edu/perl/WebSoc")
    except TimeoutError:
        driver.execute_script("window.stop();")
    
    DeptButtonID = driver.find_element_by_name('Dept') 
    button = Select(DeptButtonID)

    button.select_by_value("COMPSCI")

    
    webDisplayButton = driver.find_element_by_name("Submit")
    webDisplayButton.click()
    
    print(driver.page_source.encode("utf-8"))
    driver.quit()
    return 0
    
def scrape():
    

def main():
    pass

if __name__ == '__main__':
    scrp = crawl()
    # print(scrp)

    main()