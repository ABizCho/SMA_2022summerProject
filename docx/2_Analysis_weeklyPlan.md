# SMA 프로젝트 주차 별 계획서

주제: ‘동시 출현 네트워크 분석 및 토픽 모델링을 활용한 국내 개발 취업 준비생과 현업자의 경험과 고충 분석: 온라인 커뮤니티 게시글을 중심으로.’
<br>

## Weekly Plan
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
