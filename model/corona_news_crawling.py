from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os

def corona_news():
    news = []
    try:
        driver_path = f'{os.path.join(os.path.dirname(__file__), "chromedriver.exe")}'
        service = Service(executable_path=driver_path)
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(service=service, options=options)
        driver.get('https://mediahub.seoul.go.kr/corona19/news/keywordNewsList.do')
        elements_ec = EC.presence_of_all_elements_located((By.XPATH,'//*[@id="news_List"]/ul/li/a'))
        elements = WebDriverWait(driver=driver, timeout=3).until(elements_ec)
        for element in elements:
            link = element.get_attribute('href')
            img = element.find_element(By.XPATH,'div[1]/img').get_attribute('src')
            text = element.text.split('\n')
            title = text[0]
            content = text[1]
            date = text[2]
            news.append([link,img,title,content,date])
        news_df = pd.DataFrame(news,columns=['link','img','title','content','date'])
        news_df.to_csv('corona19.csv', index=False, encoding='cp949')

    except TimeoutException as e:
        print(e)
    return news

if __name__ =='__main__':
    corona_news()
