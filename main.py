from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from time import sleep

URL = "https://tinder.com/"
GOOGLE_ID = ""
GOOGLE_PW = ""

chromedriver_path = "c:/development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get(URL)

sleep(2)
sign_in = driver.find_element_by_xpath('//*[@id="t-1890905246"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
sign_in.click()

sleep(5)
google_login = driver.find_element_by_xpath('//*[@id="t--149300558"]/div/div/div[1]/div/div[3]/span/div[1]/div/button')
google_login.click()

#새 창을 선택한다. window_handles
sleep(2)
base_window = driver.window_handles[0]
google_login_window = driver.window_handles[1]
driver.switch_to_window(google_login_window)
print(driver.title)

google_id = driver.find_element_by_name("identifier")
google_id.send_keys(GOOGLE_ID)
google_id.send_keys(Keys.ENTER)
sleep(2)
google_pw = driver.find_element_by_name("pw") #구글에서 협조를 안해주는 군

#Tinder 창으로 돌아온다
driver.switch_to_window(base_window)
print(driver.title)

sleep(5)
allow_btn = driver.find_element_by_xpath("allow_location")
allow_btn.click()
notification_btn = driver.find_element_by_xpath("notification_location")
notification_btn.click()
cookies = driver.find_element_by_xpath("cookies_location")
cookies.click()

sleep(2)
for n in range(100):
    sleep(1)
    try:
        like_btn = driver.find_element_by_xpath("like_location")
    except ElementClickInterceptedException:
        try:
            back_btn = driver.find_element_by_xpath("back_location")
            back_btn.click()
        except NoSuchElementException:
            sleep(2)

driver.quit()