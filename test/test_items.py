from time import sleep


def test_add_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    #sleep(30)

    button = browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert button, 'кнопка не найдена'