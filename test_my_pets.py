from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


def test_all_my_pets():
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/div[1]/div[1]/div[1]")))

    number_stat = int(pytest.driver.find_element(By.XPATH, '//body/div[1]/div/div[1]').text.split()[2])
    print()
    print('колличество питомцев по статистике=', str(number_stat))

    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))

    number_pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    print('колличество питомцев в таблице=', len(number_pets))

    assert number_stat == len(number_pets), "колличество питомцев не совпадает со статистикой юзера"


def test_pets_have_photo():

    pytest.driver.implicitly_wait(10)

    number_stat = int(pytest.driver.find_element(By.XPATH, '//body/div[1]/div/div[1]').text.split()[2])
    print()
    print('колличество питомцев по статистике=', str(number_stat))

    pytest.driver.implicitly_wait(10)

    number_pets_without_photo = len(pytest.driver.find_elements(By.XPATH, '//img[@src=""]'))
    print('колличество питомцев без фото=', str(number_pets_without_photo))

    assert (number_stat / 2) >= number_pets_without_photo, "колличество питомцев без фото больше"


def test_all_pets_have_name_ages_breeds():

    pytest.driver.implicitly_wait(5)
    names = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[1]')

    pytest.driver.implicitly_wait(5)
    breeds = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[2]')

    pytest.driver.implicitly_wait(5)
    ages = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[3]')

    for i in range(len(names)):
        print(names[i].text+','+breeds[i].text+','+ages[i].text)
        assert names[i].text != '', "Не у всех есть имя"
        assert breeds[i].text != '', "Не у всех есть порода"
        assert ages[i].text != '', "Не у всех есть возраст"


def test_duplicate_name():
    pytest.driver.implicitly_wait(5)

    names = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[1]')

    pets_names = []
    r = 0

    for name in names:
        name = name.text
        pets_names.append(name)
        print()
        print(pets_names)
        print('name=', name)

        r = pets_names.count(name)
        if r != 1:
            break

    assert r == 1, "Есть питомцы с одинаковыми именами"


def test_duplicate_pets():
    pytest.driver.implicitly_wait(5)
    names = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[1]')

    pytest.driver.implicitly_wait(5)
    breeds = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[2]')

    pytest.driver.implicitly_wait(5)
    ages = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[3]')

    pets = []
    r = 0
    print()

    for i in range(len(names)):
        pets.append({
            'name': names[i].text,
            'breed': breeds[i].text,
            'age': ages[i].text
        })

        print('pets[', str(i), ']=', pets[i])

        r = pets.count(pets[i])
        print('колличество вхождений =', str(r))
        if r != 1:
            break

    assert r == 1, "Есть повторяющиеся питомцы (с одинаковыми именами, породой и возрастом)"
