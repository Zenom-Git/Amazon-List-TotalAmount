import json
import time
import os
import requests
from bs4 import BeautifulSoup

import colorama
from colorama import Fore

colorama.init(autoreset=True)
os.system(
    "TITLE 欲しいものリスト合計算出")

def san():
    print('')
    print(Fore.LIGHTGREEN_EX+'URLを貼り付けてください。'+Fore.LIGHTYELLOW_EX+'(値段表記のあるものしかカウントされません)')
    url = input(Fore.LIGHTGREEN_EX+'>> '+Fore.RESET)
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        price = soup.find_all("span", class_="a-price-whole")

        print(Fore.CYAN+f"{len(price)} 個の商品が見つかりました")
        print('')
        loop = False
        counter = 1
        ret = []
        for t in price:
            ret.append(t.text)
            list = [item.replace(',', '') for item in ret]
        for i in range(len(ret)):
            print(i, ret[i]+'円')

        list2 = [int(s) for s in list]
        print('')
        print(Fore.LIGHTGREEN_EX+f'●合計: {sum(list2)} 円')
        time.sleep(3)
        print('')
        san()
    except:
        print(Fore.YELLOW+'URLが間違っています。')
        time.sleep(2)
        print(Fore.YELLOW+'正しいURLを入力してください。')
        print('')
        san()
san()
