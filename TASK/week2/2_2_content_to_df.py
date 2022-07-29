# import pandas as pd
# import numpy as np


# arr_noun = np.load('./week2/arr2_noun_content.npy',allow_pickle=True).tolist()


# print(arr_noun)
# # 0. title to df
# df = pd.DataFrame(columns=['art_id','token'])
# temp = 0

# for i in range(len(arr_noun)):
#     print(f'level1: {i}====')
#     for j in range(len(arr_noun[i])):
#         temp += 1
#         df.loc[temp] = [i,arr_noun[i][j]]
        
# print(df)
# df.to_csv('./week2/df2_cleaned_noun_content.csv',encoding='utf-8-sig',index=False)


# # 1. content to df