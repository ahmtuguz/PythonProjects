import pandas as pd
import numpy as np
number=[5,8,9,2,3]
alfabe=["a","b","e","p","c"]
random_number=np.random.randint(0,100,5)
scalar=5
dict={"a":1,"b":2,"c":5,"d":9,"e":7}

pandas_series=pd.Series(random_number,["a","b","c","d","e"])
print(pandas_series["c"])
print(pandas_series[["c","e"]])
pandas_series=pd.Series(scalar,["a","b","c","d","e"])
pandas_series=pd.Series(dict)
pandas_series=pd.Series(number)

#pandas_series=pandas_series+50
#pandas_series=pandas_series+pandas_series
#pandas_series=pandas_series.max()
#pandas_series=pandas_series.min()
#pandas_series=pandas_series.argmax()
#pandas_series=np.square(pandas_series)
#pandas_series=pandas_series.ndim
#pandas_series=pandas_series.dtype
#pandas_series=pandas_series.shape
result=5<=pandas_series
#print(pandas_series[:2])
print(pandas_series)
print(pandas_series[result])