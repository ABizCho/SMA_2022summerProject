def createPageIdxUrls(endPage) :
    endPage -=1
    # 0. page인덱스 생성 : 0 ~ 15000, 24간격 = range(0,15001,24) 
        # 테스트용 : 0 ~ 48, 24간격
    arr_pageIdx = []
    for i in range(0, 24*endPage + 1, 24) :
        arr_pageIdx.append(i)

    # 1. page인덱스 + url 조합 및 저장
    import numpy as np

    arr1_pageIdxUrl = []
    for i in range(len(arr_pageIdx)):
        arr1_pageIdxUrl.append("https://okky.kr/articles/life?offset="+ str(arr_pageIdx[i]))
    np.savetxt('arr1_pageIdxUrl.txt',arr1_pageIdxUrl, fmt='%s')
    
    return arr1_pageIdxUrl


# # 현재 626(= 15000)페이지까지 가목표설정
print(createPageIdxUrls(626))
