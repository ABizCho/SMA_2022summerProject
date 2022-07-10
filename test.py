a = [1,2,3]
print(*a) # Array Spread Literals

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