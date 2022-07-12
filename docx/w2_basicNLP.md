# 1주차 TASK2 : 기초 텍스트 정제 (22.07.11)
1주차 예정 작업인 기초 텍스트 정제 수행 <br>
이전 작업물인 구조적으로 저장된 스크래핑 결과물 [arr4_objs.npy 관련 파일](https://github.com/ABizCho/SMA_2022summerProject/blob/main/scrap_4_getArticleHtmls.py) 를 불러와 기초 텍스트 전처리를  수행했음.

<br>

주요 Libraries : 
- pandas : 데이터프레임 관련
- re : 정규식 관련 라이브러리

<br>

관련작업물 : 
- [nlp_1_cleanMeta](https://github.com/ABizCho/SMA_2022summerProject/blob/main/nlp_1_cleanMeta.py)
- [nlp_2_cleanEtc](https://github.com/ABizCho/SMA_2022summerProject/blob/main/nlp_2_cleanEtc.py)

<br>

특이 사항 : 
- array[dictionary..]로 구조화하여 저장했던 파일을 nlp 첫과정에서 dataframe으로 옮겨 저장했음
- 'comments' column에는 복수의 댓글이 저장되어있을 수 있으며, 이는 띄어쓰기 21개를 기준으로 구분되어있음.
- 'comments'가 null인 경우 0으로 저장했음

<br><br>

## 1. 기초 정제 작업을 마친 DataSet 정보
- records 수 : 15373
- columns :
    1. `art_id` : 게시글의 식별자 (int)
    2. `art_date_year` : 게시 연도 (int)
    3. `art_date_month` : 게시 월 (int)
    4. `art_date_day` : 게시 일자 (int)
    5. `art_date_hour` : 게시 시간 (int)
    6. `user_score` : 작성자의 활동점수 (str)
    7. `art_Ncomment` : 게시글에 달린 댓글 수 (int)
    8. `art_Nview` : 게시글의 조회수 (int)
    9. `art_Nlike` : 게시글이 받은 공감 수  (int)
    10. `art_title` : 게시글 제목  (str)
    11. `art_content` : 게시글 본문 (str)
    12. `art_comments` : 게시글에 소속된 댓글 모음 (str), 띄어쓰기x21개로 댓글 구분


<br><br><br>

## 2. 기초 텍스트 전처리 Process
기초 텍스트 전처리는 전처리 대상에 따라 총 두개의 파일로 수행됐음 

1. [nlp_1_cleanMeta](https://github.com/ABizCho/SMA_2022summerProject/blob/main/nlp_1_cleanMeta.py): 게시글 comment가 담긴 컬럼의 string 값들 전체를 대상으로, html 태그가 표현된 문자열 혹은 개행문자 등의 메타 문자, 문자열을 대상으로 제거 및 저장하는 전처리를 실시했음
    - 산출물: [df2_arts_cleanMeta.csv](https://github.com/ABizCho/SMA_2022summerProject/blob/main/df2_arts_cleanMeta.csv)
<br><br>

2. [nlp_2_cleanEtc](https://github.com/ABizCho/SMA_2022summerProject/blob/main/nlp_2_cleanEtc.py): 
게시글 title, comment, column이 담긴 string 값들 전체를 대상으로, E-mail, Url, 단일로 존재하는 한글 자음/모음, 구두점 및 특수문자, 이모지 를 제거하여 저장하는 전처리를 실시했음.
    - 산출물 : [df3_arts_cleanEtc.csv](https://github.com/ABizCho/SMA_2022summerProject/blob/79bdc0a0c1064c779a7a9b67b52f659cb733b568/df3_artsCleanEtc.csv)
