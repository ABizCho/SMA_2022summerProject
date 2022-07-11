# SMA_2022summerProject
<img src='https://biz.ajou.ac.kr/_res/ajou/biz/img/intro/img-bi01.png' width=300/>

Ajou e-Business 강민형 교수님 지도하의  SMA Summer Project 2022에 선발된 '동시 출현 네트워크 분석 및 토픽 모델링을 활용한 국내 개발 취업 준비생과 현업자의 경험과 고충 분석: 온라인 커뮤니티 게시글을 중심으로’ 주제의 학부 연구를 수행 및 기록합니다.

<br><br><br><br>

---

<br><br>

## 1주차 'OKKY' Scrapping (22.07.10)
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

### 1. 스크래핑을 위한 서비스 구조 분석
[Okky의 사는얘기](https://okky.kr/articles/life?offset=0&max=24&sort=id&order=desc)를 참고해 보면, 한 게시글 목록 페이지 내에 게시글을 24개 정렬하며, 그중 첫번째 두개의 게시글은 OKKY의 자체 광고 게시글임.
<br><br>
게시글 목록 페이지를 보면 게시글 제목 옆마다 `#article id`가 게시글의 식별자로 달려있으며, 개별 게시글은 'okky.kr/article/`articleId`의 모습으로 식별자를 끝에 붙여 접근이 가능한 구조임.
<br><br>
게시글목록 페이지는 `(https://okky.kr/articles/life?offset=24)`이와 같은 url로 구성되며, offset에 들어갈 값을 0부터 시작하여, 한 게시글페이지 내 담기는 게시글 수인 숫자 24씩 증가시키며 다음 게시글 목록 페이지로 이동 가능함.
<br><br>

따라서 아래와 같은 순차적 작업을 기획 및 수행했음
<br><br>

### 2. 스크래핑 Process
스크래핑 과정을 핵심 기능단위 기준으로 총 네개의 로직으로 분할 및 수행했으며 각 로직(파일)은 다음 단계를 위한 특정 산출물을 반환함

1. [createPageIdxUrls](https://github.com/ABizCho/SMA_2022summerProject/blob/main/scrap_1_createPageIdxUrls.py): 게시글 목록에 접근하기 위한 url 배열 생성(24증가 기준)
    - 산출물: [게시글목록 URLs](https://github.com/ABizCho/SMA_2022summerProject/blob/main/arr1_pageIdxUrl.txt)
<br><br>

1. [getArticleTags](https://github.com/ABizCho/SMA_2022summerProject/blob/main/scrap_2_getArticleTags.py): 하나의 게시글 목록에서 22개씩의 `article id(tag)`를 가져오는 로직을 총 658페이지의 게시글에 대해 수행하여 배열에 저장, 해당 작업은 str 전처리 작업을 포함
    - 산출물: [Article IDs](https://github.com/ABizCho/SMA_2022summerProject/blob/main/arr2_artTags.txt)
<br><br>

1.  [createArticleUrls](https://github.com/ABizCho/SMA_2022summerProject/blob/main/scrap_3_createArticleUrls.py): 직전 작업 산출물인 artTags를 활용, 개별 게시글 페이지에 접근하기 위한 url을 생성
    - 산출물: [Article URLs](https://github.com/ABizCho/SMA_2022summerProject/blob/main/arr3_artIdxUrl.txt)
<br><br>

1. [getArticleHtmls](https://github.com/ABizCho/SMA_2022summerProject/blob/main/scrap_4_getArticleHtmls.py):  직전 작업 산출물인 artIdxUrl을 활용, 개별 타겟 게시글 페이지의 html파일을 요청 및 배열의 item으로 저장
    - 산출물 : [Objects Array](https://github.com/ABizCho/SMA_2022summerProject/blob/main/arr_objs.npy)
<br><br>





<br><br>

---

<br><br>

## SMA 2022 SUMMER PROJECT 연구주제 신청서 (2022.06.25)

### 1.데이터 수집 사이트: <br>
국내 개발자 커뮤니티 OKKY - '사는얘기 탭' 게시물들

### 2.분석주제: 
*‘동시 출현 네트워크 분석 및 토픽 모델링을 활용한 국내 개발 취업 준비생과 현업자의 경험과 고충 분석: 온라인 커뮤니티 게시글을 중심으로.’*
<br><br>
코로나 사태로 기업들의 내부 디지털 역량 강화 및 디지털 전환 요구가 가속화되며 근 몇 년, 국내 산업계는 IT인력 충원을 위해 개발 인력 확보에 총력을 다하는 모습이 연출되었다. 기업과 중앙 및 각 지자체 등은 산업의 요구와 인력 수요에 발맞춰 K-Digital Training 혹은 그와 유사한 부트캠프 등을 통해 다방면으로 IT 인재육성에 만전을 기하고 있다. 국내 언론은 앞다투어 IT 산업의 대우를 일면에 내걸며 IT업계로의 인력 진입을 다소 무책임하게 과열시켜왔다. 현재 금리인상이 지속되는 냉혹한 현실에서 스타트업 및 IT서비스 업계에 대한 평가와 투자거품은 차갑고 빠르게 꺼지고 있지만 장밋빛 미래를 꿈꾸는 수많은 청년들이 취업에 당면하거나 필드에 나가 마주할 현실을 일러줄 객관적 자료가 터무니없이 부족하다. 본 연구는 국내 취준생 혹은 개발자들이 이용하는 일개의 온라인 커뮤니티 게시글에서 추출한 텍스트를 기반으로 ‘동시 출현 네트워크’와 ‘토픽 모델’을 구성하여 취준생과 현업자들의 경험과 고충을 탐색하는 계량적 내용 분석 연구가 될 것이다. 해당 연구 결과는 IT업계의 취준 및 현업의 현실을 알리는 다소 객관적인 근거자료가 될 수 있으며, 실제 개발업계의 취업준비생과 현업자들의 고충을 반영해야 할 기업의 사내문화 개선 담당자 혹은 각 정부의 정책 담당자를 위한 새로운 아이디어와 정책 근거를 마련할 수 있을 것으로 기대한다. 
<br><br>


### 3.수집 데이터 내용
수집 데이터는 국내에서 활성화된 개발자 커뮤니티인 ‘OKKY’의 ‘사는얘기’(https://okky.kr/articles/life) 탭의 게시물 중 약 6개월-2년 사이의 제목, 내용이 될 것입니다.
<br><br>

### 4.데이터 수집 방법(계획)
OKKY는 공식 API를 지원하지 않기 때문에 Python의 Selenium, BeautifulSoup을 사용해 웹 스크래핑을 이용한 텍스트 데이터 추출을 진행할 것입니다. 현재 25일 기준으로 OKKY 운영팀에게 협조 메일을 보냈으며 추후 불허 응답 시, 허락해주신다면 연구 사이트 재선정 혹은 주제를 빠르게 수정하여 연구에 임하도록 하겠습니다. 연구윤리를 고려하여 개인 게시자를 식별할 수 있는 id, 이름, 관련 내용은 수집하지 않고 수집 이후 적절한 검토를 거쳐 확인 시 삭제할 예정입니다.
<br><br>
### 5.데이터 분석 방법(계획)
수집된 텍스트 데이터는 토큰화와하여 명사만을 추출하여 이후, ‘다빈도 키워드 추출’, ‘동시출현 네트워크 분석’, 그리고 ‘토픽 모델링 텍스트 마이닝 기법’을 적용하는 분석을 진행할 예정입니다.

<br>

---

<br>

## SMA 프로젝트 Tasks 및 Process 정리 (2022.06.28)
<br>

주제 : 
<br>‘동시 출현 네트워크 분석 및 토픽 모델링을 활용한 국내 개발 취업 준비생과 현업자의 경험과 고충 분석: 온라인 커뮤니티 게시글을 중심으로.’

<br>

연구진행절차: 
1.	**웹 스크래핑(텍스트 데이터 추출)**
    - 가.	스크래핑 방법 선정: Selenium / BeautifulSoup | html 파일로? / 요소로?
        - a.	Selenium or BeautifulSoup 비교 및 선정
        - b.	요소로 수집 or html파일로 수집 선정 <br><br>
    - 나.	추출 게시글 기간 설정: 2019 – 2022 (테스트로 2022 우선)
    - 다.	수집 데이터 요소: 게시글 내용 & 연도/월 (윤리적 고려로 식별자 제거) <br><br>
2.	**텍스트 정제**
    - 가.	추출: ‘명사’, 한국어 특성 상 키워드 뒤 조사가 함께 쓰이는 경우가 많고 어미의 변화가 다양하여 품사를 기준으로 키워드를 구분하는 방법이 적절하기 때문
    - 나.	명사 추출을 위한 숫자 및 구두점 제외
    - 다.	Tokenization: 형태소 분석기 이용 품사 구분
        - a.	형태소 분석 시, 정제되지 않은 커뮤니티 언어 특성 고려하여 결과 확인: 은어, 약어, 전문용어 로 인해 형태소 분석 결과가 부정확 할 가능성 존재
            - ->	해당 현상 발생 시, 어절 단위의 자료 분리 후 직접 독립적인 ‘키워드 전처리’를 통해 명사를 추출 (Ex. 국비 => 국비지원학원 등 정식명칭 수정, 다양하게 표현되는 동일 의미 키워드는 1개의 정식 키워드로 통일)<br>

        - b.	복합명사의 경우, Bi-gram 분석을 통해 연달아 함께 쓰이는 키워드를 확인하고 복합명사 형태로 수정하는 케이스도 고려
  
    - 라.	취준생과 현업자 파티션 방법 고안: 현업 및 취준 별 특정 키워드 선정 후, 특정 키워드 포함 시 카테고리에 편입하는 방법으로
    - 마.	불용어 사전 구축 및 무의미 키워드 추가, 수정
        - a.	한글 불용어 사전 조사 및 적용검토
        - b.	나, 너, 우리 등 인칭 대명사 등 무의미 키워드 제거
        - c.	오늘, 요즘, 정도 등의 분석 상 특별한 의미 전환이 없는 키워드 제거
        - d.	출현 빈도가 타 키워드에 비해 과하게 높은 경우 공통 키워드로 판단하여 불용어 등록 필요 (ex.컴퓨터..) <br><br>
3.	**분석 & 시각화**
    - 가.	다빈도 키워드 분석 & 워드 클라우드
    - 나.	동시 출현 네트워크 분석: 동시 출현 키워드 간 상관관계 확인 목적
        - a. 빈도에 따라 link(edge)의 굵기 등 다르게 표현하는 시각화 방법 요구
        - b. 모든 키워드 대상 네트워크 분석 시 과다한 연결관계 형성으로 시각적 분별성 떨어지므로, 연결관계의 횟수(차수)를 기준으로 분석 키워드 범위를 제한할 필요가 있음 
          - 분석 포함 노드 범위를 결정할 필요가 있음(탐색적으로)<br><br>
    - 다.	토픽 모델링 (LDA, Latent Dirichlet Allocation 알고리즘 사용)
        - a.	빈도 파악을 위해 이미 전처리 완료된 Dataset을 DTM 구조로 변환(문서-용어 행렬)
            - -> DTM(Documet-Term Matrix)는 행에 Document(문서), 열에 Term(키워드)가 배치된 행렬 구조. 본 연구에서 행에 들어갈 문서가 게시글이 될지 무엇이 될지는 ‘1-가’의 선택에 의존적
        - b.	문서에 속한 키워드를 LDA 함수를 통해 토픽 별로 분류
        	- 토픽의 개수는 추정에 따라 정함, 개수의 근거 정당화 과정 필요
            - 토픽 개수 조정 별 분석결과 비교를 통해 경계가 가장 명확한 개수로 결정(탐색적 결정과정)
        - c.	키워드가 해당 토픽에 속할 확률인 beta값 계산
        - d.	모델 평가를 위한 토픽 개수에 따른 복잡성(perplexity) 수준 분석
            - 	복잡성은 적합성 수준 평가지표
            -	낮을수록 모델 적합성이 높다.
            -	토픽 개수와 설명력은 비례하며, 토픽개수와 복잡성 수준은 반비례한다.
            -	해석 가능한 토픽 개수 범위 내에서 복잡성 수준이 완만하게 감소하는 구간 결정(막대그래프 시각화를 통해 가능)

<br><br>

---

<br>

## Weekly Plan 주차별 연구 계획 (2022.07.03)
<br>

**1주차 07.04 ~ 07.10**

-1. 데이터 수집
- 가.	BeautifulSoup를 이용한 데이터 수집 및 저장: https://okky.kr/articles/life
    -	제목 / 내용

-2. 기초 텍스트 정제 
<br>

- 가. 명사 추출을 위한 숫자 및 구두점 제외 등 전처리
	가. 불필요 개인정보 제거 전처리
	나. KoNLPy 패키지를 이용한 형태소 분석, Tokenization
Ref : https://datascienceschool.net/03%20machine%20learning/03.01.02%20KoNLPy%20%ED%95%9C%EA%B5%AD%EC%96%B4%20%EC%B2%98%EB%A6%AC%20%ED%8C%A8%ED%82%A4%EC%A7%80.html
	다. 불용어 사전 선정 및 불용어 키워드 추가, 제거
<br><br>

**2주차 07.11 ~ 07.17**

-1.	기초 텍스트 정제 연장 작업 마무리

-2.	텍스트 정제
- 가.	커뮤니티 특성을 고려한 은어, 줄임말, 전문용어 처리
A.	Bi-gram 분석을 통해 연달아 사용되는 키워드 확인 및 복합명사 형태로 수정
B.	은어, 줄임말, 전문용어 키워드 통일 전처리 => ex. 국비 -> 국비지원학원
<br>

- 나.	무의미 키워드 추가적 제거 작업
<br><br>

**3주차 07.18 ~ 07.24**

-1.	다빈도 키워드 분석 & 워드 클라우드 

-2.	동시 출현 네트워크 분석: 동시 출현 키워드 간 상관관계 확인 목적
<br>

- 가.	시각적 분별력을 제고하기 위한, edge간 Degree(연결횟수)를 기준으로 Node(키워드)포함 범위를 탐색적으로 결정
<br><br>

**4주차 07.25 ~ 07.31**

-1. 토픽 모델링 기획 

- 가. 사용 알고리즘 선정: 아마 LDA
<br>

- 나. 토픽의 개수 결정 방법 및 기준, 근거 마련
<br>

- 다. 모델 평가 방법 마련
<br>

-2. 토픽 모델링 수행의 기반작업인 DTM (Document-Term Matrix) 행렬구조 구축
<br><br>

**5주차 08.01 ~ 08.07** 
1. 토픽 모델링 수행
2. 토픽 모델 평가: 토픽 개수에 따른 복잡성(perplexity) 수준 분석
<br><br>

**6주차 08.08 ~ 08.14** 
1.	토픽 모델 보완 및 개선
2.	토픽 모델 해석
3.	기타 분석 결과 개선 및 보완
<br><br>

**7주차 08.15 ~ 08.21** <br>
보고서 작성
<br><br>

**8주차 08.22 ~ 08.31** <br>
 보고서 작성 등
