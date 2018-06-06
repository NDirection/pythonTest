import  numpy as np
import  pandas as pd
from pandas import  Series,DataFrame



obj = Series([11,21,31,41])

print(obj)

print(obj.values)


obj = Series(data=[11,2,1,3],index=['a','b','c','d'])

print(obj)


print(Series(obj,['b','a']))



sdata = {'a':1,'b':2,'c':3}

obj3 = Series(sdata)


print(sdata)


obj4 = Series(sdata,{'a','e','c'})

print(obj4)

print("----------")

print(pd.isnull(obj4))


print(obj4+obj3)





print("======================")

data = {'state':['a','b','c'] , 'year':[200,300,400],'pop':[1.5,2.3,5.4]}

frame = DataFrame(data ,columns=['state','year','pop','kk'] ,index=['a','b','c'])


print(frame)

frame['kk'] = np.arange(1,stop = 4, step= 1)

print(frame)


frame['kk'] = Series([1,3] , index= ['a','c'])

print(frame)



df1 = DataFrame(np.arange(12.).reshape((3,4)),columns=list('abcd'))
df2 = DataFrame(np.arange(20.).reshape((4,5)),columns=list('abcde'))

print(df1.add(df2,fill_value = 0))
print(df2)


frame = DataFrame(np.random.randn(4,3) ,columns=list('abc') ,index=['q','w','e','r'])

print(frame)


f = lambda x :x.max() - x.min()

print(frame.apply(f ,axis=1))
