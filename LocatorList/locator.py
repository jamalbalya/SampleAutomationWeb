from selenium.webdriver.common.by import By

class MainPageLocators(object):
    USERNAME = (By.NAME, "user-name")
    PASSWORD = (By.NAME, "password")
    BTN_LOGIN = (By.ID, "login-button")
    LOGO = (By.XPATH, "//*[@id='header_container']/div[1]/div[2]/div")

# Homepage item
    BTN_ITEM_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    BTN_ITEM_BIKE_LIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    SHOPPING_CART = (By.XPATH, "//*[@id='shopping_cart_container']/a")

# Page Cart
    BTN_REMOVE = (By.ID, "remove-sauce-labs-backpack")
    BTN_CONTINUE_SHOPING = (By.ID, "continue-shopping")
    BTN_CHECKOUT = (By.ID, "checkout")

# Page Checkout Information
    COLUMN_FIRSTNAME = (By.ID, "first-name")
    COLUMN_LASTNAME = (By.ID, "last-name")
    COLUMN_POSTAL_CODE = (By.ID, "postal-code")
    BTN_CONTINUE_CHECKOUT = (By.ID, "continue")
    CHECKOUT_THANK_YOU = (By.ID, "checkout_complete_container")

# Page Checkout overview
    BTN_FINISH = (By.ID, "finish")
    BTN_CANCEL = (By.ID, "cancel")

# Page chcekout complete
    BTN_BACK_HOMEPAGE = (By.ID, "back-to-products")