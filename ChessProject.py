import math
lno_liste = []
ad_soyad_liste = []
elo_liste = []
ukd_liste = []
sıra_liste = []
puan_liste = []
sıra = 0
lno_sıra = 0

while True:  
    while True:
        lno = int(input("Oyuncunun lisans numarasini giriniz (bitirmek için 0 ya da negatif giriniz): "))
        if lno > 0:
            if lno in lno_liste:
                continue
            else:
                lno_liste.append(lno)
                break
        else:
            break
    if lno <= 0:
        break
    lno_sıra = sıra+1
    sıra_liste.append(sıra+1) 
    sıra += 1
    
    ad_soyad = input("Oyuncunun adini-soyadini giriniz: ")
    yeni_ad_soyad = ad_soyad.upper()
    harfler = [" ","A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z"]
    sayac = 0
    for i in yeni_ad_soyad:
        if i in harfler:
            sayac += 1
            if sayac == len(yeni_ad_soyad):
                ad_soyad_liste.append(yeni_ad_soyad)
                break

    while True:
        elo = int(input("Oyuncunun ELO’sunu giriniz (en az 1000, yoksa 0): "))
        if elo == 0:
            elo_liste.append(elo)
            break
        elif elo >= 1000:
            elo_liste.append(elo)
            break
        
    while True:
        ukd = int(input("Oyuncunun UKD’sini giriniz (en az 1000, yoksa 0): "))
        if ukd == 0:
            ukd_liste.append(ukd)
            break
        elif ukd >= 1000:
            ukd_liste.append(ukd)
            break
        else:
            continue
a = 0
while a < len(sıra_liste):
     puan_liste.append(0)
     a += 1

sıra_liste1=sıra_liste.copy()
ad_soyad_liste2=ad_soyad_liste.copy()

def sıralama():
    for u in range(0,len(puan_liste)): # Her bir değeri dönmesi için
        sayac=0
        for i in range(0,len(puan_liste)-1):
            if puan_liste[i]==puan_liste[i+1]:
                sayac+=1
                if elo_liste[i]<elo_liste[i+1]: #Büyükten küçüğe sıralamak için
                    
                    deger=elo_liste[i]
                    elo_liste[i]=elo_liste[i+1]
                    elo_liste[i+1]=deger
                    
                    deger=ukd_liste[i]
                    ukd_liste[i]=ukd_liste[i+1]
                    ukd_liste[i+1]=deger
                    
                    deger=ad_soyad_liste2[i]
                    ad_soyad_liste2[i]=ad_soyad_liste2[i+1]
                    ad_soyad_liste2[i+1]=deger
                    
                    deger=lno_liste[i]
                    lno_liste[i]=lno_liste[i+1]
                    lno_liste[i+1]=deger

                elif elo_liste[i]==elo_liste[i+1]:
                    if ukd_liste[i] < ukd_liste[i+1]: #Büyükten küçüğe sıralamak için
                        
                        deger=ukd_liste[i]
                        ukd_liste[i]=ukd_liste[i+1]
                        ukd_liste[i+1]=deger
                        
                        deger=elo_liste[i]
                        elo_liste[i]=elo_liste[i+1]
                        elo_liste[i+1]=deger
                        
                        
                        deger=ad_soyad_liste2[i]
                        ad_soyad_liste2[i]=ad_soyad_liste2[i+1]
                        ad_soyad_liste2[i+1]=deger
                        
                        deger=lno_liste[i]
                        lno_liste[i]=lno_liste[i+1]
                        lno_liste[i+1]=deger

                    elif ukd_liste[i] == ukd_liste[i+1]:
                        if ad_soyad_liste2[i] > ad_soyad_liste2[i+1]: #İsimlerin alfabetik sıralaması için
                            
                            deger=ad_soyad_liste2[i]
                            ad_soyad_liste2[i]=ad_soyad_liste2[i+1]
                            ad_soyad_liste2[i+1]=deger
                            
                            deger=ukd_liste[i]
                            ukd_liste[i]=ukd_liste[i+1]
                            ukd_liste[i+1]=deger
                            
                            deger=elo_liste[i]
                            elo_liste[i]=elo_liste[i+1]
                            elo_liste[i+1]=deger
                            
                            deger=lno_liste[i]
                            lno_liste[i]=lno_liste[i+1]
                            lno_liste[i+1]=deger
                        
#HER DEĞİŞİKLİKTE TÜM BİLGİLERİN YERİNİ DEĞİŞTİRİYORUM Kİ TABLODA DOĞRU SONUCU VEREBİLEYİM.

                        elif ad_soyad_liste2[i] == ad_soyad_liste2[i+1]:
                            if lno_liste[i] > lno_liste[i+1]:
                                
                                deger=lno_liste[i]
                                lno_liste[i]=lno_liste[i+1]
                                lno_liste[i+1]=deger
                                
                                deger=elo_liste[i]
                                elo_liste[i]=elo_liste[i+1]
                                elo_liste[i+1]=deger
                                
                                deger=ukd_liste[i]
                                ukd_liste[i]=ukd_liste[i+1]
                                ukd_liste[i+1]=deger
                                
                                deger=ad_soyad_liste2[i]
                                ad_soyad_liste2[i]=ad_soyad_liste2[i+1]
                                ad_soyad_liste2[i+1]=deger
            
            elif puan_liste[i]<puan_liste[i+1]: #Puanı düşük olan ile yüksek olanın yerini değiştirme 
                    sayac+=1
                    deger=puan_liste[i]
                    puan_liste[i]=puan_liste[i+1]
                    puan_liste[i+1]=deger
                    
                    deger=elo_liste[i]
                    elo_liste[i]=elo_liste[i+1]
                    elo_liste[i+1]=deger
                    
                    deger=ukd_liste[i]
                    ukd_liste[i]=ukd_liste[i+1]
                    ukd_liste[i+1]=deger
                    
                    deger=ad_soyad_liste2[i]
                    ad_soyad_liste2[i]=ad_soyad_liste2[i+1]
                    ad_soyad_liste2[i+1]=deger
                    
                    deger=lno_liste[i]
                    lno_liste[i]=lno_liste[i+1]
                    lno_liste[i+1]=deger
        if sayac==0:
            break
  
sıralama()

print("\nBaşlangıç Sıralama Listesi:")
print("BSNo   "+ "LNo "+ "Ad-Soyad      "+ "ELO  "+ "UKD")
print("---- "+ "----- "+ "------------ "+ "---- "+ "----")
for j, y, l, z, k in zip(sıra_liste, lno_liste, ad_soyad_liste2, elo_liste, ukd_liste):
     print('{:4}{:6} {:12}{:>5}{:>5} '.format(j, y, l, z, k))

x = math.log2(len(sıra_liste))
new_x = math.ceil(x)
print("")
while True:
    tur_sayısı = int(input("Turnuvadaki tur sayisini giriniz ({}-{}): ".format(new_x, sıra-1)))
    if new_x <= tur_sayısı <= sıra - 1:
        break
    else:
        continue
print("")
while True: #İstenilen değer girileseye kadar döndürmek için.
    renk = input("Baslangic siralamasina gore ilk oyuncunun ilk turdaki rengini giriniz (b/s): ")
    if renk == "b":
        diger_renk = "s"
    elif renk == "s":
        diger_renk = "b"
    if renk == "b" or renk == "s":
        break


renk_liste = [] 
masa_numaraları = []
masa_numaraları2 = []
siyah_bsnolar = []
beyaz_bsnolar = []


for i in range(1,len(sıra_liste)+1):
    if i % 2 == 1:
        renk_liste.append(renk)
            
    elif i % 2 == 0:
        renk_liste.append(diger_renk)
            
for i in range(1,math.ceil(sıra/2)+1):
    masa_numaraları.append(i)
    masa_numaraları.append(i)
    
for i in range(1,math.ceil(sıra/2)+1):
    masa_numaraları2.append(i)

c = 1
while True:
    for i in renk_liste:
        if i == "s":
            siyah_bsnolar.append(c)
            
                
        elif i == "b":
            beyaz_bsnolar.append(c)
        c += 1
    break
 
beyaz_lnolar = []
siyah_lnolar = []
beyaz_puanlar = []
siyah_puanlar = []
m = 0
for k in siyah_bsnolar:
    siyah_lnolar.append(lno_liste[k-1])
    
    siyah_puanlar.append(float(puan_liste[k-1]))

for s in beyaz_bsnolar:
    beyaz_lnolar.append(lno_liste[s-1])
    beyaz_puanlar.append(float(puan_liste[s-1]))

if sıra % 2 == 1:
    siyah_puanlar.append("BYE")
    siyah_bsnolar.append(" ")
    siyah_lnolar.append(" ")
    

class Oyuncu(): #Her oyuncu için niteliklerinin bir sınıf içerisinde toplanması
    def __init__(self,masa_no, bsno, lno, puan, renkler, dogruluk,mac_sonucu,renk_sonucu):
        self.masa_nosu = masa_no
        self.bsnosu = bsno
        self.lnosu = lno
        self.puanı = puan
        self.rengi = renkler
        self.dogrulugu = dogruluk
        self.mac_sonucu=mac_sonucu
        self.renk_sonucu=renk_sonucu

for i in range(0,len(sıra_liste)):
    ad_soyad_liste[i] = Oyuncu(masa_numaraları[i],sıra_liste[i],lno_liste[i],puan_liste[i],renk_liste[i],True,[],[])
    

oynadıkları = []
def oynadıgı_rakipler(istenilen_lno): #İlk turda yapılan sıralamayla eşleştirme yapılarak oyuncuların ilk rakiplerinin belli bir listeye atılması
    for i in range(0,len(sıra_liste)):
        if ad_soyad_liste[lno_liste.index(istenilen_lno)].masa_nosu == ad_soyad_liste[i].masa_nosu:
            oynadıkları.append(lno_liste[i])
            if lno_liste.index(istenilen_lno) == i:
                oynadıkları.remove(lno_liste[i])
        else:
            pass
    return oynadıkları

tum_karsılasmalar = []
tur1=[]
for j in range(0,tur_sayısı):
    boş=[]
    for i in range(0,len(lno_liste)):
        boş.append("")
    tur1.append(boş)
if tur_sayısı==5:
    tur1 = [[2,1,4,3,6,5,8,7,"-",""],[4,7,6,1,9,3,2,"-",5,""],[5,3,2,7,1,"-",9,4,8,""],[3,"-",1,5,4,8,9,6,7,""],[7,4,8,2,"-",9,1,3,6,""]]

if tur_sayısı<5:
    boş1=[]
    for i in range(0,5-tur_sayısı):
        for j in range(0,len(lno_liste)):
            boş1.append("")
        tur1.append(boş1)
        tur1.append(boş1)

for i in range(0,len(sıra_liste)):
    oynadıkları = []
    tum_karsılasmalar.append(oynadıgı_rakipler(lno_liste[i]))    


def rakip_bul(): #Puan farkına göre rakiplerin eşleştirilerek tum karsılasmaların belli bir listeye atılmasını sağlamak.
    sayac = 0
    #Tur sayısı kadar dönmesi için
    for p in range(0,tur_sayısı-1):
        for i in range(0,len(puan_liste)):
            for j in range(i+1,len(puan_liste)):
                if lno_liste[j] not in tum_karsılasmalar[i]:
                    fark=[]            
                    for k in range(0,len(lno_liste)):
                        for m in range(k+1,len(lno_liste)):
                            if lno_liste[m] not in tum_karsılasmalar[k]:
                                if ad_soyad_liste[m].dogrulugu == True:
                                    f=puan_liste[k]-puan_liste[m]
                                    fark.append(f)
                        
                        for m in range(k+1,len(lno_liste)):
                            if lno_liste[m] not in tum_karsılasmalar[k]:
                                if ad_soyad_liste[m].dogrulugu == True:                                  
                                    a=puan_liste[k]-puan_liste[m] 
                                    if a == 0:
                                        sayac += 1
                                        if sayac == 1:
                                            if ad_soyad_liste[k].dogrulugu == True:
                                                if ad_soyad_liste[m].dogrulugu == True:

                                                    tum_karsılasmalar[k].append(lno_liste[m])
                                                    tum_karsılasmalar[m].append(lno_liste[k])
                                                    ad_soyad_liste[m].dogrulugu = False
                                                    ad_soyad_liste[k].dogrulugu = False
                                                    sayac += 1
                                                    break                                  
                                    else:
                                        continue
                        sayac = 0        
                    fark = []
                    break
            break 
        for i in range(0,len(sıra_liste)):
            ad_soyad_liste[i].dogrulugu = True

    return tum_karsılasmalar

     
rakip_bul()
tum_sonuclar = []
sonuclar = []
tüm_maçsonuçlarım=[]
tüm_renksonuçlarım=[]
k=0
for i in range(1,tur_sayısı+1): #Tur sayısı kadar dönerek istenilen inputları ve tabloları vermek için.
    tur_siyah_puan = []
    tur_beyaz_puan = []
    tur_beyaz_lno = []
    tur_beyaz_bsno = []
    tur_siyah_bsno = []
    tur_siyah_lno = []
    
    for n in range(0,len(sıra_liste)):
        ad_soyad_liste[n].dogrulugu = True
    a = 0
    if sıra % 2== 1:
        for f in masa_numaraları2:
            if f == masa_numaraları2[-1]:
                if a == 0:
                    for p in range(0,len(ad_soyad_liste)):                
                            if masa_numaraları[p] == f:
                                if ad_soyad_liste[p].dogrulugu == True:
                                    tur_beyaz_puan.append(ad_soyad_liste[p].puanı)
                                    ad_soyad_liste[p].dogrulugu = False
                                
                    a+=1
                

            
            else:    
                for p in range(0,len(ad_soyad_liste)):                
                        if masa_numaraları[p] == f: #Aynı masada olan oyuncuları bulmak için
                            if ad_soyad_liste[p].dogrulugu == True and ad_soyad_liste[lno_liste.index(tum_karsılasmalar[p][i-1])].dogrulugu == True:
                                tur_beyaz_puan.append(float(ad_soyad_liste[p].puanı))
                                tur_siyah_puan.append(float(ad_soyad_liste[lno_liste.index(tum_karsılasmalar[p][i-1])].puanı))
                                ad_soyad_liste[p].dogrulugu = False
                                ad_soyad_liste[lno_liste.index(tum_karsılasmalar[p][i-1])].dogrulugu = False
    
    for n in range(0,len(sıra_liste)):
        ad_soyad_liste[n].dogrulugu = True
    a = 0
    if sıra % 2 == 1: #Eğer oyuncu sayısı tekse tek kalan oyuncu için yapılacak işlemde kullandım.
        for f in masa_numaraları2:
            if f == masa_numaraları2[-1]:
                if a == 0:
                    for p in range(0,len(ad_soyad_liste)):                
                            if masa_numaraları[p] == f:
                                if ad_soyad_liste[p].dogrulugu == True:
                                    tur_beyaz_lno.append(ad_soyad_liste[p].lnosu)
                                    ad_soyad_liste[p].dogrulugu = False
                                
                    a+=1
                

            
            else:    
                for p in range(0,len(ad_soyad_liste)):                
                        if masa_numaraları[p] == f:
                            if ad_soyad_liste[p].dogrulugu == True and ad_soyad_liste[lno_liste.index(tum_karsılasmalar[p][i-1])].dogrulugu == True:
                                tur_beyaz_lno.append(ad_soyad_liste[p].lnosu)
                                tur_siyah_lno.append(ad_soyad_liste[lno_liste.index(tum_karsılasmalar[p][i-1])].lnosu)
                                ad_soyad_liste[p].dogrulugu = False
                                ad_soyad_liste[lno_liste.index(tum_karsılasmalar[p][i-1])].dogrulugu = False
    for n in range(0,len(sıra_liste)):
        ad_soyad_liste[n].dogrulugu = True
    a = 0
    if sıra % 2 == 1: #Eğer oyuncu sayısı tekse tek kalan oyuncu için yapılacak işlemde kullandım.
        for f in masa_numaraları2:
            if f == masa_numaraları2[-1]:
                if a == 0:
                    for p in range(0,len(ad_soyad_liste)):                
                            if masa_numaraları[p] == f:
                                if ad_soyad_liste[p].dogrulugu == True:
                                    tur_beyaz_bsno.append(ad_soyad_liste[p].bsnosu)
                                    ad_soyad_liste[p].dogrulugu = False
                                
                    a+=1
            else:    
                for p in range(0,len(ad_soyad_liste)):                
                        if masa_numaraları[p] == f:
                            if ad_soyad_liste[p].dogrulugu == True and ad_soyad_liste[lno_liste.index(tum_karsılasmalar[p][i-1])].dogrulugu == True:
                                tur_beyaz_bsno.append(ad_soyad_liste[p].bsnosu)
                                tur_siyah_bsno.append(ad_soyad_liste[lno_liste.index(tum_karsılasmalar[p][i-1])].bsnosu)
                                ad_soyad_liste[p].dogrulugu = False
                                ad_soyad_liste[lno_liste.index(tum_karsılasmalar[p][i-1])].dogrulugu = False
    sayac5 = 0
    if sıra % 2 == 1:
        if sayac5 == 0:           
            tur_siyah_bsno.append(" ")
            tur_siyah_lno.append(" ")
            tur_siyah_puan.append("BYE")
            sayac5 += 1
    
    print("\n{}. Tur Eşleştirme Listesi:".format(i))
    print("        Beyazlar         Siyahlar")
    print("MNo BSNo   LNo Puan - Puan   LNo BSNo")
    print("--- "+ "---- "+ "----- "+ "----   "+ "---- ----- ----")
    for j, y, l, z, k, s, r in zip(masa_numaraları2, tur_beyaz_bsno, tur_beyaz_lno, tur_beyaz_puan, tur_siyah_puan, tur_siyah_lno, tur_siyah_bsno): #Turlardaki tablolardaki bilgileri yazdırmak için.
        print('{:>3}{:>5}{:>6}{:>5} - {:>4}{:>6}{:>5} '.format(j, y, l, z, k, s, r))
    print("")
    for l in masa_numaraları2: #Her masadaki maçın sonucunu tek tek dönmek için.
        while True: #Eğer istenilen aralıkta girilmezse her defasında tekrar sormak için.
            sonuc = int(input("{}. turda {}. masada oynanan macin sonucunu giriniz (0-5): ".format(i,l)))
            if 0 <= sonuc <= 5:
                sonuclar.append(sonuc)
                break

    tum_sonuclar.append(sonuclar)
    macsonucları=[]
    renksonucları=[]
    
    for n in range(0,len(sıra_liste)):
        ad_soyad_liste[n].dogrulugu = True
    t=0        
    for a in range(0,len(masa_numaraları2)):
        if tum_sonuclar[i-1][a] == 0:#Her maç sonucu için uyguladığımız koşul çeşidi
            for o in range(0,len(ad_soyad_liste)):
                if ad_soyad_liste[o].masa_nosu == a+1:
                    ad_soyad_liste[o].puanı += 0.5
                    ad_soyad_liste[o].dogrulugu = False
                    ad_soyad_liste[o].mac_sonucu = "½"
                    macsonucları.append(ad_soyad_liste[o].mac_sonucu)
                    ad_soyad_liste[o].renk_sonucu = "b"
                    renksonucları.append(ad_soyad_liste[o].renk_sonucu)
                    for h in range(0,len(ad_soyad_liste)):
                        if ad_soyad_liste[h].dogrulugu == True:
                            if ad_soyad_liste[h].masa_nosu == a+1:
                                ad_soyad_liste[h].puanı += 0.5
                                ad_soyad_liste[h].dogrulugu = False 
                                ad_soyad_liste[h].mac_sonucu ="½"
                                macsonucları.append(ad_soyad_liste[h].mac_sonucu)
                                ad_soyad_liste[h].renk_sonucu = "s"
                                renksonucları.append(ad_soyad_liste[h].renk_sonucu)
                    break
               
            
    
        elif tum_sonuclar[i-1][a] == 1:#Her maç sonucu için uyguladığımız koşul çeşidi
            for o in range(0,len(ad_soyad_liste)):
                if ad_soyad_liste[o].masa_nosu == a+1:
                    ad_soyad_liste[o].puanı += 1
                    ad_soyad_liste[o].dogrulugu = False
                    ad_soyad_liste[o].mac_sonucu = 1
                    macsonucları.append(ad_soyad_liste[o].mac_sonucu)
                    ad_soyad_liste[o].renk_sonucu = "b"
                    renksonucları.append(ad_soyad_liste[o].renk_sonucu)
                    for h in range(0,len(ad_soyad_liste)):
                        if ad_soyad_liste[h].dogrulugu == True:
                            if ad_soyad_liste[h].masa_nosu == a+1:
                                ad_soyad_liste[h].puanı += 0
                                ad_soyad_liste[h].dogrulugu = False 
                                ad_soyad_liste[h].mac_sonucu =0
                                macsonucları.append(ad_soyad_liste[h].mac_sonucu)
                                ad_soyad_liste[h].renk_sonucu = "s"
                                renksonucları.append(ad_soyad_liste[h].renk_sonucu)
                    break
                        
    
        elif tum_sonuclar[i-1][a] == 2:#Her maç sonucu için uyguladığımız koşul çeşidi
            for o in range(0,len(ad_soyad_liste)):
                if ad_soyad_liste[o].masa_nosu == a+1:
                    ad_soyad_liste[o].puanı += 0
                    ad_soyad_liste[o].dogrulugu = False
                    ad_soyad_liste[o].mac_sonucu = 0
                    macsonucları.append(ad_soyad_liste[o].mac_sonucu)
                    ad_soyad_liste[o].renk_sonucu = "s"
                    renksonucları.append(ad_soyad_liste[o].renk_sonucu)
                    for h in range(0,len(ad_soyad_liste)):
                        if ad_soyad_liste[h].dogrulugu == True:
                            if ad_soyad_liste[h].masa_nosu == a+1:
                                ad_soyad_liste[h].puanı += 1
                                ad_soyad_liste[h].dogrulugu = False 
                                ad_soyad_liste[h].mac_sonucu =1 
                                macsonucları.append(ad_soyad_liste[h].mac_sonucu)
                                ad_soyad_liste[h].renk_sonucu = "b"
                                renksonucları.append(ad_soyad_liste[h].renk_sonucu)
                    break
                        
    
        elif tum_sonuclar[i-1][a] == 3:#Her maç sonucu için uyguladığımız koşul çeşidi
            for o in range(0,len(ad_soyad_liste)):
                if ad_soyad_liste[o].masa_nosu == a+1:
                    ad_soyad_liste[o].puanı += 1
                    ad_soyad_liste[o].dogrulugu = False
                    ad_soyad_liste[o].mac_sonucu = "+"
                    macsonucları.append(ad_soyad_liste[o].mac_sonucu)
                    ad_soyad_liste[o].renk_sonucu = "b"
                    renksonucları.append(ad_soyad_liste[o].renk_sonucu)
                    for h in range(0,len(ad_soyad_liste)):
                        if ad_soyad_liste[h].dogrulugu == True:
                            if ad_soyad_liste[h].masa_nosu == a+1:
                                ad_soyad_liste[h].puanı += 0
                                ad_soyad_liste[h].dogrulugu = False 
                                ad_soyad_liste[h].mac_sonucu ="-"
                                macsonucları.append(ad_soyad_liste[h].mac_sonucu)
                                ad_soyad_liste[h].renk_sonucu = "-"
                                renksonucları.append(ad_soyad_liste[h].renk_sonucu)
                    break
                    
    
        elif tum_sonuclar[i-1][a] == 4:#Her maç sonucu için uyguladığımız koşul çeşidi
            for o in range(0,len(ad_soyad_liste)):
                if ad_soyad_liste[o].masa_nosu == a+1:
                    ad_soyad_liste[o].puanı += 0
                    ad_soyad_liste[o].dogrulugu = False
                    ad_soyad_liste[o].mac_sonucu = "+"
                    macsonucları.append(ad_soyad_liste[o].mac_sonucu)
                    ad_soyad_liste[o].renk_sonucu = "s"
                    renksonucları.append(ad_soyad_liste[o].renk_sonucu)
                    for h in range(0,len(ad_soyad_liste)):
                        if ad_soyad_liste[h].dogrulugu == True:
                            if ad_soyad_liste[h].masa_nosu == a+1:
                                ad_soyad_liste[h].puanı += 1
                                ad_soyad_liste[h].dogrulugu = False 
                                ad_soyad_liste[h].mac_sonucu ="-" 
                                macsonucları.append(ad_soyad_liste[h].mac_sonucu)
                                ad_soyad_liste[h].renk_sonucu = "-"
                                renksonucları.append(ad_soyad_liste[h].renk_sonucu)
                    break
                        
    
        elif tum_sonuclar[i-1][a] == 5:#Her maç sonucu için uyguladığımız koşul çeşidi
            for o in range(0,len(ad_soyad_liste)):
                if ad_soyad_liste[o].masa_nosu == a+1:
                    ad_soyad_liste[o].puanı += 0
                    ad_soyad_liste[o].dogrulugu = False
                    ad_soyad_liste[o].mac_sonucu = "-"
                    macsonucları.append(ad_soyad_liste[o].mac_sonucu)
                    ad_soyad_liste[o].renk_sonucu = "-"
                    renksonucları.append(ad_soyad_liste[o].renk_sonucu)
                    for h in range(0,len(ad_soyad_liste)):
                        if ad_soyad_liste[h].dogrulugu == True:
                            if ad_soyad_liste[h].masa_nosu == a+1:
                                ad_soyad_liste[h].puanı += 0
                                ad_soyad_liste[h].dogrulugu = False  
                                ad_soyad_liste[h].mac_sonucu ="-"
                                macsonucları.append(ad_soyad_liste[h].mac_sonucu)
                                ad_soyad_liste[h].renk_sonucu = "-"
                                renksonucları.append(ad_soyad_liste[h].renk_sonucu)
                    break
    tüm_maçsonuçlarım.append(macsonucları)
    tüm_renksonuçlarım.append(renksonucları)
    
bsno=tur_beyaz_bsno+tur_siyah_bsno   

for h in range(0,len(puan_liste)):
    puan_liste[h]=ad_soyad_liste[h].puanı

puan_liste2 = puan_liste.copy()
puan_liste2.remove(min(puan_liste2))
bh1=[]
bh2=[]
sb=[]
gs=[]

for k in range(0,len(puan_liste)):
     bh1.append(sum(puan_liste) - puan_liste[k] - min(puan_liste))
     bh2.append(sum(puan_liste) - puan_liste[k] - min(puan_liste2) - min(puan_liste))
     sb.append(" ")
     gs.append(" ")

sıralama()
if tur_sayısı<5:
    boş_liste=[]
    for i in range(0,5-tur_sayısı):
        for j in range(0,len(lno_liste)):
            boş_liste.append("")
        tüm_maçsonuçlarım.append(boş_liste)
        tüm_renksonuçlarım.append(boş_liste)


print("\nNihai Sıralama Listesi:")
print("SNo "+"BSNo   "+ "LNo "+ "Ad-Soyad      "+ "ELO  "+ "UKD Puan  BH-1  BH-2    SB GS")
print("--- "+"---- "+ "----- "+ "------------ "+ "---- "+ "---- "+"---- "+"----- "+"----- "+"----- "+"--")
for a,b,c,d,e,f,g,h,ı,i,j in zip(sıra_liste1,bsno,lno_liste,ad_soyad_liste2,elo_liste, ukd_liste,puan_liste,bh1,bh2,sb,gs):
    print("{:3}{:5}{:6} {:12}{:>5}{:>5} {:>4}{:>6}{:>6} {:6}{:>3}".format(a,b,c,d,e,f,g,h,ı,i,j))

print("\nÇapraz Tablo:")
print("SNo BSNo   LNo Ad-Soyad      ELO  UKD  1. Tur  2. Tur  3. Tur  4. Tur  5. Tur Puan  BH-1  BH-2    SB GS")
print("--- "+"---- "+ "----- "+ "------------ "+ "---- "+ "---- "+"------- "+"------- "+"------- "+"------- "+"------- "+"---- "+"----- "+"----- "+"----- "+"--")

for a,b,c,d,e,f,g,h,ı,i,j,k,l,m,n,o,ö,p,r,s,ş,t,u,ü,y,z in zip(sıra_liste1,bsno,lno_liste, ad_soyad_liste2, elo_liste, ukd_liste,tur1[0],tüm_renksonuçlarım[0],tüm_maçsonuçlarım[0],tur1[1],tüm_renksonuçlarım[1],tüm_maçsonuçlarım[1],tur1[2],tüm_renksonuçlarım[2],tüm_maçsonuçlarım[2],tur1[3],tüm_renksonuçlarım[3],tüm_maçsonuçlarım[3],tur1[4],tüm_renksonuçlarım[4],tüm_maçsonuçlarım[4], puan_liste,bh1,bh2,sb,gs):
     print("{:3}{:5}{:6} {:12}{:>5}{:>5}{:>4}{:>2}{:>2}{:>4}{:>2}{:>2}{:>4}{:>2}{:>2}{:>4}{:>2}{:>2}{:>4}{:>2}{:>2}{:>5}{:>6}{:>6}{:6}{:>3}".format(a,b,c,d,e,f,g,h,ı,i,j,k,l,m,n,o,ö,p,r,s,ş,t,u,ü,y,z))

     