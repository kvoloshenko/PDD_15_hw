import requests
from bs4 import BeautifulSoup
from bs4 import Comment
import json

def data_save_txt(data, file):
    with open(file, 'w', encoding='utf8') as f:
        f.write(data)

def data_save_json(data, file):
    with open(file, 'w', encoding='utf8') as f:
        json.dump(data, f)

domain = 'https://saint-petersburg.ru'
url = f'{domain}/s/coronavirus/40/'
print(f'url={url}')

response = requests.get(url)
print(f'response.status_code={str(response)}')

# Создаем soap для разбора html
soup_base = BeautifulSoup(response.text, 'html.parser')

big_body_div = soup_base.find('div', class_='col-left-920px')
# print(big_body_div)
data_save_txt(str(big_body_div),'big_body_div.xml')
parsed_data = []
top_item_header = big_body_div.find('h1', itemprop='name').text
item = {}
# print(f'top_item_header{top_item_header}')
item['item_header']=top_item_header
top_item_url = url
# print(f'top_item_url={top_item_url}')
item['url'] = top_item_url
top_item_data = big_body_div.find('div', class_='article-data-orange').text
# print(f'top_item_data={top_item_data}')
item['date']=top_item_data
# print(f'item={item}')
parsed_data.append(item)
print(f'parsed_data={parsed_data}')


soup_news = BeautifulSoup(str(big_body_div), 'html.parser')
ul_news = soup_news.find_all('ul', class_='item-newslist')
data_save_txt(str(ul_news),'ul_news.xml')

for item in ul_news:
    item_n = {}
    # print(type(item), f'item={item}')
    item_url = f'{domain}{item.a.get("href")}'
    # print(f'item_url={item_url}')
    item_header = item.span.text
    # print(f'item_header={item_header}')
    soup_item = BeautifulSoup(str(item), 'html.parser')
    item_n['item_header'] = item_header
    item_n['url'] = item_url
    for comments in soup_item.findAll(text=lambda text: isinstance(text, Comment)):
        html_comment = comments.extract()
        # print(type(html_comment),str(html_comment))
        soap_data = BeautifulSoup(str(html_comment), 'html.parser')
        item_data = soap_data.li.text
        # print(f'item_data={item_data}')
        item_n['date'] = item_data
    parsed_data.append(item_n)
print(f'parsed_data={parsed_data}')
data_save_json(parsed_data,'parsed_data.json')
