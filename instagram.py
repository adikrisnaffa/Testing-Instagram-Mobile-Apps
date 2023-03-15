from time import sleep
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

caps = {
    "appPackage" : "com.instagram.android",
    "appActivity" : "com.instagram.mainactivity.MainActivity",
    "noReset" : True,
    "platformName" : "Android",
    "automationName" : "UiAutomator2",
    "newCommandTimeout" : "3600"
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)

driver.implicitly_wait(30)

def test_instagram():
    Search_Explore = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout[@content-desc=\"Search and explore\"]/android.widget.ImageView")
    Search_Explore.click()

    Reels = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout[@content-desc=\"Reels\"]/android.widget.ImageView")
    Reels.click()

    Shop = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout[@content-desc=\"Home\"]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ImageView")
    Shop.click()

    Profile = driver.find_element(by=AppiumBy.ID, value="com.instagram.android:id/tab_avatar")
    Profile.click()

    driver.quit()