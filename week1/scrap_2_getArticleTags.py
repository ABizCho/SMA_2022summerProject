import numpy as np
import requests
from bs4 import BeautifulSoup as bs
import re

# 0. arr1_pageIdxUrl 불러오기
arr1_pageIdxUrl = np.loadtxt('arr1_pageIdxUrl.txt', dtype='str').tolist()
print(arr1_pageIdxUrl)

#
import time
SLEEPTIME = 0.5   # 1초당 2개 = 0.5초당 1개
arr_htmls_forTags = []

def getHtml(url):
    time.sleep(SLEEPTIME)
    print('GET LOG: ',url)
    return requests.get(url)

arr_htmls_forTags = list(map(getHtml,arr1_pageIdxUrl))
    
# 1. pageIdxUrl으로부터 Tags 가져와서 배열 구성
arr2_artTags = []
for i in range(len(arr_htmls_forTags)) :
    # page = requests.get(arr1_pageIdxUrl[i])
    soup = bs(arr_htmls_forTags[i].text, 'html.parser')
    elements = str(soup.select('.article-id'))
    
    arr_numTag = re.sub('<.+?>', '', elements, 0).split(sep=' ')
    
    arr_numTag = arr_numTag[2:] # 광고글 제거 : 배열상 앞의 두개 요소 제거
    
    for i in range(len(arr_numTag)) :
        arr_numTag[i] = arr_numTag[i].strip('[').strip('#').strip(',').strip(']') #태그제외
        
    arr2_artTags.extend(arr_numTag)
    

print(arr2_artTags)
print(type(arr2_artTags))
print(type(arr2_artTags[0]))

# 저장 로직 짜세요
np.savetxt('arr2_artTags.txt',arr2_artTags, fmt='%s')
