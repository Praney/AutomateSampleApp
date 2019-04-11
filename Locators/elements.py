from selenium.webdriver.common.by import By

class PageLocators(object):
    
    # A class for page locators. All locators should come here
    notif = (By.ID,"doc.saulmm.notification: id / simple_notification")

    title = (By.ID,"android: id / title")

    clearNotif = (By.ID,"com.android.systemui: id / clear_notification")