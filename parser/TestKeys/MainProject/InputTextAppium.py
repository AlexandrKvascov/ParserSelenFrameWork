from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import json, time

class TextInput():
    def EnglishInput(driver, text):
        time.sleep(2)
        abc_file = {
        "q":"key_q" ,
        "w":"key_w" ,
        "e":"key_e" ,
        "r":"key_r" ,
        "t":"key_t" ,
        "y":"key_y" ,
        "u":"key_u" ,
        "i":"key_i" ,
        "o":"key_o" ,
        "p":"key_p" ,
        "a":"key_a" ,
        "s":"key_s" ,
        "d":"key_d" ,
        "f":"key_f" ,
        "g":"key_g" ,
        "h":"key_h" ,
        "j":"key_j" ,
        'k':"key_k" ,
        "l":"key_l" ,
        "z":"key_z" ,
        "x":"key_x" ,
        "c":"key_c" ,
        "v":"key_v" ,
        "b":"key_b" ,
        "n":"key_n" ,
        "m":"key_m",
        " ": "key_space"

        }
        abc_tap ={
        "key_q": [(78,2179)],
        "key_w": [(224,2179)],
        "key_e": [(359,2179)],
        "key_r": [(504,2179)],
        "key_t": [(650,2179)],
        "key_y": [(790,2179)],
        "key_u": [(940,2179)],
        "key_i": [(1087,2179)],
        "key_o": [(1227,2179)],
        "key_p": [(1367,2179)],
        "key_a": [(140,2403)],
        "key_s": [(286,2403)],
        "key_d": [(430,2403)],
        "key_f": [(577,2403)],
        "key_g": [(717,2403)],
        "key_h": [(857,2403)],
        "key_j": [(1014,2403)],
        "key_k": [(1148,2403)],
        "key_l": [(1300,2403)],
        "key_z": [(291,2616)],
        "key_x": [(443,2616)],
        "key_c": [(577,2616)],
        "key_b": [(868,2616)],
        "key_n": [(1008,2616)],
        "key_m": [(1160,2616)],
        "key_space":[(728,2823)]
        }
        text = text.lower()
        text  = list(text)
        print(text)
        for i in range(len(text)):
            print(text[i])

            letter = abc_file[text[i]]
            print(str(letter))
            print(abc_tap[letter])
            driver.tap(abc_tap[str(letter)])
if __name__ == '__main__':
    x = TextInput()