import math
def calc(x):
 return str(math.log(abs(12*math.sin(int(x)))))
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import os

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/file_input.html")

first_name = browser.find_element_by_css_selector("input[name='firstname']")
first_name.send_keys("Vasya")

second_name = browser.find_element_by_css_selector("input[name='lastname']")
second_name.send_keys("Petrov")

email = browser.find_element_by_css_selector("input[name='email']")
email.send_keys("fndsd@dsjkd.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))

file_path = os.path.join(current_dir, 'file.txt')
input_file = browser.find_element_by_css_selector("input#file")
input_file.send_keys(file_path)

button = browser.find_element_by_css_selector("button.btn.btn-primary")
button.click()


# button = browser.find_element_by_css_selector("button#book")
# wait = WebDriverWait(browser, 15).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h5#price'), '100')
# )
# button.click()
# x_element = browser.find_element_by_css_selector("span#input_value.nowrap")
# x = x_element.text
# y = calc(x)
# InputPlace = browser.find_element_by_css_selector("input#answer.form-control")
# InputPlace.send_keys(y)
# button = browser.find_element_by_css_selector("button#solve")
# button.click()

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )
# button.click()
# message = browser.find_element_by_id("verify_message")
#
# button1 = WebDriverWait(browser, 5).until_not(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )
#
# assert "successful" in message.text