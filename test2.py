import numpy as np

arr4_objs = np.load('arr4_objs.npy', allow_pickle=True).tolist()

# print(arr4_objs)

# ''''''
# # arrObj 불러오기 유효성 검증
# print(type(arr4_objs[0]['art_id']))
# print(type(arr4_objs[0]['art_date_year']))
# print(type(arr4_objs[0]['art_date_month']))
# print(type(arr4_objs[0]['art_date_hour']))
# print(type(arr4_objs[0]['user_score']))
# print(type(arr4_objs[0]['art_Ncomment']))
# print(type(arr4_objs[0]['artNview']))
# print(type(arr4_objs[0]['art_Nlike']))
# print(type(arr4_objs[0]['art_title']))
# print(type(arr4_objs[0]['art_content']))
# print(type(arr4_objs[0]['comments']))
# print(arr4_objs[1]['comments'])


# for i in range(50):
#     print(arr4_objs[i])
    
''''''
np.savetxt('arr4_objsTxt.txt',arr4_objs)

