from time import sleep
import pytest


@pytest.mark.parametrize('user_language', [''])
def test_add_to_cart_button(browser, user_language):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    sleep(1)

    button = browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert button, 'кнопка не найдена'