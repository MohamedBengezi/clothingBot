from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def gecko_test(site_000='https://shop.misha-and-puff.com/products/house-sweater?variant=17828310024243&oi=0'):
    """
    simple overview:
        1) set up webdriver
        2) load this article 
        3) close up shop 

    input:
        >> site_000
            > default: url of this article
    """
    # # set the driver
    driver = webdriver.Firefox()

    # # load this article
    driver.get(site_000)
    # # and chill a bit
    # sleep(1)
    # elem = driver.find_element_by_link_text('House Sweater')
    # print(elem)
    # elem.send_keys(webdriver.common.keys.Keys.RETURN)
    sleep(3)

    select = driver.find_element_by_xpath("//select[@data-product-option='option2']")
    all_options = select.find_elements_by_tag_name("option")
    for option in all_options:
        value = option.get_attribute("value")
        if value == "4-5 y":
            print("Value is: %s" % value)
            option.click()

    # select by visible text
    # select.select_by_visible_text('4-5 y')

    addToCart = driver.find_element_by_xpath("//input[@value='Add to cart']")
    addToCart.send_keys(webdriver.common.keys.Keys.RETURN)
    sleep(2)

    checkout = driver.find_element_by_xpath("//a[@href='/checkout']")
    checkout.send_keys(webdriver.common.keys.Keys.RETURN)
    sleep(2)

    email = driver.find_element_by_xpath("//input[@id='checkout_email']")
    email.send_keys('testst')

    firstName = driver.find_element_by_xpath("//input[@name='checkout[shipping_address][first_name]']")
    firstName.send_keys('Hanin')

    lastName = driver.find_element_by_xpath("//input[@id='checkout_shipping_address_last_name']")
    lastName.send_keys('Bengezi')

    address = driver.find_element_by_xpath("//input[@id='checkout_shipping_address_address1']")
    address.send_keys('12 testing st')

    city = driver.find_element_by_xpath("//input[@id='checkout_shipping_address_city']")
    city.send_keys('Seattle')

    country = driver.find_element_by_xpath("//select[@id='checkout_shipping_address_country']")
    all_options = country.find_elements_by_tag_name("option")
    for option in all_options:
        value = option.get_attribute("value")
        if value == "United States":
            print("Value is: %s" % value)
            option.click()
            break

    state = driver.find_element_by_xpath("//select[@id='checkout_shipping_address_province']")
    state_options = state.find_elements_by_tag_name("option")
    for states in state_options:
        value1 = states.get_attribute("value")
        print("Value1 is: %s" % value1)
        if value1 == "WA":
            print("Value is: %s" % value1)
            states.click()
            break

    zipcode = driver.find_element_by_xpath("//input[@id='checkout_shipping_address_zip']")
    zipcode.send_keys('TEST')

    phone = driver.find_element_by_xpath("//input[@id='checkout_shipping_address_phone']")
    phone.send_keys('9055311442')

    button =  driver.find_element_by_xpath("//button[@name='button']")
    button.send_keys(webdriver.common.keys.Keys.RETURN)


    # driver.find_element_by_xpath("//input[@id='checkout_shipping_address_first_name']")
    # checkout_shipping_address_first_name
    # checkout_shipping_address_last_name
    # checkout_shipping_address_address1
    # checkout_shipping_address_city
    # select checkout_shipping_address_country
    # select checkout_shipping_address_province
    # checkout_shipping_address_zip
    # checkout_shipping_address_phone
    # button continue_to_shipping_method_button


    # k, cool. let's bounce.
  #  driver.quit()


# make runable
if __name__ == '__main__':
    # here we go
    gecko_test()
