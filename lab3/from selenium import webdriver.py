from selenium import webdriver

import time
import random

# открываем браузер и переходим на страницу
driver = webdriver.Chrome()
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSd4k-0Mui1sKFOBYIiZzDBCjyNuS_UK-Qw0hssHOO2_E4L1hQ/viewform?usp=sf_link')

# находим все элементы с вопросами
question_container = driver.find_element_by_class_name('freebirdFormviewerViewItemsItemItem')
questions = question_container.find_elements_by_css_selector('.quantumWizTogglePaperradioEl')

# выводим текст каждого вопроса
for question in questions:
    print(question.text)

# закрываем браузер
driver.quit()