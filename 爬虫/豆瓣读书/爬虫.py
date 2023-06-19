import requests
from lxml import etree
import csv
import re

url3 = 'https://www.douban.com/doulist/152361157/?start=0&sort=time&playable=0&sub_type='
url0 = 'https://www.douban.com/doulist/152361157/?start='
url1 = '&sort=time&playable=0&sub_type='
headers = {
    'User-Agent': 'zilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
urls = []
# 修改爬取的界面的url
for i in range(0, 250, 25):
    url = url0 + str(i) + url1
    urls.append(url)
print('进入爬虫')
out = open('./douban.txt', 'w', encoding='utf-8')
# 爬虫主题
for i in urls:
    webs = requests.get(url=i, headers=headers).text
    # p=r'class="doulist-item"'
    # titles=re.findall(p,webs)
    res = etree.HTML(webs)
    # csv_write=csv.writer(out,dialect='excel')
    for i in range(6, 31):
        post = res.xpath(F'//*[@id="content"]/div/div[1]/div[{i}]/div/div[2]/div[2]/a/img/@src')[0]
        title = res.xpath(F'//*[@id="content"]/div/div[1]/div[{i}]/div/div[2]/div[3]/a/text()')[0].strip()
        rating = res.xpath(F'//*[@id="content"]/div/div[1]/div[{i}]/div/div[2]/div[4]/span[2]/text()')[0].strip()
        # 有的没有作家信息，需要进行判定一下
        if len(res.xpath(F'//*[@id="content"]/div/div[1]/div[{i}]/div/div[2]/div[5]/text()')) == 3:

            abstract1 = res.xpath(F'//*[@id="content"]/div/div[1]/div[{i}]/div/div[2]/div[5]/text()')[0].strip()
            abstract2 = res.xpath(F'//*[@id="content"]/div/div[1]/div[{i}]/div/div[2]/div[5]/text()')[1].strip()
            abstract3 = res.xpath(F'//*[@id="content"]/div/div[1]/div[{i}]/div/div[2]/div[5]/text()')[2].strip()
        else:
            abstract1 = str(0)
            abstract2 = res.xpath(F'//*[@id="content"]/div/div[1]/div[{i}]/div/div[2]/div[5]/text()')[0].strip()
            abstract3 = res.xpath(F'//*[@id="content"]/div/div[1]/div[{i}]/div/div[2]/div[5]/text()')[1].strip()
        # str1=[post,title,rating,abstract1,abstract2,abstract3]
        str1 = str(title + ',' + post + ',' + rating + ',' + abstract1 + ',' + abstract2 + ',' + abstract3)
        out.write(str1 + "\n")
        print(i)
out.close()
