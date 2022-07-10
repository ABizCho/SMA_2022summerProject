import numpy as np
import requests
from bs4 import BeautifulSoup as bs
import re

# 0. arr2_artIdxUrl 불러오기
arr3_artIdxUrl = np.loadtxt('arr3_artIdxUrl.txt', dtype='str').tolist()

# 1.getArticleHtml
import time
SLEEPTIME = 0.1  
arr4_artHtmls = []

def getArtHtml(url):
    time.sleep(SLEEPTIME)
    print('GET LOG: ',url)
    return requests.get(url)

arr4_artHtmls = list(map(getArtHtml,arr3_artIdxUrl))

print(arr4_artHtmls)
print(type(arr4_artHtmls))
print(type(arr4_artHtmls[0]))


''''''
arrSoup = []
for i in range(len(arr4_artHtmls)):
    arrSoup.append( bs(arr4_artHtmls[i].text, 'html.parser') )

# arr_obj구성
arr_objs = []
for i in range(len(arrSoup)):
    #comments 파싱/구성 로직
    soup = arrSoup[i]
    arr_commentEls= soup.find_all('article',{'class': 'note-text'})
    arr_comments = []
    for j in range(len(arr_commentEls)):
        arr_comments.append(arr_commentEls[j].get_text())
        
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
       'user_score': soup.find('div',{'class': 'activity'}).get_text(),
       'art_Ncomment': int(soup.select('.content-identity-count')[0].get_text()),
       'artNview': int(soup.select('.content-identity-count')[1].get_text()),
       'art_Nlike': int(soup.select('.content-eval-count')[0].get_text()),
       'art_title': soup.find('h2',{'class':'panel-title'}).get_text(),
       'art_content': soup.find('article',{'content-text'}).get_text(),
       'comments': arr_comments,
           }
    
    print('OBJ LOG: ', i)
    arr_objs.append(artObj)
    
np.save('arr4_objs',arr_objs)
print('로직종료================')
    
''''''





