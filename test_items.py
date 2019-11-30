from selenium import webdriver
import time

def test_language_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    browser.implicitly_wait(5)
    
    find_add_basket_button=browser.find_element_by_css_selector("#add_to_basket_form > button")
    
    assert find_add_basket_button, "not found"
    
