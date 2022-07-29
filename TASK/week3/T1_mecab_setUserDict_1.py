#
with open("C:/mecab/user-dic/nnp.csv", 'r', encoding='utf-8') as f: 
    file_data = f.readlines()
print(file_data)


#
file_data.clear()
#
# file_data.append('표층형,0,0,0,품사,의미부류,종성유무,읽기,타입,첫품사,막품사,원형,인덱스표현\n')

file_data.append('아주대,,,,NNP,*,F,아주대,*,*,*,*,*\n')
file_data.append('이직,,,0,NNP,*,F,이직,*,*,*,*,*\n')
file_data.append('빅데이터,,,0,NNP,*,F,빅데이터,*,*,*,*,*\n')
file_data.append('임금체불,,,0,NNP,*,F,임금체불,*,*,*,*,*\n')
file_data.append('지급명령,,,0,NNP,*,F,지급명령,*,*,*,*,*\n')
file_data.append('컴공과,,,0,NNP,*,F,컴공과,*,*,*,*,*\n')
file_data.append('신입생,,,0,NNP,*,F,신입생,Compound,*,*,신입+생,*\n')
file_data.append('사장님,,,0,NNP,*,F,사장님,*,*,*,*,*\n')
file_data.append('코드분석,,,0,NNP,*,F,코드분석,*,*,*,*,*\n')
file_data.append('리액트,,,0,NNP,*,F,리액트,*,*,*,*,*\n')
file_data.append('공식문서,,,0,NNP,*,F,공식문서,*,*,*,*,*\n')
file_data.append('배울점,,,0,NNP,*,F,배울점,*,*,*,*,*\n')
file_data.append('로컬스트리지,,,0,NNP,*,F,로컬스트리지,*,*,*,*,*\n')
file_data.append('미러링,,,0,NNP,*,F,미러링,*,*,*,*,*\n')
file_data.append('재지원,,,0,NNP,*,F,재지원,*,*,*,*,*\n')
file_data.append('C언어,,,0,NNP,*,F,C언어,*,*,*,*,*\n')
file_data.append('개인프로젝트,,,0,NNP,*,F,개인프로젝트,*,*,*,*,*\n')
file_data.append('깃헙,,,0,NNP,*,F,깃헙,*,*,*,*,*\n')
file_data.append('1일1커밋,,,0,NNP,*,F,1일1커밋,*,*,*,*,*\n')
file_data.append('데싸,,,0,NNP,*,F,데싸,*,*,*,*,*\n')
file_data.append('취준생,,,0,NNP,*,F,취준생,*,*,*,*,*\n')
file_data.append('1학년,,,0,NNP,*,F,1학년,*,*,*,*,*\n')
file_data.append('2학년,,,0,NNP,*,F,2학년,*,*,*,*,*\n')
file_data.append('3학년,,,0,NNP,*,F,3학년,*,*,*,*,*\n')
file_data.append('4학년,,,0,NNP,*,F,4학년,*,*,*,*,*\n')
file_data.append('플젝,,,0,NNP,*,F,플젝,*,*,*,*,*\n')
file_data.append('커리,,,0,NNP,*,F,커리,*,*,*,*,*\n')
file_data.append('작은회사,,,0,NNP,*,F,작은회사,*,*,*,*,*\n')
file_data.append('문제해결능력,,,0,NNP,*,F,문제해결능력,*,*,*,*,*\n')

# type = SH 따로 설정하는 이유
    # SH(한자) 품사태그는 형태소 중 가장 적게 식별되는 형태소라고 판단. 해당 SH태그를 특정 사용자설정 NNP들에 적용하여, NNP or NNG 복합명사 구성 로직에서 합성되지 않도록 fix 해두기 위해.
    # 추후 type의 연속등장 조건을 통해 복합명사 합성 로직에서
    # 더이상 합성되지 말아야 할 word를 고정시켜두기 위해 SH로 설정
        # NNP + NNP / NNP + NNG 등일 때, SH는 이 조건에 들어가지 않도록
file_data.append('의,,,0,JKG,*,F,의,*,*,*,*,*\n')
file_data.append('가요,,,0,EF,*,F,가요,*,*,*,*,*\n')

file_data.append('고졸,,,0,SH,*,T,고졸,*,*,*,*,*\n')
file_data.append('자료구조,,,0,SH,*,F,자료구조,*,*,*,*,*\n')
file_data.append('알고리즘,,,0,SH,*,T,알고리즘,*,*,*,*,*\n')




print(file_data)
with open("C:/mecab/user-dic/nnp.csv", 'w', encoding='utf-8') as f: 
    for line in file_data: 
        f.write(line)

        
# 컴파일로 마무리 : 파워쉘 관리자 권한
# > cd C:\mecab
# > .\tools\add-userdic-win.ps1
