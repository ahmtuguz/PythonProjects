import random
a=random.randint(0,101)


hak=5
sayaç=0
i=1
while i<=hak:
  x=int(input("SAYI GİRİNİZ: "))
  toplam=100-(20*sayaç)
  if x==a:
     print(f"TEBRİKLER {i}. HAKKINIZDA BİLDİNİZ VE... \n {toplam} PUAN KAZANDINIZ ")
     break
  
  else:
    if a>x:
        print("*********************YUKARI ÇIK**********************")
    elif a<x:
        print("**********************AŞAĞI İN***********************")

  
 
  i+=1  
  sayaç+=1
if i>hak:
      print("malesef hakkınız kalmadı")  
      print("GAME OVER:)")
      print(f"Doğru Cevap: {a}")
        

    
