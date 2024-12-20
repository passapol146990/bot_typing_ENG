from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import bs4

url = 'https://www.typingstudy.com/th-thai_kedmanee-3/lesson/1'
drive = webdriver.Edge()
drive.get(url)

def brToEnter(drive):
    while True:
        try:
            br = drive.find_element(By.TAG_NAME,'br')
            drive.execute_script("""
                var element = arguments[0];
                var newTextNode = document.createTextNode(arguments[1]);
                element.parentNode.replaceChild(newTextNode, element);
            """, br, '↵')
        except:
            break


def autoWrite(wpm):
    while True:
        brToEnter(drive)
        data = drive.page_source # เข้าถึง html
        soup = bs4.BeautifulSoup(data)
        try:
            selected_element = soup.select_one("html>body>div>div:nth-of-type(3)>div:nth-of-type(2)>div:nth-of-type(2)")
            text = selected_element.get_text()+' '

            if selected_element:
                if '↵' not in text:
                    for i in text:
                        time.sleep(wpm)
                        drive.find_element(By.XPATH,'//*[@id="type"]').send_keys(i)
                else:
                    for i in text:
                        time.sleep(wpm)
                        if i == '↵':
                            drive.find_element(By.XPATH,'//*[@id="type"]').send_keys(Keys.ENTER)
                        else:
                            drive.find_element(By.XPATH,'//*[@id="type"]').send_keys(i)
        except:
            break
    print('success')









