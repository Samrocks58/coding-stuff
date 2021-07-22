import selenium, time, random, logging, urllib3, sys
from urllib3.connectionpool import log as other_logger
from selenium.webdriver.remote.remote_connection import LOGGER as selenium_logger
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.common.exceptions import NoSuchElementException
from playsound import playsound
cool_sound=r"non-program bulcrapo/Sweet_Sound.wav"

selenium_logger.setLevel(logging.WARNING)
other_logger.setLevel(logging.WARNING)
opts= EdgeOptions()
opts.use_chromium = True
opts.add_experimental_option("excludeSwitches", ["enable-logging"])
#opts.set_headless(True)
# opts.add_argument("user-data-dir=C:\\Path to chrome profile")
opts.set_headless(False)
meetingLink = input("Please Enter The Meeting Link: ")
playsound(cool_sound)
meetingCode = meetingLink.split("lookup/")[1][:10]


#browser = webdriver.Edge(executable_path=r'C:\Users\spear\OneDrive\Desktop\Better Newer Webdriver\msedgedriver')
browser = Edge(executable_path=r'C:\Users\spear\OneDrive\Desktop\Better Newer Webdriver\msedgedriver', options=opts)
browser.get(meetingLink)


def find_meeting_page():
    global meetingCode
    browser.refresh()
    # WebDriverWait(browser, 5).until(browser.find_element_by_xpath("/html/body/c-wiz/div/div[2]/div/div[1]/div[3]/div/div[1]/label/input"))
    try:
        Meeting_Page = browser.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div/span/span/div/div/svg")
        # if Meeting_Page is not None:
        for i in range(50):
            playsound(cool_sound)
            time.sleep(2)
    except NoSuchElementException:
        pass
    try:
        browser.find_element_by_xpath("/html/body/c-wiz/div/div[2]/div/div[1]/div[3]/div/div[1]/label/input").send_keys(meetingCode + Keys.RETURN)
        print("Finding meeting page...")
    except NoSuchElementException:
        find_meeting_page()
    time.sleep(3)
    try:
        Meeting_Page = browser.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div/span/span/div/div/svg")
        # if Meeting_Page is not None:
        for i in range(50):
            playsound(cool_sound)
            time.sleep(2)
    except NoSuchElementException:
        find_meeting_page()

#Science : https://meet.google.com/lookup/hfluzwhvoq?authuser=0&hs=179
#Health : https://meet.google.com/lookup/wnidztjsht
#Social Studies : https://meet.google.com/lookup/ayc7l3ml3z?authuser=1&hs=179
#English : https://meet.google.com/lookup/hvtpiqn3h2?authuser=1&hs=179
#Test Data: https://meet.google.com/lookup/zovrazhfri?pli=1&authuser=0
time.sleep(5)
#WebDriverWait(browser, 2).until()
try:
    # WebDriverWait(browser, 5).until(browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/div[3]/div/span").click())
    browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/div[3]/div/span").click()
except Exception as except2:
    line_num1 = sys.exc_info()[-1].tb_lineno
    print(f"Something is wrong!!! There is a {except2.__class__.__name__} at line {line_num1}!!!")
try:
    # WebDriverWait(browser, 5).until(browser.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div[2]/div/div/span/span"))
    time.sleep(15)
    browser.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div[2]/div/div/span/span").click()
    time.sleep(15)
    # WebDriverWait(browser, 5).until(browser.find_element_by_xpath("/html/body/header/div[1]/div/div[3]/div[1]/div/span[1]/a"))
    browser.find_element_by_xpath("/html/body/header/div[1]/div/div[3]/div[1]/div/span[1]/a").click()
    time.sleep(15)
    # WebDriverWait(browser, 5).until(browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"))
    browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys("spearce2024@k12.andoverma.us" + Keys.RETURN)
    time.sleep(15)
    # try:
    #     browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input").send_keys("spear5858" + Keys.RETURN)
    # except Exception:
    #     pass
    try:
        # WebDriverWait(browser, 2).until(browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/main/div/div/div/form/div[2]/div[1]/input"))
        browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/main/div/div/div/form/div[2]/div[1]/input").send_keys("spearce2024")
        browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/main/div/div/div/form/div[2]/div[2]/input").send_keys("bowl495DOZE" + Keys.RETURN)
    except NoSuchElementException:
        pass
    time.sleep(15)
    # WebDriverWait(browser, 2).until(browser.find_element_by_xpath(browser.find_element_by_xpath("/html/body/c-wiz/div/div[2]/div/div[1]/div[3]/div/div[1]/label/input")))
    browser.find_element_by_xpath("/html/body/c-wiz/div/div[2]/div/div[1]/div[3]/div/div[1]/label/input").send_keys(meetingCode + Keys.RETURN)
    time.sleep(3)

except Exception as except1:
    line_num2 = sys.exc_info()[-1].tb_lineno
    print(f"Something is wrong!!! There is a {except1.__class__.__name__} at line {line_num2}!!!")
if find_meeting_page():
    for repetion in range(999999999999):
        print("YAYYYYYY!!!!!!!!    You did it SAM!!!!")

browser.quit()
quit()

# pyinstaller --onefile -w --add-data "C:\Users\spear\AppData\Local\Programs\Python\Python36\Scripts\coins.png;." --add-data "Gibster-ow1XA.otf;." snake.py