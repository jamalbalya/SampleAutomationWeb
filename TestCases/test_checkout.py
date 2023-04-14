from LocatorList.locator import *
import time
import configparser


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        driver.implicitly_wait(15)


class MainPage(BasePage):
    def CheckoutItem(self):
        element_item_backpack = self.driver.find_element(*MainPageLocators.BTN_ITEM_BACKPACK)
        assert element_item_backpack.is_displayed(), "Item backpack button is not displayed"
        element_item_backpack.click()
        time.sleep(3)

        element_shopping_cart = self.driver.find_element(*MainPageLocators.SHOPPING_CART)
        assert element_shopping_cart.is_displayed(), "Shopping cart button is not displayed"
        element_shopping_cart.click()
        time.sleep(3)

        element_btn_checkout = self.driver.find_element(*MainPageLocators.BTN_CHECKOUT)
        assert element_btn_checkout.is_displayed(), "Checkout button is not displayed"
        element_btn_checkout.click()
        time.sleep(3)

        # Checkout Information
        InformationCheckout = configparser.ConfigParser()
        InformationCheckout.read('InformationCheckout.ini')
        firstname = InformationCheckout.get("application", "firstname")
        lastname = InformationCheckout.get("application", "lastname")
        PostalCode = InformationCheckout.get("application", "PostalCode")

        element_column_firstname = self.driver.find_element(*MainPageLocators.COLUMN_FIRSTNAME)
        assert element_column_firstname.is_displayed(), "Column firstname is not displayed"
        element_column_firstname.send_keys(firstname)
        time.sleep(2)

        element_column_lastname = self.driver.find_element(*MainPageLocators.COLUMN_LASTNAME)
        assert element_column_lastname.is_displayed(), "Column lastname is not displayed"
        element_column_lastname.send_keys(lastname)
        time.sleep(2)

        element_column_postal_code = self.driver.find_element(*MainPageLocators.COLUMN_POSTAL_CODE)
        assert element_column_postal_code.is_displayed(), "Column postal code is not displayed"
        element_column_postal_code.send_keys(PostalCode)
        time.sleep(2)

        element_btn_continue = self.driver.find_element(*MainPageLocators.BTN_CONTINUE_CHECKOUT)
        assert element_btn_continue.is_displayed(), "Continue checkout button is not displayed"
        element_btn_continue.click()
        time.sleep(3)

        # Checkout overview
        element_btn_finish = self.driver.find_element(*MainPageLocators.BTN_FINISH)
        assert element_btn_finish.is_displayed(), "Finish button is not displayed"
        element_btn_finish.click()
        time.sleep(3)

        # Checkout complete
        element_btn_back_homepage = self.driver.find_element(*MainPageLocators.BTN_BACK_HOMEPAGE)
        assert element_btn_back_homepage.is_displayed(), "Back to homepage button is not displayed"
        element_btn_back_homepage.click()
        time.sleep(3)
