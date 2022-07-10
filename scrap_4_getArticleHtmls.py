import numpy as np
import requests
from bs4 import BeautifulSoup as bs
import re

# 0. arr2_artIdxUrl 불러오기
arr3_artIdxUrl = np.loadtxt('arr3_artIdxUrl.txt', dtype='str').tolist()

# 1.getArticleHtml
import time
SLEEPTIME = 0.5  
arr4_artHtmls = []

def getArtHtml(url):
    time.sleep(SLEEPTIME)
    print('GET LOG: ',url)
    return requests.get(url)

arr4_artHtmls = list(map(getArtHtml,arr3_artIdxUrl))

print(arr4_artHtmls)
print(type(arr4_artHtmls))
print(type(arr4_artHtmls[0]))

# 2.save
np.savetxt('arr4_artHtmls.txt',arr4_artHtmls,fmt='%s')


