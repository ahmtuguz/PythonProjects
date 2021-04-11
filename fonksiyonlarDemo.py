AliHesap={
    "ad":"Ali",
    "soyad":"Çetin",
    "bakiye":2000,
    "ekHesap":3000
}
VeliHesap={
    "ad":"Veli",
    "soyad":"Yılmaz",
    "bakiye":4000,
    "ekHesap":2000
}
def paraÇek(isim,tutar):
    toplam=isim["bakiye"]+isim["ekHesap"]
    if isim["bakiye"]>=tutar:
        print(f"Çekmek istediğiniz {tutar} lirayi çektiniz.")
        print(f"Kalan tutar: {isim['bakiye']-tutar}")
    elif toplam>=tutar:
        karar=int(input("Ek hesaba geçmek istiyor musunuz(1/2):"))
        if karar==1:
            print(f"Çekmek istediğiniz {tutar} lirayi çektiniz.")
            print(f"Ek hesapta kalan tutar: {toplam - tutar}")
        elif karar==2:
            print("İşlem sonlandırılıyor")
            print(f"Kalan tutar: {isim['bakiye']}")
        else:
            print("Hatalı işlem yaptınız tekrar deneyiniz.")
    else:
        print("Yetersiz bakiye.")
paraÇek(AliHesap,4000)