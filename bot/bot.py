from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

user_name = "1094164565"
password = "1094164565"
driver = webdriver.Firefox()
driver.get("https://climpinutresa.amatia.cloud/autocuidado/courses/autocuidado/login.php?status=LOGIN_FAILED")
element = driver.find_element_by_name("username")
element.send_keys(user_name)
element = driver.find_element_by_name("password")
element.send_keys(password)
element = driver.find_element_by_name("accept_term")
actions = ActionChains(driver)
actions.move_to_element(element).click(element).perform()

element.close()