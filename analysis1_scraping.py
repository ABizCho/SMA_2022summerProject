'''
Analysis 1 - web scraping

    방법 선정 : 'scrapy' vs 'selenium' vs 'BeautifulSoup'

    추가 라이브러리 : requests(HTTP 요청(메시지)를 보낼 수 있는 기능을 제공)
'''

import requests
from bs4 import BeautifulSoup as bs


page = requests.get("https://okky.kr/articles/life?offset=51&max=24&sort=id&order=desc")


soup = bs(page.text, "html.parser") # bs객체 인스턴스 생성-할당 / bs의 첫번째 파라미터는 파싱할 대상을 지정 (page라는 객체 그자체 혹은 자식요소 지정가능)

    # 한페이지 내 태그 긁어오기
        # CSS 셀렉터 : https://developer.mozilla.org/ko/docs/Web/CSS/CSS_Selectors
elements = str(soup.select('.article-id'))

    # str 배열로 나누기
import re
arr_numTag = re.sub('<.+?>', '', elements, 0).split(sep=' ')
print(arr_numTag)

    # 배열 아이템s 전처리
for i in range(len(arr_numTag)) :
    arr_numTag[i] = arr_numTag[i].strip('[').strip('#').strip(',').strip(']') # 태그 제외

    # article방문, pages가져오기
# artTitle = bs(requests.get('https://okky.kr/article/'+ arr_numTag[0]).text, 'html.parser').select('.panel-title')
arr_htmls = []  #html pages 저장
for i in range(len(arr_numTag)) :
    arr_htmls.append(bs(requests.get('https://okky.kr/article/'+ arr_numTag[i]).text, 'html.parser'))

    # htmls에서 title 추출
arr_titles = []
for i in range(len(arr_htmls)):
    arr_titles.append(arr_htmls[i].find('h2',{'class': 'panel-title'}).text)
print(arr_titles)

    
### 저장하기

    #https://aruymeek.tistory.com/7
    
    #https://velog.io/@banana/46.3-%EC%9B%B9-%ED%8E%98%EC%9D%B4%EC%A7%80%EC%9D%98-HTML%EC%9D%84-%EA%B0%80%EC%A0%B8%EC%99%80%EC%84%9C-%ED%8C%8C%EC%9D%BC%EB%A1%9C-%EC%A0%80%EC%9E%A5%ED%95%98%EA%B8%B0