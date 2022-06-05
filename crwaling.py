#from selenium import webdriver
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.parse import quote_plus
import requests
"""
#driver = webdriver.Chrome()
baseUrl = "https://purme.org/archives/47309"
url = baseUrl
html = urlopen(url)
soup = bs(html, "html.parser")
img = soup.find_all(class_='img',limit = 2)

n = 1
for i in img: # 이미지를 50개 저장하기 위한 반복문
    imgUrl = i['data-source'] 
    with urlopen(imgUrl) as f:
        with open('C:\Python39\img' + url + str(n)+'.jpg','wb') as h: # 이미지 + 사진번호 + 확장자는 jpg
            img = f.read() #이미지 읽기
            h.write(img) # 이미지 저장
    n += 1
print('다운로드 완료')"""

import csv
import requests
import time
from bs4 import BeautifulSoup

def blog_crawling(page=1):
    url = "https://search.naver.com/search.naver?query=%ED%99%8D%EB%8C%80%20%EA%B0%9C%EB%AF%B8&nso=&where=blog&sm=tab_opt".format(page)
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    blog_post_list = []
    
    for links in soup.select('li.list-item > dl'):
        title = links.select('dt > a')
        content = links.select('dd.sh_blog_passage')
        author = links.select('dd.txt_block a')

        title = title[0].get('title')

        content = content[0].text

        author = author[0].text

        blog_post = {'author': author, 'title': title, 'content': content}

        blog_post_list.append(blog_post)

    return blog_post_list

def save_data(blog_post):
    keys = blog_post[0].keys()
    with open('blog_crawling.csv', 'w') as file:
        writer = csv.DictWriter(file, keys)
        writer.writeheader()
        writer.writerows(blog_post)

blog_post_list = []
for i in range(1, 100, 10):
    blog_post_list.extend( blog_crawling(page=i) )
    time.sleep(2)

save_data(blog_post_list)

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import urllib.parse


# 네이버 검색 후 검색 결과
baseUrl = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='
plusUrl = input('검색어를 입력하세요 : ')
# 한글 검색 자동 변환
url = baseUrl + urllib.parse.quote_plus(plusUrl)
html = urlopen(url)
bsObject = bs(html, "html.parser")

# 조건에 맞는 파일을 다 출력해라
title = bsObject.find_all(class_='total_info')


for i in title:
    print(i.attrs['title'])
    print(i.attrs['href'])
    print()