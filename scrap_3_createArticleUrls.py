import numpy as np

# 0. arr2_artIdxUrl 불러오기
arr2_artTags = np.loadtxt('arr2_artTags.txt', dtype='str').tolist()

print(arr2_artTags)

def createArticleUrls(PageNum):
    URL = 'https://okky.kr/article/'
    p_url = URL + PageNum
    print('Create LOG',p_url)
    return p_url

arr3_artIdxUrl = list(map(createArticleUrls, arr2_artTags))

np.savetxt('arr3_artIdxUrl.txt', arr3_artIdxUrl, fmt='%s')
