# import pyperclip

# # Получение содержимого буфера обмена
# clipboard_content = pyperclip.paste()

# # Вывод содержимого буфера обмена
# print("Содержимое буфера обмена:", clipboard_content)
# words = clipboard_content.split()

# # Поиск и извлечение ссылки
# for word in words:
#     if word.startswith("https://"):
#         link = word
#         break

# print("Ссылка на товар:", link)
import re

# text = '488 д\n/кг\n549 д'
text  = '1 119 д\n/кг'
text = text.split('\n')
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