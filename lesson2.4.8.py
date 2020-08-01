from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def logx(x):
	return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Firefox()

browser.get('http://suninjuly.github.io/explicit_wait2.html')

#webdriver, pls wait for 12 seconds before price fall to 100$
price = WebDriverWait(browser, 12).until(
	EC.text_to_be_present_in_element((By.ID, "price"), "$100")
	)

button = browser.find_element_by_css_selector('#book')
button.click()

browser.execute_script("window.scrollBy(0, 250);")

x = browser.find_element_by_css_selector('#input_value')
y = x.text
answer = logx(y)
form_control = browser.find_element_by_id('answer').send_keys(answer)

submint = browser.find_element_by_id('solve').click()


