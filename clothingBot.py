import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

site_000 = 'https://shop.misha-and-puff.com/collections/sale'


def selectSize():
    select = driver.find_element_by_xpath(
        "//select[@data-product-option='option2']")
    all_options = select.find_elements_by_tag_name("option")
    for option in all_options:
        value = option.get_attribute("value")
        if value == "4-5 y":
            print("Value is: %s" % value)
            option.click()


def addToCart():
    addToCart = driver.find_element_by_xpath("//input[@value='Add to cart']")

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "add-to-cart"))
        )
    except:
        print("timed out waiting for product page")

    try:
        addToCart.send_keys(webdriver.common.keys.Keys.RETURN)
    except:
        try:
            addToCart.click()
        except:
            print("Could not click 'Add to cart'")
    sleep(2)

    checkout = driver.find_element_by_xpath("//a[@href='/checkout']")
    checkout.send_keys(webdriver.common.keys.Keys.RETURN)


def findItem(prodName):
    elem = driver.find_element_by_xpath('//img[contains(@alt,"'+prodName+'")]')
    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(elem, 5, 5)
    action.click()
    action.perform()


def clickButton():
    cont = driver.find_element_by_name("button")
    cont.send_keys(webdriver.common.keys.Keys.RETURN)


def inputPayment():
    wait = WebDriverWait(driver, 10)
    wait.until(EC.frame_to_be_available_and_switch_to_it(
        (By.CLASS_NAME, "card-fields-iframe")))

    cardNumber = driver.find_element_by_id("number")
    cardNumber.send_keys('493')

    name = driver.find_element_by_id("name")
    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(name, 5, 5)
    action.click()
    action.send_keys_to_element(name, 'meeee')

    expiry = driver.find_element_by_id("expiry")
    expiry.send_keys('04 / 34')

    verification_value = driver.find_element_by_id("verification_value")
    verification_value.send_keys('123')

    driver.switch_to.default_content()


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


if __name__ == '__main__':
    # setting the site and driver
    driver = webdriver.Firefox()
    # load the site
    driver.get(site_000)
    prodName = sys.argv[1]
    sleep(1)
    findItem(prodName)
    sleep(2)
    selectSize()
    addToCart()
    sleep(6)
    shippingDetails()
    clickButton()
    sleep(4.5)
    clickButton()
    sleep(7)
    inputPayment()
