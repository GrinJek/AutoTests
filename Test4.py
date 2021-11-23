import math
def calc(x):
 return str(math.log(abs(12*math.sin(int(x)))))
from selenium import webdriver

# browser = webdriver.Chrome()
# browser.execute_script("document.title='Script executing';alert('Robots at work');")

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

button = browser.find_element_by_css_selector("button.trollface.btn.btn-primary")
button.click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
x_element = browser.find_element_by_css_selector("span#input_value.nowrap")
x = x_element.text
y = calc(x)
InputPlace = browser.find_element_by_css_selector("input#answer.form-control")
InputPlace.send_keys(y)
button = browser.find_element_by_css_selector("button.btn.btn-primary")
button.click()


# confirm = browser.switch_to.alert
# confirm.accept()
# x_element = browser.find_element_by_css_selector("span#input_value.nowrap")
# x = x_element.text
# y = calc(x)
# InputPlace = browser.find_element_by_css_selector("input#answer.form-control")
# InputPlace.send_keys(y)
# button = browser.find_element_by_css_selector("button.btn.btn-primary")
# button.click()





# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# browser.execute_script("window.scrollBy(0, 100);")
# button.click()

# x_element = browser.find_element_by_css_selector("span#input_value.nowrap")
# x = x_element.text
# y = calc(x)
#
# InputPlace = browser.find_element_by_css_selector("input#answer.form-control")
# InputPlace.send_keys(y)
#
# button = browser.find_element_by_css_selector("button.btn.btn-primary")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#
# option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
# option1.click()
#
# option2 = browser.find_element_by_css_selector("[id='robotsRule']")
# option2.click()
#
# button.click()
