''''''
# a = [1,2,3]
# print(*a) # Array Spread Literals


''''''
import numpy as np

import numpy as np
import requests
from bs4 import BeautifulSoup as bs
import re

# 0. arr2_artIdxUrl 불러오기
arr3_artIdxUrl = np.loadtxt('arr3_artIdxUrl.txt', dtype='str').tolist()
arr3 = []

for i in range(2) :
    arr3.append(arr3_artIdxUrl[i])

print(arr3)
# 1.getArticleHtml
import time
SLEEPTIME = 0.5  
arr4_artHtmls = []

def getArtHtml(url):
    time.sleep(SLEEPTIME)
    print('GET LOG: ',url)
    return requests.get(url)

arr4 = list(map(getArtHtml,arr3))


''''''
arrSoup = []
for i in range(len(arr4)):
    arrSoup.append( bs(arr4[i].text, 'html.parser') )

#
arr_objs = []
for i in range(len(arrSoup)):
    # print(arrSoup[i].select_one('.panel-title').text)
    # for j in range(2):
    #     print(arrSoup[i].select('.content-identity-count')[j].get_text())
    
    #comments 파싱/구성 로직
    soup = arrSoup[i]
    arr_commentEls= soup.find_all('article',{'class': 'note-text'})
    arr_comments = []
    for i in range(len(arr_commentEls)):
        arr_comments.append(arr_commentEls[i].get_text())
        
    #Date 파싱/구성 로직
    date = soup.select_one('.timeago').get_text()
    ydm, hms = date.split(' ')
    year, month, day = ydm.split('-')
    hour,min,sec = hms.split(':')
    
    #obj구성로직
    artObj = {'art_id': soup.select_one('.article-id').get_text().strip('#'),
       'art_date_year': year,
       'art_date_month': month,
       'art_date_day': day,
       'art_date_hour':hour,
       'user_score': int(soup.find('div',{'class': 'activity'}).get_text()),
       'art_Ncomment': int(soup.select('.content-identity-count')[0].get_text()),
       'artNview': int(soup.select('.content-identity-count')[1].get_text()),
       'art_Nlike': int(soup.select('.content-eval-count')[0].get_text()),
       'art_title': soup.find('h2',{'class':'panel-title'}).get_text(),
       'art_content': soup.find('article',{'content-text'}).get_text(),
       'comments': arr_comments,
           }
    
    print(artObj)
    arr_objs.append(artObj)
    
np.save('arr_objs',arr_objs)
print(artObj)
