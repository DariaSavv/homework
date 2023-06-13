# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys, ActionChains
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
sbis_site = ' https://fix-online.sbis.ru/'

try:
    driver.get(sbis_site)
    sleep(1)
    user_login, user_password = 'Веспа', 'Веспа123'
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(user_login, Keys.ENTER)
    assert login.get_attribute('value') == user_login
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_password, Keys.ENTER)
    sleep(5)
    driver.get('https://fix-online.sbis.ru/page/contacts')
    sleep(1)
    search = driver.find_element(By.CSS_SELECTOR, '[name="ws-input_2023-06-13"]')
    search.send_keys('Савватеева', Keys.ENTER)
    sleep(2)
    dialog = driver.find_element(By.CSS_SELECTOR, '.ws-ellipsis')
    dialog.click()
    sleep(8)


finally:
    driver.quit()