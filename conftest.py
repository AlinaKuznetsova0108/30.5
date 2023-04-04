from settings import valid_email, valid_password
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

driver = webdriver.Chrome(executable_path="C:\\Users\\User\\PycharmProjects\\pythonProject\\30.5.1\\chromedriver.exe")

@pytest.fixture(autouse=True, scope="session")
def testing():
#    options = webdriver.ChromeOptions()
#    options.add_argument("--start-maximized")
#    pytest.driver = webdriver.Chrome('d:/chromedriver.exe', chrome_options=options)

    pytest.driver = webdriver.Chrome('C:\\Users\\User\\PycharmProjects\\pythonProject\\30.5\\chromedriver.exe')

    pytest.driver.implicitly_wait(10)

    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    field_email = pytest.driver.find_element(By.ID, 'email')
    field_email.clear()
    field_email.send_keys(valid_email)

    field_pass = pytest.driver.find_element(By.ID, 'pass')
    field_pass.clear()
    field_pass.send_keys(valid_password)
    time.sleep(2)

    pytest.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/all_pets', "Некорректный email или пароль"
    if not pytest.driver.current_url == 'https://petfriends.skillfactory.ru/all_pets':
        pytest.driver.quit()
        raise Exception("Некорректный email или пароль")

    if pytest.driver.find_element(By.XPATH, "//body/nav[1]/button[1]").is_displayed():
        time.sleep(2)
        pytest.driver.find_element(By.XPATH, "//body/nav[1]/button[1]").click()
        time.sleep(2)

    pytest.driver.find_element(By.XPATH, "//a[contains(text(),'Мои питомцы')]").click()

    assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/my_pets', "Не страница Мои питомцы"
    if not pytest.driver.current_url == 'https://petfriends.skillfactory.ru/my_pets':
        pytest.driver.quit()
        raise Exception("Не страница Мои питомцы")

    yield

    pytest.driver.quit()
