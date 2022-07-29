import pandas as pd

df = pd.read_csv('df_arts.csv',encoding='utf-8-sig')
    # 개행문자 등 제거
for i in range(len(df)):
    df.loc[i,'comments'] = df.loc[i,'comments'].replace("[","").replace("]","").replace("\\n","").replace("\\t","").replace("\\xa0","").replace("\\xa0","")

# for i in range(len(df)):
#     print(df.loc[i,'comments'])

df.to_csv('df2_arts_cleanMeta.csv',encoding='utf-8-sig',index=False)

