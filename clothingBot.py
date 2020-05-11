import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

site_000 = 'https://apolina-kids.com/collections/all'


if __name__ == '__main__':
    # setting the site and driver
    driver = webdriver.Firefox()
    # load the site
    URL = site_000
    driver.get(URL)
    sleep(1)
    findItem('POL DRESS - FARM CHECK / HAY')
    sleep(1)
    selectSize()
    addToCart()
    sleep(3)
    shippingDetails()
    clickButton(None)
    sleep(2.5)
    clickButton(None)
    sleep(3)


def findItem(prodName):
    elem = driver.find_element_by_xpath('//img[contains(@alt,"'+prodName+'")]')
    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(elem, 5, 5)
    action.click()
    action.perform()


def selectSize():
    try:
        select = driver.find_element_by_xpath(
            "//select[@id=\"product-select-4540644753485-option-0\"]")
        all_options = select.find_elements_by_tag_name("option")
        for option in all_options:
            value = option.get_attribute("value")
            if value == "5-7Y":
                print("Value is: %s" % value)
                option.click()
    except:
        print('No select found')


def addToCart():
    try:
        addToCart = driver.find_element_by_xpath(
            "//input[@value='Add to Cart']")
    except:
        print('Add To Cart button not found')

    try:
        addToCart.send_keys(webdriver.common.keys.Keys.RETURN)
    except:
        try:
            addToCart.click()
        except:
            print("Could not click 'Add to cart'")
    sleep(2)

    checkout = driver.find_element_by_xpath(
        "//input[@value='Check Out']")
    checkout.send_keys(webdriver.common.keys.Keys.RETURN)


def clickButton(id):
    if (id is None):
        cont = driver.find_element_by_name("button")
    else:
        cont = driver.find_element_by_id(id)
    cont.send_keys(webdriver.common.keys.Keys.RETURN)


def shippingDetails():
    email = driver.find_element_by_id("checkout_email")
    email.send_keys('hanin68@gmail.com')

    firstName = driver.find_element_by_id(
        "checkout_shipping_address_first_name")
    firstName.send_keys('Hanin')

    lastName = driver.find_element_by_id("checkout_shipping_address_last_name")
    lastName.send_keys('Bengezi')

    address = driver.find_element_by_id(
        "checkout_shipping_address_address1")
    address.send_keys('6818 137th Ave NE')

    aprtment = driver.find_element_by_id(
        "checkout_shipping_address_address2")
    aprtment.send_keys('Unit 437')

    city = driver.find_element_by_id(
        "checkout_shipping_address_city")
    city.send_keys('Redmond')

    country = driver.find_element_by_id(
        "checkout_shipping_address_country")
    all_options = country.find_elements_by_tag_name("option")
    for option in all_options:
        value = option.get_attribute("value")
        if value == "United States":
            print("Value is: %s" % value)
            option.click()
            break

    state = driver.find_element_by_id(
        "checkout_shipping_address_province")
    state_options = state.find_elements_by_tag_name("option")
    for states in state_options:
        value1 = states.get_attribute("value")
        print("Value1 is: %s" % value1)
        if value1 == "WA":
            print("Value is: %s" % value1)
            states.click()
            break

    zipcode = driver.find_element_by_id(
        "checkout_shipping_address_zip")
    zipcode.send_keys('98052')

    phone = driver.find_element_by_id("checkout_shipping_address_phone")
    phone.send_keys('9055311442')


# def inputPayment():
    # driver.switch_to.frame(driver.find_element_by_xpath(
    #     "//*[contains(@id,'card-fields-number')]"))
    # wait = WebDriverWait(driver, 10)
    # wait.until(EC.frame_to_be_available_and_switch_to_it(
    #     (By.CLASS_NAME, "card-fields-iframe")))

    # cardNumber = driver.find_element_by_id("number")
    # cardNumber.send_keys('4930 0000 0000 0000')

    # name = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    #     (By.XPATH, "//input[@id='name']")))
    # driver.execute_script("arguments[0].setAttribute(arguments[1], arguments[2]);",
    #                       name,
    #                       "value",
    #                       "NNAAAAMME")
    # name.send_keys('NAME')
    # name.send_keys(webdriver.common.keys.Keys.RETURN)

    # js = "arguments[0].setAttribute('value','\"+NAME+\"')"
    # expiry = driver.find_element_by_id("expiry")
    # driver.execute_script("arguments[0].setAttribute(arguments[1], arguments[2]);",
    #                       expiry,
    #                       "value",
    #                       "04 / 34")

    # verification_value = driver.find_element_by_id("verification_value")
    # driver.execute_script("arguments[0].setAttribute(arguments[1], arguments[2]);",
    #                       verification_value,
    #                       "value",
    #                       "123")
    # sleep(10)

    # driver.switch_to.default_content()
