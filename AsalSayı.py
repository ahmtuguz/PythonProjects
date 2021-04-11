def asaılSayıHesapla(sayı1,sayı2):
    for sayı in range(sayı1,sayı2+1):
        if sayı>1:
            for i in range(2,sayı):
                if sayı%i==0:
                    break
            else:
                    print(sayı)
sayı1=int(input("sayı giriniz: "))
sayı2=int(input("sayı giriniz: "))
asaılSayıHesapla(sayı1,sayı2)