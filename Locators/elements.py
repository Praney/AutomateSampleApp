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

    temparrayMax = []
    temparrayMin = []

    for i in range(1,6):
        temparrayMax.append((By.XPATH,"//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ViewFlipper/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[" + str(i) + "]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView[2]"))

    for j in range(1,6):
        temparrayMin.append((By.XPATH,"//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ViewFlipper/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[" + str(j) + "]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView[3]"))