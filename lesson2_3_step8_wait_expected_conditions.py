from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import log, sin
from time import sleep

def calc(x):
  return str(log(abs(12*sin(int(x)))))


try:
    browser = webdriver.Chrome()

    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    # говорим Selenium проверять в течение 15 секунд, пока цена не станет 100$
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element_by_id("book").click()

    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    browser.find_element_by_id("answer").send_keys(y)


    #button = browser.find_element_by_css_selector("#solver")
    button = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.ID, "solve"))
    )
    browser.execute_script("return arguments[0].scrollIntoView();", button)
    button.click()

    answer = browser.switch_to.alert.text
    print(answer.split()[-1])

    sleep(1)

    browser.switch_to.alert.accept()


except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')


finally:
    sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()

