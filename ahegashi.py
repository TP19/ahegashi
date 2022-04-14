#from pykakasi import *

import requests
import pykakasi
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
kakasi = pykakasi.kakasi()
kakasi.setMode("s", True)
kakasi.setMode("J","HF") # Japanese to furigana
kakasi.setMode("H","aF")
text = "猫が好きです！犬も素晴らしいです！ハリネズミ、カワウソ、パンダ！"
conv = kakasi.getConverter()
v1 = conv.do(text)
v2 = kakasi.convert(text)
print(v1)

for item in v2:
    print("{}: \33[94mkana '{}'\33[0m, \33[91mhiragana '{}'\33[0m, \33[92mromaji: '{}'\33[0m".format(item['orig'], item['kana'], item['hira'], item['passport']))

init_api_call = "https://kanjiapi.dev/v1/kanji/"

def split(text):
	return [letter for letter in text]

for i in range(len(split(text))):
    try:
        response = requests.request("GET", init_api_call + str(split(text)[i]))
        if response.ok:
            print(response.json())
        #response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print("")
