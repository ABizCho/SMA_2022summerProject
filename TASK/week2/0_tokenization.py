import pandas as pd

df = pd.read_csv('./outputs/df3_2_artsCleanEtc.csv')

df = df.loc[:10]

'''
Tokenization
'''
# # way1. 어절 단위로 분리
# def word_tokenizer(str):
#     res_arr = str.split(' ')
#     remove_set = {''}
#         # ref: 효율적 제거 : https://latte-is-horse.tistory.com/200
#     res_arr = [i for i in res_arr if i not in remove_set]
#     return res_arr

# print(df['art_title'].map( word_tokenizer ))


# way2. customized konlpy : okt 이용
    # ref : https://github.com/lovit/customized_konlpy 
        # KONLPY 문제해결 : https://velog.io/@soo-im/konlpy-%EC%84%A4%EC%B9%98-%EC%97%90%EB%9F%AC-%ED%95%B4%EA%B2%B0%EC%B1%85-%EC%95%84%EB%82%98%EC%BD%98%EB%8B%A4-JPYPE        
        # https://mr-doosun.tistory.com/22 [고졸 입니다만..:티스토리]

from konlpy.tag import Okt
okt = Okt()

# print(df['art_title'].map(lambda str_title : okt.morphs(str_title, stem=True)))
print(df['art_title'].map(lambda str_title : okt.pos(str_title, norm=True)))



# way3. kiwipiepy 지능형 한국어 형태소 분석기
    # ref : https://bab2min.github.io/kiwipiepy/v0.13.1/kr/



# 1. Bi-gram 분석을 통해 연달아 사용되는 키워드 확인 및 복합명사 형태로 수정
    # ref : https://lovit.github.io/nlp/2018/10/23/ngram/
            # https://velog.io/@hyewon0309/LM-%ED%95%9C%EA%B5%AD%EC%96%B4-Tokenizer-Python
            # https://inspiringpeople.github.io/data%20analysis/ckonlpy/



# 2. 은어, 줄임말, 전문용어 키워드 통일 전처리