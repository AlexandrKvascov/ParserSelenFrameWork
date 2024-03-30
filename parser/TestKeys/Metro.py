from MainProject.ClassElements import ClassFind
from MainProject.XpathElements import XpathFind
from MainProject.Keycode import Key
from MainProject.StartTestAppium import StartAppium
from MainProject.TextElements import TextFind
from MainProject.TapElementAppium import TapElement
from MainProject.InputTextAppium import TextInput
from MainProject.SwipeAppium import Swipe
from MainProject.IdElements import IdFind
from MainProject.StartTestSelenium import StartSelenium
import time
import pyperclip
import json 
import re
Brends =[
        'BAZARCO',
        'GRAN ANA PAULA',
        'MYASOET MEAT COMPANY',
        'PRIMEBEEF',
        'АГРОЭКО',
        'АТЯШЕВО',
        'БЛИЖНИЕ ГОРКИ',
        'БУТЧЕР',
        'Без бренда',
        'ВАХАВЯК ПЛЮС',
        'ВЕСКО',
        'ДИЕТА18',
        'ДМИТРОГОРСКИЙ ПРОДУКТ',
        'ДОМАШНИЙ РЕСТОРАТОР',
        'ЗАРЕЧНОЕ',
        'КРОЛЪ И К',
        'МИРАТОРГ',
        'МЯСНИКИ',
        'МЯСО ЕСТЬ!',
        'ОБРАЗЦОВО',
        'ОСТАНКИНО',
        'САМСОН',
        'СЛОВО МЯСНИКА',
        'ФИЛЬЕ ПРОПЕРТИ',
        'ЧЕРКИЗОВО',
        'ЭКОЛЬ',
        'METRO CHEF'
]

driver = StartSelenium.sellenium()

url = 'https://online.metro-cc.ru/category/myasnye/myaso'
driver.get(url)



def cardsInfo(elem, id):
    description = ClassFind.webfindClass(elem,'product-card-name__text')
    product_name = description.text
    print(product_name)
    for  i in Brends:
        if i in product_name.upper():
            brend = i
            break
        else:
            brend = 'unknown'
    text_price = ClassFind.webfindClass(elem, 'product-unit-prices__trigger')
    text_price = text_price.text
    print(text_price)
    text = text_price.split('\n')
    print(len(text))
    if len(text) == 2:
        price = re.sub(r'д', 'р', text[0])
        newPrice = ''

    elif len(text)==3:
        newPrice = re.sub(r'д', 'р', text[0])
        price = re.sub(r'д', 'р', text[2])
    else:
        price = 'Unknow'
        newPrice = 'Unknow'

    src = ClassFind.webCssSelectr(elem,'.product-card-photo__link.reset-link')
    href = ClassFind.Attribute(src,'href')

    cards = {
            'Id': id,
            'Наименование': f'{product_name}\n',
            'Ссылка на товар': f'{href}\n',
            'Регулярная цена': f'{price}\n',
            'Промо цена': f'{newPrice}\n',
            'Бренд': f'{brend}\n'
        }
    return cards
file = []
id = 0
for i in range(1000):
    time.sleep(5)
    elements = ClassFind.webCssSelectors(driver, '.catalog-2-level-product-card.product-card.subcategory-or-type__products-item.with-prices-drop')
    print(len(elements))
    for elem in range(len(elements)):
        id += 1
        inform = cardsInfo(elements[elem], id)
        file.append(inform)
        print(inform)
    if id >300:
        break
            
  
    driver.execute_script("arguments[0].scrollIntoView();", elements[-1])
   
    next = ClassFind.webCssSelectr(driver,'.v-pagination__navigation.catalog-paginate__item')
    # print(len(next))
    next.click()
with open('metro.json', 'w', encoding='utf-8') as f:
    json.dump(file,f,indent=4, ensure_ascii=False)