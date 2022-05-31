from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from nltk.tokenize import word_tokenize
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen
import webbrowser

#Info:
#CS Courses Button by selector: body > form > table > tbody > tr:nth-child(4) > td:nth-child(3) > select
#CS Courses Button by XPath: /html/body/form/table/tbody/tr[4]/td[3]/select 
# /html/body/form/p[2]/input[1]
def crawl(driver):

    # driver = webdriver.Chrome(ChromeDriverManager().install())
    wait = WebDriverWait(driver, 10)
    driver.set_page_load_timeout(10)

    try:
        driver.get("https://www.reg.uci.edu/perl/WebSoc")
    except TimeoutError:
        driver.execute_script("window.stop();")
    
    # DeptButtonID = driver.find_element_by_name('Dept') 
    DeptButtonID = driver.find_element(by=By.NAME, value="Dept")
    button = Select(DeptButtonID)

    button.select_by_value("COMPSCI")

    
    # webDisplayButton = driver.find_element_by_name("Submit")
    webDisplayButton = driver.find_element(by=By.NAME, value="Submit")
    webDisplayButton.click()
    
    # print(driver.page_source.encode("utf-8"))
    return driver
    
def scrape(driver):
    soup = BeautifulSoup(driver.page_source, "lxml")

    courseTitles = []
    data = []
    CourseScraper = soup.find_all("td", class_ = "CourseTitle")

    for title in CourseScraper:
        course = title.get_text()
        course = course.replace(u'\xa0', u'').replace(u'\n', u'').replace(u'\t', u'')
        course = course.replace(u'(Prerequisites)', u'').strip()
        courseTitles.append(course)

    dataScraper = soup.find("div", class_= "course-list")
    # rows = dataScraper.findChildren("th").get_text().replace(u'<th title=', u'')
    rows = dataScraper.findChildren("th")

    # for item in rows:
    #     data.append(cleanTags(item))

    cleanedString = cleanTags(driver.page_source)
    classes = cleanedString[cleanedString.index('CompSci \xa0'):cleanedString.index('Total Classes Displayed')]
    classes = classes.replace(u"\xa0", u"").replace(u"Prerequisites", u"").replace(u"(  )", u"")
    classes = classes.split("CompSci")
    return classes

def cleanTags(html):
    soup = BeautifulSoup(html, "html.parser")
    
    for data in soup(['style', 'script', 'title']):
        data.decompose()
    return ' '.join(soup.stripped_strings)

def parse(info):
    cols = 17
    skip = 0
    for item in info:
        if skip == 0:
            skip += 1
            continue


def test(driver):
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    tables = pd.read_html(driver.page_source)
    print('Tables found:', len(tables))
    
    df1 = tables[1]  # Save first table in variable df1\
    df1 = df1.drop(df1.index[range(6)])
    df1.to_csv("testoutput.csv", sep='\t')

    print('First Table')
    print(df1)


def main():
    pass

if __name__ == '__main__':
    driver = webdriver.Chrome(ChromeDriverManager().install())
    crwl = crawl(driver)
    # scrp = scrape(crwl)
    tst = test(crwl)
    driver.quit()

    # print(scrp)

    main()