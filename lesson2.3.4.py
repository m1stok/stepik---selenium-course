from selenium import webdriver
from time import sleep
import math

link = 'http://suninjuly.github.io/alert_accept.html'

try:
	browser = webdriver.Firefox()
	browser.get(link)

	button = browser.find_element_by_tag_name("button").click()

	alert = browser.switch_to.alert.accept()

	sleep(0.5)

	def logrfm(x):
		return str(math.log(abs(12*math.sin(int(x)))))

	x = browser.find_element_by_css_selector('#input_value')
	y = x.text
	answer = logrfm(y)

	form_control = browser.find_element_by_id('answer').send_keys(answer)

	submint = browser.find_element_by_css_selector('.btn').click()

finally:
	sleep(15)
	browser.quit()