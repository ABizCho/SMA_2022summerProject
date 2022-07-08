'''
Analysis 1 - web scraping

    방법 선정 : 'scrapy' vs 'selenium' vs 'BeautifulSoup'

    추가 라이브러리 : requests(HTTP 요청(메시지)를 보낼 수 있는 기능을 제공)
'''

import requests
from bs4 import BeautifulSoup as bs

page = requests.get("https://okky.kr/articles/life?offset=51&max=24&sort=id&order=desc")
soup = bs(page.text, "html.parser") # bs객체 인스턴스 생성-할당 / bs의 첫번째 파라미터는 파싱할 대상을 지정 (page라는 객체 그자체 혹은 자식요소 지정가능)

# CSS 셀렉터 : https://developer.mozilla.org/ko/docs/Web/CSS/CSS_Selectors
element = str(soup.select('.article-id'))

import re 
resTag = re.sub('<.+?>', '', element, 0).strip()) # 태그 제외

# article방문, 제목 가져오기
artUrl = bs(requests.get('https://okky.kr/articles/'+ resTag).text, 'html.parser').select('.panel-title')
    

# ###############
# # 1. 사는얘기 탭 페이지 방문하여 태그 담는 배열 만들기
# #     페이지 0으로 시작 24씩 증가하며 한페이지씩 넘어감
#         # [1] https://okky.kr/articles/life?offset=0&max=24&sort=id&order=desc
#         # [2] https://okky.kr/articles/life?offset=24&max=24&sort=id&order=desc
# url_txt = 'https://okky.kr/articles/life?offest='


#     # 1.1 10페이지짜리 url담긴 배열 만들기
# urlArr = []
# for i in range(10) : 
#     # print(url_txt + str(i*24))
#     urlArr.append(url_txt + str(i*24))
# # print(urlArr)

#     #+ 페이지 가져오기
# arr_pages = []
# def getPages(url) :
#     return requests.get(url)
# arr_pages = list(map(getPages,urlArr))
# print(arr_pages)

# #     # 1.2 urlArr 페이지의 모든 태그 긁어서 배열에 '게시글URL'로 저장
# arr_soups = []
# def getSoups(page) :
#     return bs(page.text, 'html.parser').select('.article-id')
# arr_soups = list(map(getSoups,urlArr))

# print(arr_soups)
# arr_result = []

# list(map(,urlArr))
# for i in range(len(urlArr)) :
#     currPage = requests.get('urlArr')
#     url_txt
    
    
    # 1.3 각 arr_url_tag의 제목 긁어오기 테스트


# for index, element in enumerate(elements, 1):
# 		print("{} 번째 게시글의 제목: {}".format(index, element.text))