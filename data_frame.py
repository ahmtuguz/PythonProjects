import pandas as pd
import numpy as np

# s1=pd.Series([5,2,3,4])
# s2=pd.Series([10,8,7,6])
# data=dict(apple=s1,bananas=s2)
# result=pd.DataFrame(data)
# print(result)

# list=[["Ahmet",90],["Büşra",40],["Murat",70],["Yagmur",20]]
# dict={"Name":["Ahmet","Büşra","Murat","Yagmur"],"Grade":[90,40,70,20]}
# dict_list=[
#     {"Name":"Ahmet","Grade":90},
#     {"Name":"Büşra","Grade":40},
#     {"Name":"Murat","Grade":70},
#     {"Name":"Yagmur","Grade":20}
#     ]
# result=pd.DataFrame(list,index=[1,2,3,4],columns=["Name","Grade"],dtype=float)
# result=pd.DataFrame(dict,index=[1,2,3,4])
# result=pd.DataFrame(dict_list,index=["a","b","c","d"])
# print(result)

# df=pd.read_csv("country_vaccinations.csv")
# df=pd.read_excel("2019-2020 akademik yili ka 103 ogrenim hibe listesi 24_03_2020.xlsx")
# df=pd.read_json("example_1.json")
# print(df)

df=pd.DataFrame(np.random.randn(3,3),index=["A","B","C"],columns=["Coloum1","Coloum2","Coloum3"])
result=df["Coloum1"]
result=type(df["Coloum1"])
result=df.loc["A","Coloum2"]
result=df.loc[:,:"Coloum2"]
result=df.loc[:,"Coloum1":"Coloum2"]
result=df.loc[:"B","Coloum1":"Coloum2"]
result=df.iloc[:2]
result=df.loc[["A","C"],["Coloum1","Coloum3"]]

df["Coloum4"]=pd.Series(np.random.randn(3),index=["A","B","C"])
df["Coloum5"]=df["Coloum2"]+df["Coloum3"]
df.drop("Coloum1",axis=1,inplace=True)
print(df)
print(result)