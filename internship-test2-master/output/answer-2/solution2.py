import pandas as pd
df=pd.DataFrame(pd.read_csv("C:/Users/server/Desktop/internship-test2-master/input/question-2/main.csv"))
result=df.groupby("occupation").agg({"age":["min","max"]})
print(result) 
result.to_csv("C:/Users/server/Desktop/internship-test2-master/output/answer-2/main.csv")  