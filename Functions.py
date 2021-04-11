# def factoriyel(number):
#     if not isinstance(number,int):
#         raise TypeError("Number must be integer")
#     if number<=0:
#         raise ValueError("Number must be zero or positive")
#     def inner_factoriyel(number):
#         if number==1:
#             return number
#         return number*inner_factoriyel(number-1)
#     return inner_factoriyel(number)
# try:
#     print(factoriyel(5))
# except Exception as ex:
#     print(ex)
#*****************************************************
# def üsAlma(number):
#     def inner_fonk(power):
#         return number**power
#     return inner_fonk
# two=üsAlma(5)
# three=üsAlma(4)
# print(three(4))
# print(two(3))
#*******************************************************
# def hesapEt(işlem_secimi):
#     def toplama(*args):
#         toplam = 0
#         for i in args:
#             toplam+=i
#         return toplam
#
#     def çarpma(*args):
#         çarpim = 1
#         for i in args:
#             çarpim *= i
#         return çarpim
#     if işlem_secimi=="toplama":
#         return toplama
#     else:
#         return çarpma
# işlem=hesapEt("toplama")
# print(işlem(8,5,6,9,4))
#
# işlem=hesapEt("çarpma")
# print(işlem(8,5,6,9,4))

#*****************************************************

def toplam(a,b):
    return a+b
def çıkarma(a,b):
    return a-b
def çarpma(a,b):
    return a*b

def işlem(f1,f2,f3,secim):
    if secim=="toplam":
        print(f1(5,10))
    elif secim=="çıkarma":
        print(f2(45,20))
    elif secim=="çarpma":
        print(f3(9,2))
işlem(toplam,çıkarma,çarpma,"toplam")
işlem(toplam,çıkarma,çarpma,"çıkarma")
işlem(toplam,çıkarma,çarpma,"çarpma")