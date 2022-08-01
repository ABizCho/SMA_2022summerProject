# compile 이후 우선순위 변경

#1.불러오기
with open("C:/mecab/mecab-ko-dic/user-jkg.csv", 'r', encoding='utf-8') as f: 
    file_data = f.readlines()
print(file_data)

#2.용이한 수정을 위한 인덱스 출력 코드 
for i in range(len(file_data)):
    print(f'[인덱스 : {i}] = {file_data[i]}')

#3.수정부
    # 기본 폼 예시 : '의,465,551,0,JKG,*,F,의,*,*,*,*,*\n'

file_data[0] = '의,465,551,0,JKG,*,F,의,*,*,*,*,*\n' # '의'의 우선순위 수정
print(file_data)

#4.저장부
with open("C:/mecab/mecab-ko-dic/user-jkg.csv", 'w', encoding='utf-8') as f: 
    for line in file_data: 
        f.write(line)
        
        
# 컴파일로 마무리 : 파워쉘 관리자 권한
# > cd C:\mecab
# > .\tools\add-userdic-win.ps1
######################################################################################

with open("C:/mecab/mecab-ko-dic/user-ef.csv", 'r', encoding='utf-8') as f: 
    file_data = f.readlines()
print(file_data)

#2.용이한 수정을 위한 인덱스 출력 코드 
for i in range(len(file_data)):
    print(f'[인덱스 : {i}] = {file_data[i]}')

#3.수정부
    # 기본 폼 예시 : '의,465,551,0,JKG,*,F,의,*,*,*,*,*\n'

file_data[0] = '가요,3,5,0,EF,*,F,가요,*,*,*,*,*\n' # '의'의 우선순위 수정
print(file_data)

#4.저장부
with open("C:/mecab/mecab-ko-dic/user-ef.csv", 'w', encoding='utf-8') as f: 
    for line in file_data: 
        f.write(line)
        