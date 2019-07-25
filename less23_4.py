from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import  math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

element = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "10000")
)

button = browser.find_element_by_id("book")
button.click()

x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text
y = calc(x)

element = browser.find_element_by_css_selector("#answer")
element.send_keys(y)

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("#solve")
button.click()