import numpy as np
import pandas as pd

# sozluk={"İstanbul":[30,29,np.nan],"Ankara":[25,np.nan,20],"İzmir":[40,39,38],"Antalya":[30,np.nan,np.nan]}
# frame=pd.DataFrame(sozluk)
# frame=frame.dropna(axis=1,thresh=2)
# frame=frame.fillna(20)
# print(frame)

# yeni_sozluk={"Departman":["Yazılım","Hukuk","Hukuk","Pazarlama","Pazarlama","Yazılım"],
#             "İsmi":["Ahmet","Mehmet","Deniz","Irmak","Ali","İrem"],
#             "Maaş":[200,300,400,500,800,400]}
# yframe=pd.DataFrame(yeni_sozluk)
# yframe=yframe.groupby("Departman")
#yframe=yframe.count()
#yframe=yframe.mean()
#yframe=yframe.max()
#print(yframe)

# sozluk1={"İsim":["Ahmet","Mehmet","Ali"],
#          "Spor":["Futbol","Basketbol","Tenis"],
#         }
# sozluk2={"İsim":["Ahmet","Mehmet","Ali"],
#          "Kalori":[100,200,300],
#         }
# frame1=pd.DataFrame(sozluk1)
# frame2=pd.DataFrame(sozluk2)
# frame=pd.merge(frame1,frame2,on="İsim")
# print(frame)


# yeni_sozluk={
#             "İsmi":["Ahmet","Mehmet","Deniz","Irmak","Ali","İrem"],
#             "Departman":["Yazılım","Hukuk","Hukuk","Pazarlama","Pazarlama","Yazılım"],
#             "Maaş":[200,300,400,500,800,400]
#             }
# yframe=pd.DataFrame(yeni_sozluk)
# result=yframe["Departman"].unique()
# result=yframe["Departman"].nunique()
# result=yframe["Departman"].value_counts()

# def hesapla(maaş):
#     return maaş*0.66
# result=yframe["Maaş"].apply(hesapla)
# print(result)