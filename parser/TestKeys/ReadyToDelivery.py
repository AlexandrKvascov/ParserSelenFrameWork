from MainProject.ClassElements import ClassFind
from MainProject.XpathElements import XpathFind
from MainProject.Keycode import Key
from MainProject.StartTestAppium import StartAppium
from MainProject.TextElements import TextFind
from MainProject.TapElementAppium import TapElement
from MainProject.InputTextAppium import TextInput
from MainProject.SwipeAppium import Swipe
driver = StartAppium.appium()
tab = XpathFind.find_content_view(driver, "Create\nTab 3 of 5")
tab.click()

