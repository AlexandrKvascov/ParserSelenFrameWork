from MainProject.ClassElements import ClassFind
from MainProject.XpathElements import XpathFind
from MainProject.Keycode import Key
from MainProject.StartTestAppium import StartAppium
from MainProject.TextElements import TextFind
from MainProject.TapElementAppium import TapElement
from MainProject.InputTextAppium import TextInput
from MainProject.SwipeAppium import Swipe
#_____Пример теста, как легко их писать_______


#импортируем driver для подключения к эмулятору 
driver = StartAppium.appium()

#Нажимаем на таб бар снизу, для этого нам нужен его content-desc
#Всегда передаём два параметра, driver и его xpath
tab = XpathFind.find_content_view(driver, "Create\nTab 3 of 5")
tab.click()

#Выбираем отправку 
#Внимательно проверять \n часто бывает такое, что они ломают адрес
want_send = XpathFind.find_xpath_app(driver,'//android.widget.ImageView[@content-desc="Ready\nto send"]')
want_send.click()


#Нажимаем на from 

from_send = XpathFind.find_xpath_app(driver,'//android.view.View[@content-desc="From"]')

from_send.click()

#Дальше мы должны были ввести город, но сломалась клавиатура на эмуляторе 

TextInput.EnglishInput(driver, "Saint Petersburg")
first_elem = XpathFind.find_xpath_app(driver, '//android.view.View[@content-desc="Dismiss"]/android.view.View/android.widget.EditText/android.view.View[2]/android.view.View')

TapElement.tapLocation(driver, first_elem)
to_send = XpathFind.find_xpath_app(driver,'//android.view.View[@content-desc="To"]')
to_send.click()

TextInput.EnglishInput(driver, "Moscow")
second_elem = XpathFind.find_xpath_app(driver,'//android.view.View[@content-desc="Dismiss"]/android.view.View/android.widget.EditText/android.view.View[2]/android.view.View')
TapElement.tapLocation(driver, second_elem)



#Выбираем дату 

from_date = XpathFind.find_xpath_app(driver,'//android.view.View[@content-desc="From"]')
from_date.click()

okey = XpathFind.find_xpath_app(driver,'//android.widget.Button[@content-desc="OK"]')
okey.click()

to_date = XpathFind.find_xpath_app(driver, '//android.view.View[@content-desc="To"]')
to_date.click()
okey = XpathFind.find_xpath_app(driver,'//android.widget.Button[@content-desc="OK"]')

okey.click()

Swipe.toElemntDown(driver, '//android.widget.CheckBox[@content-desc="Approximately"]')


train_one = XpathFind.find_xpath_app(driver, '(//android.widget.ImageView[@content-desc="Railway station"])[1]')
train_one.click()

train_two = XpathFind.find_xpath_app(driver, '(//android.widget.ImageView[@content-desc="Railway station"])[2]')
train_two.click()


doc = XpathFind.find_content_widget_button(driver,'Documentation\nDocuments, books, paper products')
doc.click()

Swipe.toElemntDown(driver, '//android.view.View[@content-desc="Keep cold"]')

s_size = XpathFind.find_content_widget_image(driver, "S\nUp to 2 kg\n23x19x10 cm")
s_size.click()
Swipe.toElemntDown(driver, '//android.widget.Button[@content-desc="Next"]')


phone = ClassFind.findAllClassNames(driver, 'android.widget.EditText')
for i in phone:
    i.click()
    i.send_keys('89111644684')
    Key.Entercode(driver)
    
    
next = XpathFind.find_xpath_app(driver, '//android.widget.Button[@content-desc="Next"]')
next.click()
post = XpathFind.find_xpath_app(driver, '//android.widget.Button[@content-desc="Post"]')
post.click()

