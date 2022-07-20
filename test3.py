from types import NoneType
import pandas as pd

df = pd.read_csv('./outputs/df3_artsCleanEtc.csv')

def replace_nChar(str) :
    return str.replace('\n',' ')
    
df['art_title'] = df['art_title'].map(replace_nChar)

df.to_csv('df3_2_artsCleanEtc.csv', encoding='utf-8-sig',index=False)
