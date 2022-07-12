# 1주차 TASK1 : 'OKKY' Scrapping (22.07.10)
1주차 예정 작업인 스크래핑 수행 <br>
국내 개발자 커뮤니티 OKKY - '사는얘기 탭' 게시물 중 [2021.06.22 ~ 2022.07.10] 기간 내 게시글을 타겟으로

<br>

주요 Libraries : 
- beautifulSoup
- requests
- re

<br>

관련작업물 : 
- [scrap_1_createPageIdxUrls](https://github.com/ABizCho/SMA_2022summerProject/blob/main/scrap_1_createPageIdxUrls.py)
- [scrap_2_getArticleTags](https://github.com/ABizCho/SMA_2022summerProject/blob/main/scrap_2_getArticleTags.py)
- [scrap_3_createArticleUrls](https://github.com/ABizCho/SMA_2022summerProject/blob/main/scrap_3_createArticleUrls.py)
- [scrap_4_getArticleHtmls](https://github.com/ABizCho/SMA_2022summerProject/blob/main/scrap_4_getArticleHtmls.py)

<br>

제한사항 : 
1. OKKY 개발 담당자님의 요청으로, 1초당 2개로 html 스크래핑을 제한함.<br> get 관련 작업물에 time.sleep() 메서드를 이용해 0.5초당 1개 스크래핑

2. 오후 5시 ~ 익일 오전 8시 사이의 스크래핑 요청 제한을 지키며 작업,<br> 15000개 article기준 약 3시간 소요

<br><br>

## 1. 스크래핑을 위한 서비스 구조 분석
[Okky의 사는얘기](https://okky.kr/articles/life?offset=0&max=24&sort=id&order=desc)를 참고해 보면, 한 게시글 목록 페이지 내에 게시글을 24개 정렬하며, 그중 첫번째 두개의 게시글은 OKKY의 자체 광고 게시글임.
<br><br>
게시글 목록 페이지를 보면 게시글 제목 옆마다 `#article id`가 게시글의 식별자로 달려있으며, 개별 게시글은 'okky.kr/article/`articleId`의 모습으로 식별자를 끝에 붙여 접근이 가능한 구조임.
<br><br>
게시글목록 페이지는 `(https://okky.kr/articles/life?offset=24)`이와 같은 url로 구성되며, offset에 들어갈 값을 0부터 시작하여, 한 게시글페이지 내 담기는 게시글 수인 숫자 24씩 증가시키며 다음 게시글 목록 페이지로 이동 가능함.
<br><br>

따라서 아래와 같은 순차적 작업을 기획 및 수행했음
<br><br><br>

## 2. 스크래핑 Process
스크래핑 과정을 핵심 기능단위 기준으로 총 네개의 로직으로 분할 및 수행했으며 각 로직(파일)은 다음 단계를 위한 특정 산출물을 반환함

1. [createPageIdxUrls](https://github.com/ABizCho/SMA_2022summerProject/blob/main/scrap_1_createPageIdxUrls.py): 게시글 목록에 접근하기 위한 url 배열 생성(24증가 기준)
    - 산출물: [게시글목록 URLs](https://github.com/ABizCho/SMA_2022summerProject/blob/main/arr1_pageIdxUrl.txt)
<br><br>

2. [getArticleTags](https://github.com/ABizCho/SMA_2022summerProject/blob/main/scrap_2_getArticleTags.py): 하나의 게시글 목록에서 22개씩의 `article id(tag)`를 가져오는 로직을 총 658페이지의 게시글에 대해 수행하여 배열에 저장, 해당 작업은 str 전처리 작업을 포함
    - 산출물: [Article IDs](https://github.com/ABizCho/SMA_2022summerProject/blob/main/arr2_artTags.txt)
<br><br>

3.  [createArticleUrls](https://github.com/ABizCho/SMA_2022summerProject/blob/main/scrap_3_createArticleUrls.py): 직전 작업 산출물인 artTags를 활용, 개별 게시글 페이지에 접근하기 위한 url을 생성
    - 산출물: [Article URLs](https://github.com/ABizCho/SMA_2022summerProject/blob/main/arr3_artIdxUrl.txt)
<br><br>

4. [getArticleHtmls](https://github.com/ABizCho/SMA_2022summerProject/blob/main/scrap_4_getArticleHtmls.py):  직전 작업 산출물인 artIdxUrl을 활용, 개별 타겟 게시글 페이지의 html파일 내 필요한 요소들을 dictionary로 구조화하고 배열의 items로 순차 저장
    - 산출물 : [Article Htmls 처리 코드](https://github.com/ABizCho/SMA_2022summerProject/blob/main/scrap_4_getArticleHtmls.py)

<br>

5. [handleRaw](https://github.com/ABizCho/SMA_2022summerProject/blob/main/scrap_5_handleRaw.py):
getArticleHtmls에서 구조화하여 저장한 array[dict] 데이터셋을 DataFrame으로 옮겨 저장.

    - 산출물 : [df_arts.csv](https://github.com/ABizCho/SMA_2022summerProject/blob/main/df_arts.csv)

<br><br>
