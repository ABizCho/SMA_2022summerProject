import re
import pandas as pd

df = pd.read_csv('df2_arts_cleanMeta.csv')
#
def clean_str(text):
    if type(text) != str :
        return 0
    pattern = '([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)' # E-mail제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '(http|ftp|https)://(?:[-\w.]|(?:%[\da-fA-F]{2}))+' # URL제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '([ㄱ-ㅎㅏ-ㅣ]+)'  # 한글 자음, 모음 제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '<[^>]*>'         # HTML 태그 제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '[^\w\s]'         # 특수기호제거
    text = re.sub(pattern=pattern, repl='', string=text)
    return text

# 이모지 제거 함수
def remove_emoji(text):
    if type(text) != str :
        return 0
        
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                        #    u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)


# title 처리
for i in range(len(df)):
    df.loc[i,'art_title'] = remove_emoji(clean_str(df.loc[i,'art_title']))

# content 처리
for i in range(len(df)):
    df.loc[i,'art_content'] = remove_emoji(clean_str(df.loc[i,'art_content']))

# comments 처리
for i in range(len(df)):
    df.loc[i,'comments'] = remove_emoji(clean_str(df.loc[i,'comments']))
    
    
df.to_csv('df3_artsCleanEtc.csv',encoding='utf-8-sig',index=False)