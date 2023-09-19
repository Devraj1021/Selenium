import time
# C:\Users\DEV\OneDrive\Desktop\Selenium\env\Scripts>activate
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

# PATH = "chromedriver_win32"
#
# options = webdriver.ChromeOptions()
#
# driver = webdriver.Chrome(service=Service(PATH), options=options)
driver = webdriver.Chrome("C:\\Users\\DEV\\OneDrive\\Desktop\\Selenium\\chromedriver_win32\\chromedriver.exe")
#
driver.get("https://www.instagram.com/accounts/login")
# driver.get("https://www.hotstar.com")
# driver.get("https://open.spotify.com/")
time.sleep(5)

element = driver.find_element(By.NAME, "username")
element.clear()
element.send_keys("Devraj1021")
time.sleep(5)

password = driver.find_element(By.NAME, "password")
password.clear()
password.send_keys("Devraj@03")
time.sleep(1000)
# username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input=[name='username']")))
# time.sleep(5)
# password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input=[name='password']")))
# time.sleep(5)
# username.clear()
# time.sleep(5)
# username.send_keys("Devraj1021")
# time.sleep(10)
# password.clear()
# time.sleep(5)
# password.send_keys("devraj03")
# time.sleep(10)

# button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button=[type='submit']")))
# button = driver.find_element(By.TAG_NAME, "Log in")
# button.click()
# button = driver.find_element(By.CSS_SELECTOR, "submit")
# button.click()
driver.find_element(By.XPATH, "///*[@id='loginForm']/div[1]/div[3]/button/div").click()
# //*[@id="loginForm"]/div[1]/div[3]/button/div
# /html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[1]/div[3]/button/div
time.sleep(20)
#
# driver.find_element()
