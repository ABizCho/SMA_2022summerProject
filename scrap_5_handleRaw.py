import numpy as np
import pandas as pd
arr4_objs = np.load('arr4_objs.npy',allow_pickle=True).tolist()


df_arts = pd.DataFrame( columns=['art_id','art_date_year','art_date_month','art_date_day','art_date_hour','user_score','art_Ncomment','artNview','art_Nlike','art_title','art_content','comments'])

for i in range(len(arr4_objs)):
    df_arts = df_arts.append(arr4_objs[i],ignore_index=True)

df_arts.to_csv('df_arts.csv',encoding='utf-8-sig',index=False)

