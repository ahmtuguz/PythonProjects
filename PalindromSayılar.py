liste=[]

for i in range(900,1000):
    for j in range(900,1000):
        toplam=0
        tersi=0
        kalan=0
        
        toplam=i*j
        deger=toplam

        kalan=toplam%10
        toplam=toplam-kalan
        tersi=tersi+kalan*100000

        kalan=toplam%100
        toplam=toplam-kalan
        tersi=tersi+kalan*1000

        kalan=toplam%1000
        toplam=toplam-kalan
        tersi=tersi+kalan*10

        kalan=toplam%10000
        toplam=toplam-kalan
        tersi=tersi+kalan*0.1

        kalan=toplam%100000
        toplam=toplam-kalan
        tersi=tersi+kalan*0.001

        kalan=toplam%1000000
        toplam=toplam-kalan
        tersi=tersi+kalan*0.00001
       

        if deger==tersi:
            liste.append(deger)

print("Palindrom Sayılar: ")
print(liste)
            



