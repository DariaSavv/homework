# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
try:
    driver.get('https://sbis.ru')
    menu = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item-1')
    menu.click()
    sleep(2)
    tensor_logo = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor')
    tensor_logo.click()
    driver.switch_to.window(driver.window_handles[1])
    sleep(2)
    news_block = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content')
    assert news_block.is_displayed()
    about = news_block.find_element(By.LINK_TEXT, 'Подробнее')
    actions = ActionChains(driver)
    actions.move_to_element(about)
    actions.scroll_by_amount(0, 40)
    actions.click(about)
    actions.perform()
    driver.switch_to.window(driver.window_handles[1])
    sleep(5)
    assert driver.current_url == 'https://tensor.ru/about'

finally:
    driver.quit()
