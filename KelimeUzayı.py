import itertools
import textwrap
import random
import time
#yazi="Durağan-bellek-özelliğiyle-tanımlanan-değişkene-programın-yürütülmesi-başlamadan-önce-bellekte-yer-atanır-Programda-değişkene-ilk-kez-başvurulduğunda-ana-belleğe-yüklenir-ve-programın-yürütülmesi-sona-erinceye-değin-atanan-yer-saklanır-Dışsal-bir-blokta-yürütme-sırasında-ilk-adımda-bazı-değişkenlerin-başlangıç-değerlerinin-biliniyor-olması-için-durağan-olarak-tanımlanmaları-uygun-bir-yoldur-İçsel-bir-prosedürde-bir-değişkenin-durağan-olarak-tanımlanması-içinse-prosedürün-ilk-yürütmesinden-son-yürütmesine-değin-değişkenin-değerinin-değişmemesi-gibi-bir-koşulun-varlığı-konu-olabilir-Her-iki-durumda-içsel-ve-dışsal-prosedürde-durağan-bellek-özelliğiyle-tanımlanan-değişken-bir-başka-prosedürde-yeni-bellek-sınıfı-gerektirecek-biçimde-tanımlandığı-sürece-durağan-bellek-sınıfı-özelliğini-korur-Ayrıca-durağan-bellek-özelliği-taşıyan-değişkenler-programın-neresinde-tanımlanırsa-tanımlansınlar-yürütmeden-önce-belleğe-atanırlar"
alfabe=["-","A","B","C","Ç", "D", "E","F","G","Ğ","H","İ","I","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z","a","b","c","ç","d","e","f","g","ğ","h","i","ı","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"," "]
balfabe=["A","B","C","Ç", "D", "E","F","G","Ğ","H","İ","I","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z"]
kalfabe=["a","b","c","ç","d","e","f","g","ğ","h","i","ı","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]

def checkAlphabet():
    c = 0
    while True:
        result=input("bir metin giriniz")
        result=result.replace("-"," ")
        for i in result:
            if i in alfabe:
                c += 1
                if c == len(result):
                    break
            else:
                c = 0
                break
        if c == len(result):
            break
    return result

result = checkAlphabet()
satir_genişliği=int(input("genişlik: "))

def satırDüzenle(text=result, indent=0, width=satir_genişliği):
    return "\n".join( textwrap.wrap(text, width=width, initial_indent=" "*indent, subsequent_indent=" "*indent) )

def interleave(*iterables):
	"[a,b,c], [1,2,3] -> [a,1,b,2,c,3]"
	return [c for c in itertools.chain.from_iterable(itertools.zip_longest(*iterables)) if c is not None]

def justify(width, text):
	return "\n".join(map(lambda line: (lambda words: (lambda w, n: "".join(interleave(words, [" " * (w // n + 2)] * (w % n) + [" " * (w // n + 1)] * (n - w % n))))(width - len(line), len(words)-1))(line.split()), text.splitlines()))
# newLine=satırDüzenle()
# newLine=newLine.splitlines()
# my_string =""
# for i in range(0,len(newLine)-1):
#      if len(newLine[i])<=satir_genişliği:
#             satır_listesi=newLine[i].split(" ")
#             while len(newLine[i])<=satir_genişliği:
#                 if (satir_genişliği-len(newLine[i]))<=(len(satır_listesi)-1):
#                         break
#                 for j in satır_listesi:
#                     if i%2==0:
#                         if j == satır_listesi[-1]:
#                             pass
#                         else:
#                                 j=j+"-"
#                         my_string += j
#                     elif i%2==1:
#                         if j == satır_listesi[-1]:
#                             pass
#                         else:
#                             j=j+"-"
#                         my_string+=j
#                 if (satir_genişliği-len(newLine[i]))<=(len(satır_listesi)-1):
#                         break
#             print(my_string)
#             my_string =""
                

#      else:
#          pass

def kelimeSayma(arg):
    newResult=arg.upper()
    
    kelime_sonucu=newResult.split(" ")
    kelime_sonucu=list(kelime_sonucu)
    kelime_sonucu.sort()

    sayı_sonucu=newResult.split(" ")
    sayı_sonucu=list(sayı_sonucu)
    sayı_sonucu.sort()
    
    i=0
    while i<len(kelime_sonucu):
        j=0
        while j<len(kelime_sonucu):
            if i!=j:
                if kelime_sonucu[i]==kelime_sonucu[j]:
                    kelime_sonucu.pop(j)
                else:
                    pass    
            else:
                pass
            j+=1
        i+=1 

    for i in range(0,len(sayı_sonucu)):
        değişken=1
        for j in range(0,len(sayı_sonucu)):
            if i!=j:
                if sayı_sonucu[i]==sayı_sonucu[j]:
                    değişken+=1
                else:
                    pass
        sayı_sonucu[i]=değişken        
    
    print("\nKelime"+(" "*15)+"Tekrar Say"+(" "*4)+"|"+(" "*4)+"Kelime"+(" "*15)+"Tekrar Say\n"+("-"*20)+" "+("-"*10)+(" "*4)+"|"+(" "*4)+("-"*20)+" "+("-"*10))

    #sayı_sonucu.sort()
    #sayı_sonucu.reverse()
    
    max_sonuç=0
    for i in range(0,len(kelime_sonucu)):
        if len(kelime_sonucu[i])>max_sonuç:
            max_sonuç=len(kelime_sonucu[i])

    for i in range(0,len(kelime_sonucu)):
        print(kelime_sonucu[i]+str(sayı_sonucu[i]).rjust((27-max_sonuç)+(max_sonuç-len(kelime_sonucu[i])))+(" "*8)+"|"+(" "*4)+kelime_sonucu[i]+str(sayı_sonucu[i]).rjust((27-max_sonuç)+(max_sonuç-len(kelime_sonucu[i]))))

def harfSayma(arg1,arg2,arg3):
    print("Harf"+(" "*2)+"1"+(" "*3)+"2"+(" "*3)+"3"+(" "*3)+"4"+(" "*3)+"5"+(" "*3)+"6"+(" "*3)+"7"+(" "*3)+"8"+(" "*3)+"9"+(" "*3)+"10"+(" "*3)+"11"+(" "*3)+"12"+(" "*3)+"13"+(" "*3)+"14"+(" "*3)+"15"+(" "*3)+"16"+(" "*3)+"17"+(" "*3)+"18"+(" "*3)+"19"+(" "*3)+"20"+"  Toplam")
    print("---- "+"--- "+"--- "+"--- "+"--- "+"--- "+"--- "+"--- "+"--- "+"--- "+"---- "+"---- "+"---- "+"---- "+"---- "+"---- "+"---- "+"---- "+"---- "+"---- "+"---- "+"------")
    
    byazi=result.lower()

    toplam=[]
    for i in kalfabe:
        adet=byazi.count(f"{i}")
        toplam.append(adet)

    sonuç=byazi.split(" ")
    sonuç=list(sonuç)
    sonuç.sort()
    
    sutün1=[]
    for i in kalfabe:
        sayaç=0  
        for j in range(0,len(sonuç)):
            if i==sonuç[j][0]:
                sayaç+=1
            else:
                pass
        if sayaç<10:
            sayaç="0"+str(sayaç)
        sutün1.append(sayaç)  

    sutün2=[]
    for i in kalfabe:
        sayaç=0
        for j in range(0,len(sonuç)):
            if i==sonuç[j][1]:
                sayaç+=1
            else:
                pass
        if sayaç<10:
            sayaç="0"+str(sayaç)
        sutün2.append(sayaç)    

    sutün3=[]
    for i in kalfabe:
        sayaç=0  
        for j in range(0,len(sonuç)):
            if len(sonuç[j])>=3:
                if i==sonuç[j][2]:
                    sayaç+=1
                else:
                    pass
            else:
                pass    
        if sayaç<10:
            sayaç="0"+str(sayaç)
        sutün3.append(sayaç)  

    sutün4=[]
    for i in kalfabe:
        sayaç=0  
        for j in range(0,len(sonuç)):
            if len(sonuç[j])>=4:
                if i==sonuç[j][3]:
                    sayaç+=1
                else:
                    pass
        if sayaç<10:
            sayaç="0"+str(sayaç)
        sutün4.append(sayaç)  

    sutün5=[]
    for i in kalfabe:
        sayaç=0  
        for j in range(0,len(sonuç)):
            if len(sonuç[j])>=5:
                if i==sonuç[j][4]:
                    sayaç+=1
                else:
                    pass
        if sayaç<10:
            sayaç="0"+str(sayaç)
        sutün5.append(sayaç)  

    sutün6=[]
    for i in kalfabe:
        sayaç=0  
        for j in range(0,len(sonuç)):
            if len(sonuç[j])>=6:
                if i==sonuç[j][5]:
                    sayaç+=1
                else:
                    pass
        if sayaç<10:
            sayaç="0"+str(sayaç)
        sutün6.append(sayaç)  

    sutün7=[]
    for i in kalfabe:
        sayaç=0  
        for j in range(0,len(sonuç)):
            if len(sonuç[j])>=7:
                if i==sonuç[j][6]:
                    sayaç+=1
                else:
                    pass
        if sayaç<10:
            sayaç="0"+str(sayaç)
        sutün7.append(sayaç)  

    sutün8=[]
    for i in kalfabe:
        sayaç=0  
        for j in range(0,len(sonuç)):
            if len(sonuç[j])>=8:
                if i==sonuç[j][7]:
                    sayaç+=1
                else:
                    pass
        if sayaç<10:
            sayaç="0"+str(sayaç)
        sutün8.append(sayaç)  

    sutün9=[]
    for i in kalfabe:
        sayaç=0  
        for j in range(0,len(sonuç)):
            if len(sonuç[j])>=9:
                if i==sonuç[j][8]:
                    sayaç+=1
                else:
                    pass
        if sayaç<10:
            sayaç="0"+str(sayaç)
        sutün9.append(sayaç)  

    sutün10=[]
    for i in kalfabe:
        sayaç=0  
        for j in range(0,len(sonuç)):
            if len(sonuç[j])>=10:
                if i==sonuç[j][9]:
                    sayaç+=1
                else:
                    pass
        if sayaç<10:
            sayaç="0"+str(sayaç)
        sutün10.append(sayaç)  

    sutün11=[]
    for i in kalfabe:
        sayaç=0  
        for j in range(0,len(sonuç)):
            if len(sonuç[j])>=11:
                if i==sonuç[j][10]:
                    sayaç+=1
                else:
                    pass
        if sayaç<10:
            sayaç="0"+str(sayaç)
        sutün11.append(sayaç)  

    sutün12=[]
    for i in kalfabe:
        sayaç=0  
        for j in range(0,len(sonuç)):
            if len(sonuç[j])>=12:
                if i==sonuç[j][11]:
                    sayaç+=1
                else:
                    pass
        if sayaç<10:
            sayaç="0"+str(sayaç)
        sutün12.append(sayaç)  

    sutün13=[]
    for i in kalfabe:
        sayaç=0  
        for j in range(0,len(sonuç)):
            if len(sonuç[j])>=13:
                if i==sonuç[j][12]:
                    sayaç+=1
                else:
                    pass
        if sayaç<10:
            sayaç="0"+str(sayaç)
        sutün13.append(sayaç)  

    sutün14=[]
    for i in kalfabe:
        sayaç=0  
        for j in range(0,len(sonuç)):
            if len(sonuç[j])>=14:
                if i==sonuç[j][13]:
                    sayaç+=1
                else:
                    pass
        if sayaç<10:
            sayaç="0"+str(sayaç)
        sutün14.append(sayaç)  

    sutün15=[]
    for i in kalfabe:
        sayaç=0  
        for j in range(0,len(sonuç)):
            if len(sonuç[j])>=15:
                if i==sonuç[j][14]:
                    sayaç+=1
                else:
                    pass
        if sayaç<10:
            sayaç="0"+str(sayaç)
        sutün15.append(sayaç)  

    sutün16=[]
    for i in kalfabe:
        sayaç=0  
        for j in range(0,len(sonuç)):
            if len(sonuç[j])>=16:
                if i==sonuç[j][15]:
                    sayaç+=1
                else:
                    pass
        if sayaç<10:
            sayaç="0"+str(sayaç)
        sutün16.append(sayaç)  

    sutün17=[]
    for i in kalfabe:
        sayaç=0  
        for j in range(0,len(sonuç)):
            if len(sonuç[j])>=17:
                if i==sonuç[j][16]:
                    sayaç+=1
                else:
                    pass
        if sayaç<10:
            sayaç="0"+str(sayaç)
        sutün17.append(sayaç)  

    sutün18=[]
    for i in kalfabe:
        sayaç=0  
        for j in range(0,len(sonuç)):
            if len(sonuç[j])>=18:
                if i==sonuç[j][17]:
                    sayaç+=1
                else:
                    pass
        if sayaç<10:
            sayaç="0"+str(sayaç)
        sutün18.append(sayaç)  

    sutün19=[]
    for i in kalfabe:
        sayaç=0  
        for j in range(0,len(sonuç)):
            if len(sonuç[j])>=19:
                if i==sonuç[j][18]:
                    sayaç+=1
                else:
                    pass
        if sayaç<10:
            sayaç="0"+str(sayaç)
        sutün19.append(sayaç)  

    sutün20=[]
    for i in kalfabe:
        sayaç=0  
        for j in range(0,len(sonuç)):
            if len(sonuç[j])>=20:
                if i==sonuç[j][19]:
                    sayaç+=1
                else:
                    pass
        if sayaç<10:
            sayaç="0"+str(sayaç)
        sutün20.append(sayaç)  

    myList=""
    for i in range(0,len(balfabe)):
        myList += balfabe[i]
        myList = "".join(myList)
        myList+="     "

        myList += str(sutün1[i])
        myList = "".join(myList)
        myList+="  "

        myList += str(sutün2[i])
        myList = "".join(myList)
        myList+="  "

        myList += str(sutün3[i])
        myList = "".join(myList)
        myList+="  "

        myList += str(sutün4[i])
        myList = "".join(myList)
        myList+="  "

        myList += str(sutün5[i])
        myList = "".join(myList)
        myList+="  "

        myList += str(sutün6[i])
        myList = "".join(myList)
        myList+="  "

        myList += str(sutün7[i])
        myList = "".join(myList)
        myList+="  "

        myList += str(sutün8[i])
        myList = "".join(myList)
        myList+="  "

        myList += str(sutün9[i])
        myList = "".join(myList)
        myList+="  "

        myList += str(sutün10[i])
        myList = "".join(myList)
        myList+="   "

        myList += str(sutün11[i])
        myList = "".join(myList)
        myList+="   "

        myList += str(sutün12[i])
        myList = "".join(myList)
        myList+="   "

        myList += str(sutün13[i])
        myList = "".join(myList)
        myList+="   "

        myList += str(sutün14[i])
        myList = "".join(myList)
        myList+="   "

        myList += str(sutün15[i])
        myList = "".join(myList)
        myList+="   "

        myList += str(sutün16[i])
        myList = "".join(myList)
        myList+="   "

        myList += str(sutün17[i])
        myList = "".join(myList)
        myList+="   "

        myList += str(sutün18[i])
        myList = "".join(myList)
        myList+="   "

        myList += str(sutün19[i])
        myList = "".join(myList)
        myList+="   "

        myList += str(sutün20[i])
        myList = "".join(myList)
        myList+="    "

        myList += str(toplam[i])
        myList = "".join(myList)
        if i<=20:
            myList+="\n"
        
        elif i>=21:
            print(myList)
            myList = ""
        else:
            pass  
    
def harfUzayı(arg):
    sonuç=result.upper()
    sonuç=sonuç.replace(" ","")
    liste=[]
    for i in sonuç:
        liste.append(i)
    random.shuffle(liste)
    
    a=1
    myString=""
    random_harfler=""
    for i in range(1,len(liste)):
        myString += liste[i]
        myString = "".join(myString)
        
        random_harfler += liste[i]
        random_harfler = "".join(random_harfler)

        myString+=" "
        myString = "".join(myString)

        random_harfler+=" "
        random_harfler = "".join(random_harfler)
        
        if i>=25*a:
            if a<=25:
                random_harfler+="\n"
                print(myString)
                myString = ""
                a+=1
            else:
                pass    
        else:
            pass        
    
    rows=random_harfler.splitlines()
    liste=list()
    for i in range(0,25):
        elements=rows[i].split(" ")
        liste.append(elements)
    
    kelime=[]
    satırNo=[]
    sütunNo=[]
    yönü=[]

    start=time.time()
    def sol_sağ():
        newResult1=result.upper()

        sonuçlar=newResult1.split(" ")
        sonuçlar=list(sonuçlar)
        sonuçlar.sort()

        for i in range(0,25):
            for j in range(0,16):
                string=""
                for k in range(0,10):
                    string+=liste[i][j+k]
                    string = "".join(string)
                    if string in sonuçlar:
                        if i+1<10:
                            sayii="0"+str(i+1) 
                            satırNo.append(sayii)
                        else:
                            satırNo.append(i+1)
                        if j+k+1-(len(string)-1)<10:
                            sayii="0"+str(j+k+1-(len(string)-1)) 
                            sütunNo.append(sayii)
                        else:
                            sütunNo.append(j+k+1-(len(string)-1))    
                        if len(string)<3:
                            string+=" "
                            kelime.append(string)
                        else:
                            kelime.append(string)
                        yönü.append("Doğu")           
        
        for i in range(0,16):
            for j in range(0,16):
                string=""
                for k in range(0,10):
                    string+=liste[i][24-j-k]
                    string = "".join(string)
                    if string in sonuçlar:
                        if i+1<10:
                            sayii="0"+str(i+1) 
                            satırNo.append(sayii)
                        else:
                            satırNo.append(i+1)
                        if 25-j<10:
                            sayii="0"+str(25-j) 
                            sütunNo.append(sayii)
                        else:
                            sütunNo.append(25-j)    
                        if len(string)<3:
                            string+=" "
                            kelime.append(string)
                        else:
                            kelime.append(string)
                        yönü.append("Batı")
    def aşağı_yukarı():
        newResult1=result.upper()

        sonuçlar=newResult1.split(" ")#!!!!!!!
        sonuçlar=list(sonuçlar)
        sonuçlar.sort()

        for i in range(0,16):
            for j in range(0,25):
                string=""
                for k in range(0,10):
                    string+=liste[i+k][j]
                    string = "".join(string)
                    if string in sonuçlar:
                        if i+1<10:
                            sayii="0"+str(i+1) 
                            satırNo.append(sayii)
                        else:
                            satırNo.append(i+1)
                        if j+1<10:
                            sayii="0"+str(j+1) 
                            sütunNo.append(sayii)
                        else:
                            sütunNo.append(j+1)    
                        if len(string)<3:
                            string+=" "
                            kelime.append(string)
                        else:
                            kelime.append(string)  
                        yönü.append("Güney") 

    def çapraz_ilk():
        newResult1=result.upper()

        sonuçlar=newResult1.split(" ")#!!!!!!!
        sonuçlar=list(sonuçlar)
        sonuçlar.sort()

        for i in range(0,16):
            for j in range(0,16):
                string=""
                for k in range(0,10):
                    string+=liste[i+k][j+k]
                    string = "".join(string)
                    if string in sonuçlar:
                        if i+1<10:
                            sayii="0"+str(i+1) 
                            satırNo.append(sayii)
                        else:
                            satırNo.append(i+1)
                        if j+1<10:
                            sayii="0"+str(j+1) 
                            sütunNo.append(sayii)
                        else:
                            sütunNo.append(j+1)    
                        if len(string)<3:
                            string+=" "
                            kelime.append(string)
                        else:
                            kelime.append(string)  
                        yönü.append("Güneydoğu")

    def çapraz_iki():
        newResult1=result.upper()

        sonuçlar=newResult1.split(" ")#!!!!!!!
        sonuçlar=list(sonuçlar)
        sonuçlar.sort()

        for i in range(0,16):
            for j in range(0,16):
                string=""
                for k in range(0,10):
                    string+=liste[i+k][24-j-k]
                    string = "".join(string)
                    if string in sonuçlar:
                        if i+1<10:
                            sayii="0"+str(i+1) 
                            satırNo.append(sayii)
                        else:
                            satırNo.append(i+1)
                        if 25-j<10:
                            sayii="0"+str(25-j) 
                            sütunNo.append(sayii)
                        else:
                            sütunNo.append(25-j)    
                        if len(string)<3:
                            string+=" "
                            kelime.append(string)
                        else:
                            kelime.append(string)
                        yönü.append("Güneybatı")

    sol_sağ()
    aşağı_yukarı()
    çapraz_ilk()
    çapraz_iki()

    end=time.time()

    print("\nKelime"+(" "*15)+"Satır No "+"Sütun No "+"Yönü\n"+("-"*20)+" "+("-"*8)+" "+("-"*8)+" "+("-"*9))
    
    myWords=""
    for i in range(0,len(kelime)):
        myWords += kelime[i]
        myWords = "".join(myWords)
        myWords+=" "*21

        myWords += str(satırNo[i])
        myWords = "".join(myWords)
        myWords+=" "*7

        myWords += str(sütunNo[i])
        myWords = "".join(myWords)
        myWords+=" "*4

        myWords += yönü[i]
        myWords = "".join(myWords)

        print(myWords)
        myWords+="\n"
        myWords = ""
        
    if len(kelime)==0 and len(satırNo)==0 and len(sütunNo)==0 and len(yönü)==0:
        print("HİÇBİR ŞEY BULUNAMADI")

    print("\nToplam Arama Zamanı: ",end-start)

print(justify(satir_genişliği,satırDüzenle()))
kelimeSayma(result)
harfSayma(result,balfabe,kalfabe)
harfUzayı(result)

# my_list = ""
# m=1
# a=1
# for i in result:
#         my_list += i
#         my_list = "".join(my_list)
#         my_list = my_list.split("-")
#         my_list = " ".join(my_list)    
        
#         if  m==((satir_genişliği)*a):
            
#             # for i in range(1,len(result)+1):
#             #     index1=satir_genişliği-(my_list.index(" ",i,i+1))
#             #     index2=satir_genişliği-((my_list.index(" "))*(i+1))
#             #     fark=(my_list.index(" "))-(my_list.index(" "))
#             #     if fark>index1:
#             #         print("")
#             #     else:
#             #         pass    
            
#             print(my_list.lstrip())
#             my_list = ""
#             a+=1
#         else:
#             pass
#         m+=1



