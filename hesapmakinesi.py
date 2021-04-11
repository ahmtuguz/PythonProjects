def toplama(sayı1,sayı2):
    return sayı1+sayı2

def çıkarma(sayı1,sayı2):
    return sayı1-sayı2

def çarpma(sayı1,sayı2):
    return sayı1*sayı2

def bölme(sayı1,sayı2):
    return sayı1/sayı2

işlem=input("yapmak istediğiniz işlem: ")
if(işlem=="+"):
    sayı1=int(input("toplamak istediğiniz sayıları giriniz:"))
    sayı2=int(input("toplamak istediğiniz sayıları giriniz:"))
    sonuç=toplama(sayı1,sayı2)

elif(işlem=="-"):
    sayı1=int(input("çıkarmak istediğiniz sayıları giriniz:"))
    sayı2=int(input("çıkarmak istediğiniz sayıları giriniz:"))
    sonuç=çıkarma(sayı1,sayı2)      

elif(işlem=="*"):
    sayı1=int(input("çarpmak istediğiniz sayıları giriniz:"))
    sayı2=int(input("çarpmak istediğiniz sayıları giriniz:"))
    sonuç=çarpma(sayı1,sayı2)

elif(işlem=="/"):
    sayı1=int(input("bölünen sayıyı giriniz:"))
    sayı2=int(input("bölen sayıyı giriniz:"))
    sonuç=bölme(sayı1,sayı2)

print(f"işleminizin sonucu ...{sonuç}...")