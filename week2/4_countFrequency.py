import pandas as pd
import io
from collections import Counter

df = pd.read_csv('')


token = list(df['token'])

for i,v in enumerate(token):
  if len(v) < 2:
    token.pop(i)
    

countToken = Counter(token)
comList = countToken.most_common(30)
for v in comList:
  print(v)