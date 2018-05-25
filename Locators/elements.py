from selenium.webdriver.common.by import By

class PageLocators(object):
    
    # A class for page locators. All locators should come here
    city = (By.XPATH,"//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ViewFlipper/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout")

    temperature = (By.ID,"com.daniloprado.weather:id/textview_temperature")

    add = (By.ID,"com.daniloprado.weather:id/fab")

    enterCityName = (By.ID,"com.daniloprado.weather:id/edittext_toolbar_city_search")

    cityList = (By.ID,"com.daniloprado.weather:id/textview_found_city_name")

    navigate = (By.XPATH,'//android.widget.ImageButton[@content-desc="Navigate up"]')

    verify = (By.XPATH,"//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ViewFlipper/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[5]/android.widget.RelativeLayout/android.widget.TextView")
