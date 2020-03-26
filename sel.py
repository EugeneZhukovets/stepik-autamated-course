from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )
button_book = browser.find_element_by_id("book")
button_book.click()

num = browser.find_element_by_id("input_value").text
y = calc(num)

answer = browser.find_element_by_id("answer")
answer.send_keys(y)

submit = browser.find_element_by_id("solve")
submit.click()
time.sleep(5)
browser.quit()

