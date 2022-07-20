import pandas as pd
import numpy as np


arr_noun = np.load('./week2/arr_noun_title.npy',allow_pickle=True).tolist()

# 0. title to df
df = pd.DataFrame(columns=['art_id','token'])
temp = 0

for i in range(len(arr_noun)):
    print(f'level1: {i}------------------')
    for j in range(len(arr_noun[i])):
        temp += 1
        df.loc[temp] = [i,arr_noun[i][j]]
        
print(df)
df.to_csv('./week2/df1_cleand_noun_title.csv',encoding='utf-8-sig',index=False)


# 1. content to df