import requests
import pandas as pd
from bs4 import BeautifulSoup
from lxml import etree
import re

url = 'https://www.rockauto.com/en/parts/gsp,cv+axle,2288'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
           'referer': 'https://www.rockauto.com/'}
rsp = requests.get(url=url, headers=headers)
# oe_xpath = '//*[@id="navhref[2]"]/text()'
oe_xpath = '//*[@id="navchildren[1]"]//div//td'
html = etree.HTML(rsp.text)
result = html.xpath(oe_xpath)

urls = []
part_number = []
# 遍历每个元素并获取文本内容
for element in result:
    text_content = ''.join(element.xpath('.//text()')).strip()
    if text_content !='':
        part_number.append(text_content)
        urls.append('https://www.rockauto.com/en/parts/gsp,'+str(text_content)+',cv+axle,2288')
# print(part_number)
# print(urls)