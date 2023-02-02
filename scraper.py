# python web crawler for cryptocurrencies

from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

url = 'https://www.binance.com/en/markets'
page = requests.get(url)
page.raise_for_status()

crypto = []
i = 0
soup = BeautifulSoup(page.text, 'html.parser')

names_source = soup.findAll('div', 'css-1ap5wc6')
value_source = soup.findAll('div', ['css-1ez6tx0', 'css-li1e6c', 'css-ovtrou'])

for name in names_source:
    tmp_name = re.sub("<div class=\"css-1ap5wc6\" data-bn-type=\"text\">","", str(name))
    curr_name = re.sub("</div>","", tmp_name)
    
    tmp_value = re.sub("<div class=\"css-\w+\" data-bn-type=\"text\" style=\"direction:ltr\">", "", str(value_source[i]))
    curr_value = re.sub("</div>", "", str(tmp_value))

    crypto.append({'currency': curr_name, 'value': curr_value})
    i += 1

s = pd.DataFrame(crypto)
print(s)