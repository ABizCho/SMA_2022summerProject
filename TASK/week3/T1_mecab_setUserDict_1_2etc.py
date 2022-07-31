

#####################################
with open("C:/mecab/user-dic/jkg.csv", 'r', encoding='utf-8') as f: 
    file_data = f.readlines()
print(file_data)


#
file_data.clear()

#
file_data.append('의,,,0,JKG,*,F,의,*,*,*,*,*\n')

print(file_data)
with open("C:/mecab/user-dic/jkg.csv", 'w', encoding='utf-8') as f: 
    for line in file_data: 
        f.write(line)
        
##########################################
with open("C:/mecab/user-dic/ef.csv", 'r', encoding='utf-8') as f: 
    file_data = f.readlines()
print(file_data)


#
file_data.clear()

#
file_data.append('가요,,,0,EF,*,F,가요,*,*,*,*,*\n')

print(file_data)
with open("C:/mecab/user-dic/ef.csv", 'w', encoding='utf-8') as f: 
    for line in file_data: 
        f.write(line)