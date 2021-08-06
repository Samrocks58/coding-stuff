import selenium, time, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options


options=Options()
# options.add_argument('--log-level=3')
print(options)
browser = webdriver.Edge(executable_path=r'C:\Users\spear\OneDrive\Desktop\Desktop Folder\Web Driver\msedgedriver')
browser.get("https://discord.com/login/")
# browser.get('https://www.walmart.com/')
# email_xpath="/html/body/div/div/div[2]/form/div/input"
# password_xpath="/html/body/div[1]/div/div[2]/form[1]/div[2]/input[1]"
# Walmart_xpath="/html/body/div/div[1]/div/header/div/a[1]"
#Original Password XPath: "/html/body/div/div/div[2]/form/div[1]/input[1]"
#/html/body/div[1]/div/div[2]/form[1]/div[1]

"""" java=browser.find_element_by_class_name("js-content")
sign_in=java.find_element_by_id("sign-in-widget")
sign_in2=sign_in.find_element_by_class_name("sign-in-widget")
form=sign_in2#.find_element_by_class_name("form-box")
email=sign_in2.find_element_by_class_name("form-field required error")
password=sign_in2.find_element_by_class_name("form-field required undefined password-field error")"""
# while True:
    # time.sleep(1)
# time.sleep(random.randint(3, 8))
# Account=browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/section/div[2]/div/div[3]/div[2]/div/div[2]/div[1]/button")
# Account.click()
# Sign_in=browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/section/div[3]/div[2]/div/div/div[2]/div/a[1]/div/span").click()
# time.sleep(random.randint(3, 8))
# email_signIn=browser.find_element_by_xpath(email_xpath).send_keys("")
# time.sleep(random.randint(3, 5))
# password_signIn=browser.find_element_by_xpath(password_xpath).send_keys("" + Keys.RETURN)
# time.sleep(random.randint(3, 8))
# Search_Bar=browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/section/div[2]/div/div[3]/div[2]/div/form/input[2]").send_keys("clock" + Keys.RETURN)
# time.sleep(random.randint(3, 8))
discord=[]
time.sleep(5)
# while True:
    # message=input("What do you want to text? ")
    # if message == "quit":
        # break
    # else:
        # discord.append(message)
time.sleep(2)
# browser.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/div[2]/input").send_keys("")
# browser.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input").send_keys("" + Keys.RETURN)
time.sleep(15)
browser.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/div/div/div[1]/nav/div[2]/div/a[3]/div/div[2]/div[1]/div/div").click()
time.sleep(20)
while True:
    text_bar = browser.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/main/form/div/div/div/div[3]/div[2]/div")
    #text_bar.send_keys(""+Keys.RETURN)
    time.sleep(1)
time.sleep(999999)
browser.quit()