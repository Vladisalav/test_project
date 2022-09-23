from selenium.webdriver.common.by import By


def test_add_to_card(browser):
    page = ProductPage(url="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/, browseer")
    url = browser.find_element_by_css_selector("#login_link")
    link.click()

def test_guest_can_go_to_login_page(browser):
   browser.get(link)
   go_to_login_page(browser)
