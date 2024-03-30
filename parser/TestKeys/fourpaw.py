
from MainProject.StartTestAppium import StartAppium
from MainProject.IdElements import IdFind
import time
import pyperclip
import json 
def parser_items(id):

    time.sleep(3)
    productName = IdFind.find_id(driver, 'com.appteka.lapy:id/txtProductName')
    productName = productName.text

    share = IdFind.find_id(driver, 'com.appteka.lapy:id/share')
    share.click()
    share = IdFind.find_id(driver, 'android:id/chooser_copy_button')
    share.click()
    clipboard_content = pyperclip.paste()
    words = clipboard_content.split()
   # Поиск и извлечение ссылки
    for word in words:
        if word.startswith("https://"):
            link = word
            break

    print("Ссылка на товар:", link)
    try:
        price = IdFind.find_id(driver, 'com.appteka.lapy:id/txtOldPrice')
        price = price.text
        newPrice = IdFind.find_id(driver, 'com.appteka.lapy:id/txtPrice')
        newPrice = newPrice.text
    except:
        price = IdFind.find_id(driver, 'com.appteka.lapy:id/txtPrice')
        price = price.text
        newPrice = ''
    brand = IdFind.find_id(driver, "com.appteka.lapy:id/brandName")
    brand = brand.text
    cards = {
        'Id': id,
        'Наименование': f'{productName}\n',
        'Ссылка на товар': f'{link}\n',
        'Регулярная цена': f'{price}\n',
        'Промо цена': f'{newPrice}\n',
        'Бренд': f'{brand}\n'
    }
    return cards

driver = StartAppium.appium()
file = []
name = ('Собаки')
categorys = IdFind.finds_id(driver,'com.appteka.lapy:id/txtCategoryName')
for category in categorys:
    if category.text == name:
        category.click()
        break
type_goods = IdFind.finds_id(driver,'com.appteka.lapy:id/txtTitle')

for types in type_goods:
    types.click()
    break
for i in range(10000):
    try: 
        time.sleep(1)

        byer = IdFind.finds_id(driver,'com.appteka.lapy:id/btnToCart')
        if len(byer) != 0:
            break

    except: 
       continue
id = 0
goodnames = IdFind.finds_id(driver,'com.appteka.lapy:id/txtGoodName')
print(len(byer))
for id in range(1000):

    img = IdFind.finds_id(driver,'com.appteka.lapy:id/imgGood')
    img[0].click()
    try:
        sorted = IdFind.find_id(driver,'com.appteka.lapy:id/txtSort')
        driver.back()
        img[1].click()
    except:
        pass
    cards = parser_items(id)
    file.append(cards)
    driver.back()
    time.sleep(2)
    driver.swipe(650,2000,650,1400)
    goodnames = IdFind.finds_id(driver,'com.appteka.lapy:id/txtGoodName')
    print(len(goodnames))
   
    if id > 110:
        break
print(file)

with open('fourpaw.json', 'w', encoding='utf-8') as f:
    json.dump(file, f, indent=4, ensure_ascii=False)