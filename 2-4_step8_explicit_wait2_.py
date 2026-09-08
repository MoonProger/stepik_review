from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # ЯВНОЕ ОЖИДАНИЕ (лимит - 5 сек, проверяет пока кнопка не станет кликабельной)
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # math
    x_value = browser.find_element(By.CSS_SELECTOR, "[id='input_value']").text
    y = str(math.log(abs(12 * math.sin(int(x_value)))))
    (browser.find_element(By.CSS_SELECTOR, "[id='answer']")).send_keys(y)

    # сабмит
    (browser.find_element(By.ID, "solve")).click()

finally:
    time.sleep(3)
    print(browser.switch_to.alert.text.split(': ')[-1]) # выводим код степика
    browser.quit()