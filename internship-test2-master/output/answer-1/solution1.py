import pandas as pd
import numpy as np
df = pd.read_csv ("C:/Users/server/Desktop/internship-test2-master/input/question-1/main.csv")
print(df)
df.groupby(pd.Grouper(key='Year')).sum()
df.groupby((df['Year']//10)*10).sum()
print(df)
df.to_csv("C:/Users/server/Desktop/internship-test2-master/output/answer-1/main.csv") 