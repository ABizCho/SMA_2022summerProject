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
file_data.append('데이터 분석,,,0,NNP,*,F,데이터 분석,*,*,*,*,*\n')
file_data.append('데이터 사이언스,,,0,NNP,*,F,데이터 사이언스,*,*,*,*,*\n')
file_data.append('클린 코드,,,0,NNP,*,F,클린 코드,*,*,*,*,*\n')
file_data.append('클린 아키텍처,,,0,NNP,*,F,클린 아키텍처,*,*,*,*,*\n')
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
file_data.append('로컬스트리지,,,0,NNP,*,F,로컬스트리지,*,*,*,*,*\n')
file_data.append('스프링클라우드,,,0,NNP,*,F,스프링클라우드,*,*,*,*,*\n')
file_data.append('보고,,,0,NNP,*,F,보고,*,*,*,*,*\n')
file_data.append('커리,,,0,NNP,*,F,커리,*,*,*,*,*\n')
file_data.append('백엔드,,,0,NNP,*,F,백엔드,*,*,*,*,*\n')
('프론트엔드,,,0,NNP,*,F,프론트엔드,*,*,*,*,*\n')

file_data.append('컴퓨터 공학,,,0,NNP,*,T,컴퓨터 공학,*,*,*,*,*\n')
file_data.append('최종 면접,,,0,NNP,*,T,최종 면접,*,*,*,*,*\n')
file_data.append('토이 프로젝트,,,0,NNP,*,T,토이 프로젝트,*,*,*,*,*\n')
file_data.append('사이드 프로젝트,,,0,NNP,*,T,사이드 프로젝트,*,*,*,*,*\n')
file_data.append('자바 스크립트,,,0,NNP,*,T,자바 스크립트,*,*,*,*,*\n')
file_data.append('타입 스크립트,,,0,NNP,*,T,타입 스크립트,*,*,*,*,*\n')
file_data.append('대학생,,,0,NNP,*,T,대학생,*,*,*,*,*\n')
file_data.append('대학교,,,0,NNP,*,T,대학교,*,*,*,*,*\n')
file_data.append('고졸,,,0,NNP,*,T,고졸,*,*,*,*,*\n')
file_data.append('자료구조,,,0,NNP,*,F,자료구조,*,*,*,*,*\n')
file_data.append('알고리즘,,,0,NNP,*,T,알고리즘,*,*,*,*,*\n')
file_data.append('네카라쿠배,,,0,NNP,*,T,네카라쿠배,*,*,*,*,*\n')
file_data.append('네카라쿠배당토,,,0,NNP,*,T,네카라쿠배당토,*,*,*,*,*\n')
file_data.append('백엔드,,,0,NNP,*,T,백엔드,*,*,*,*,*\n')
file_data.append('프론트엔드,,,0,NNP,*,T,프론트엔드,*,*,*,*,*\n')
file_data.append('안드로이드 스튜디오,,,0,NNP,*,T,안드로이드 스튜디오,*,*,*,*,*\n')
file_data.append('인텔리제이,,,0,NNP,*,T,인텔리제이,*,*,*,*,*\n')
file_data.append('인텔리 제이,,,0,NNP,*,T,인텔리 제이,*,*,*,*,*\n')
file_data.append('비전공자,,,0,NNP,*,T,비전공자,*,*,*,*,*\n')
file_data.append('기반,,,0,NNP,*,T,기반,*,*,*,*,*\n')
file_data.append('현직,,,0,NNP,*,T,현직,*,*,*,*,*\n')
file_data.append('고도화,,,0,NNP,*,T,고도화,*,*,*,*,*\n')
file_data.append('현직,,,0,NNP,*,T,현직,*,*,*,*,*\n')
file_data.append('Deep Dive,,,0,NNP,*,T,Deep Dive,*,*,*,*,*\n')
file_data.append('딥다이브,,,0,NNP,*,T,딥다이브,*,*,*,*,*\n')
file_data.append('gs홈쇼핑,,,0,NNP,*,T,gs홈쇼핑,*,*,*,*,*\n')
file_data.append('전공책,,,0,NNP,*,T,전공책,*,*,*,*,*\n')
file_data.append('대기업,,,0,NNP,*,T,대기업,*,*,*,*,*\n')
file_data.append('중소기업,,,0,NNP,*,T,중소기업,*,*,*,*,*\n')
file_data.append('중견기업,,,0,NNP,*,T,중견기업,*,*,*,*,*\n')
file_data.append('영세업체,,,0,NNP,*,T,영세업체,*,*,*,*,*\n')
file_data.append('작은회사,,,0,NNP,*,T,작은회사,*,*,*,*,*\n')
file_data.append('기계식 키보드,,,0,NNP,*,T,기계식 키보드,*,*,*,*,*\n')
file_data.append('풀스택,,,0,NNP,*,T,풀스택,*,*,*,*,*\n')
file_data.append('확진자,,,0,NNP,*,T,확진자,*,*,*,*,*\n')
file_data.append('인터넷 쇼핑몰,,,0,NNP,*,T,인터넷 쇼핑몰,*,*,*,*,*\n')
file_data.append('앱 개발,,,0,NNP,*,T,앱 개발,*,*,*,*,*\n')
file_data.append('만원,,,0,NNP,*,T,만원,*,*,*,*,*\n')
file_data.append('년차,,,0,NNP,*,T,년차,*,*,*,*,*\n')
file_data.append('연차,,,0,NNP,*,T,연차,*,*,*,*,*\n')
file_data.append('개월,,,0,NNP,*,T,개월,*,*,*,*,*\n')
file_data.append('년,,,0,NNP,*,T,년,*,*,*,*,*\n')
file_data.append('원,,,0,NNP,*,T,원,*,*,*,*,*\n')
file_data.append('취준,,,0,NNP,*,T,취준,*,*,*,*,*\n')
file_data.append('솔루션 업체,,,0,NNP,*,T,솔루션 업체,*,*,*,*,*\n')
file_data.append('IT 기업,,,0,NNP,*,T,IT 기업,*,*,*,*,*\n')
file_data.append('계약 사항,,,0,NNP,*,T,계약 사항,*,*,*,*,*\n')

print(file_data)
with open("C:/mecab/user-dic/nnp.csv", 'w', encoding='utf-8') as f: 
    for line in file_data: 
        f.write(line)