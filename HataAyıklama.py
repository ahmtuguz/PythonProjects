# def sorgula(password):
#     import re
#     if len(password)<7:
#         raise Exception("Parola en az 7 karakterden oluşmalı")
#     elif not re.search("[a-z]",password):
#         raise Exception("Parola küçük harf içermelidir.")
#     elif not re.search("[A-Z]",password):
#         raise Exception("Parola büyük harf içermelidir.")
#     elif not re.search("[0-9]",password):
#         raise Exception("Parola rakam içermelidir.")
#     elif not re.search("[@_$]",password):
#         raise Exception("Parola alpha numeric karakter içermelidir.")
#     elif re.search("\s",password):
#         raise Exception("Parola BOŞLUK içermemelidir.")
# password="1234567aA_"
# try:
#     sorgula(password)
# except Exception as ex:
#     print(ex)
# else:
#     print("Giriş başarılı.")
# finally:
#     print("Sistem başarıyla kapandı")

liste=["1","2","5a","10b","abc","50","10"]
for i in liste:
    try:
        result=int(i)
        print(result)
    except Exception:
        continue

