#!python3

import requests, re
from bs4 import BeautifulSoup
import pandas as pd
import io

#download and parse the HTML
startUrl= 'https://en.wikipedia.org/wiki/Tesla,_Inc.'

regex = re.compile('_\[\w\]')

#download the html from start_url

downloaded_html = requests.get(startUrl)

#parse the html with beautifulsoup and create a soup object

soup = BeautifulSoup(downloaded_html.text, 'html.parser')

#save a local copy

with io.open('downloaded.html', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())

full_table = soup.select('table.wikitable')[0]


table_head = full_table.select('tr th')

print('-----------')

table_columns = []

for element in table_head:
    column_label = element.get_text(separator = ' ', strip=True)
    column_label = column_label.replace(' ', '_')
    column_label = regex.sub('', column_label)
    table_columns.append(column_label)
print(table_columns)

table_rows = full_table.select('tr')

table_data = []

for index, element in enumerate(table_rows):
    if index > 0:
        row_list = []
        values = element.select('td')
        for value in values:
            row_list.append(value.text)
        table_data.append(row_list)
print(table_data)

