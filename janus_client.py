from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

opts = Options()
opts.set_preference(name="permissions.default.microphone", value=1)
opts.set_preference(name="permissions.default.camera", value=1)


driver = webdriver.Firefox(options = opts)
driver.get("https://classickerobel.duckdns.org:8083/")
username = driver.find_element_by_name("username")
username.send_keys("default")
password = driver.find_element_by_name("password")
password.send_keys("123")
password.send_keys(Keys.RETURN)

driver.get("https://classickerobel.duckdns.org:8083/streamer")
