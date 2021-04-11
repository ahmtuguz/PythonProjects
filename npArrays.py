import numpy as np

#matris=np.arange(1,100,3)
# matris=np.zeros(10)
# matris=np.ones(10)
# matris=np.linspace(0,10,5)
# matris=np.random.randint(10)
# matris=np.random.randn(2)
# result=np.arange(1,100,3)
# matris=result.reshape(11,3)
# matris=np.random.randint(0,100,10)
# print(matris)
# sonuc=matris.min()
# sonuc=matris.max()
# sonuc=matris.mean()
# sonuc=matris.argmax()
# print(sonuc)
#print(matris.sum(axis=1))
#print((matris.sum(axis=0)))

# arr1=np.arange(0,10)
# arr2=arr1.copy()
# arr2[0]=11
# print(arr1)
# print(arr2)

array1=np.random.randint(0,100,6)
array2=np.random.randint(0,100,6)

result=array1+array2
result=array1+50
result=array1*array2
result=np.tan(array1)
result=np.log(array2)

mresult1=array1.reshape(2,3)
mresult2=array2.reshape(2,3)
mresult=np.vstack((mresult1,mresult2))
mresult=np.hstack((mresult1,mresult2))

mresult=mresult2>50
mresult=mresult2[mresult]
print(mresult1)
print(mresult2)
print(mresult)
# print(array1)
# print(array2)
# print(result)