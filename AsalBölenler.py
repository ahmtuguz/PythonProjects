liste=[]
sayı=int(input("Sayı Giriniz: "))

for i in range(2,sayı+1):
    if sayı%i==0:
        toplam=0
        for j in range(2,i):
            if i%j==0:
                toplam=toplam+1
            else:
                pass
        if toplam==0:    
            liste.append(i) 
              

print(liste)