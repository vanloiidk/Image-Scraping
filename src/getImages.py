from datetime import datetime
from selenium import webdriver
import time
import chromedriver_binary
import os
from urllib import request
def scrollDown(driver):
    SCROLL_PAUSE_TIME = 0.5
    scrollNum = 1000
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    print(last_height)
    num, last = divmod(last_height,scrollNum)
    for i in range(1,num+1):
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, {});".format(scrollNum*i))

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
    driver.execute_script("window.scrollTo(0, {});".format(last_height))


def getDatTime():
    now = datetime.now()
    dt_string = now.strftime("%Y%m%d_%H%M%S")
    return dt_string

def createDir(path = "./", name = getDatTime()):
    if path[-1]!="/":
        path+="/"
    path +=name
    os.mkdir(path)
    return path

if __name__=="__main__":

    dir = createDir()
    captionFile = open(dir+"/caption.txt","w+")
    inputUrl = str(input("Enter Link:").replace(" ","").replace("\n", ""))
    n = int(input("Enter number of pages:"))

    step = 0
    browser = webdriver.Chrome()

    for j in range(1,n+1):
        url ="{}?pagi={}".format(inputUrl,j)
        browser.get(url)
        scrollDown(browser)

        images = browser.find_elements_by_css_selector('div.item img')


        for i in range(len(images)):
            url = images[i].get_attribute('src')
            caption = images[i].get_attribute('alt')
            captionFile.write("hinh{}.jpg#0 {}\n".format(i+step,caption))
            print(url)
            if url is None:
                continue
            os.system("wget -O {0} {1}".format(dir+"/hinh{}.jpg".format(i+step), url))
        step+=len(images)

    browser.close()
    captionFile.close()