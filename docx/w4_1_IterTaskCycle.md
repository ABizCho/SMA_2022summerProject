# 1회성 작업 결과물
1. week1 / df3_2_artsCleanEtc.csv
2. week2 / ...

# 반복되는 Task Cycle 및 Outputs 투입 및 산출 순서 정리

## week3


### T1: mecab 사용자 정의 사전 단어 추가

   1. `T1_mecab_setUserDict1_1nnp.py & .._2etc.py` : 사용자 정의 Token 설정

   2. `PowerShell console / in mecab dir path / $ 사용자 정의 사전 컴파일링 커맨드`
   3. `T1_mecab_setUserDictt2_afterPr.py` : 사전 컴파일 이후, 파일 내 형태소 판별 우선순위값 재조정 및 저장

<br><br>

### T2: mecab 수행 및 복합명사 처리 로직 개선

   - TaskFile : `T2_mecab_comp_n_xxx.ipynb`
   - input : `week1 / df3_2_artCleanEtc.csv`
   - output : `week3 / df0_n_res_totalComps_xxx.csv`

<br><br>

## week4

### T1: week3의 복합명사화 결과물을 cleaning
- TaskFile: `T1_compound-to-NounDf.ipynb`

- input: `week3 / df0_n_res_totalComps_xxx.csv`
  
- output: `week4 / T1_df_cleaned_noun_xxx.csv`
  
- 처리내용
   1. 명사 혹은 복합명사화 된 TOKEN들만을 추출 재구성
   2. SL(영단어)타입 토큰 중 대문자 포함 token을 인식 및 소문자 통일작업
   3. 길이가 1인 token 제거

<br><br>

### T2: 개선된 Nouns Dataframe을 바탕으로 DTM 재구성
- TaskFile: `T2_DTM.ipynb`

- input:` week4 / T1_df_cleaned_noun_xxx.csv`

- output: ` week4 / T2_DTM_xxx.csv`

<br><br>

### T3: NetworkX를 이용해 개선된 동시출현키워드 결과물 확인 
해당 결과물을 바탕으로 개선점 추가 확인 및 앞의 PROCESS 선택적 반복 진행중

<br>

- TaskFile : `T3_DTM_to_Netword.ipynb`
