import  numpy as np
import  numpy.random as randn
import matplotlib.pyplot as plt


arr = np.arange(8)
arr = arr.reshape((4, 2))

print(arr)

arr = np.array([1,2,3,4,5])

print(arr.dtype)

arr = np.array([1.3,3.4])

print(arr)

arr = arr.astype(np.int32)

print(arr)

arr = np.arange(10)

print(arr)

arr = np.array([[1,2,3,4,5],[2,3,4,5,6]],dtype=np.float)

print(arr)

print(arr*arr)

arr = np.arange(10)

print(arr[5:8])

arr[5:8] = 99

print(arr)

kk = arr[4:8]

print(kk)

kk[1] = 8888

print(arr)


arr =  np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(arr[0])

arr[0] = 55

print(arr)

aar2 = np.array([[1,2,3,4,5],[2,3,4,5,6],[4,5,5,6,7]],dtype=np.float)

print(aar2)

print(aar2[:2])


print(aar2[1:,2:4])


data = randn.rand(7,4)
print(data)

names = np.array(['A','B','C','D','E','F','G'])

selector = (names == 'A') | (names == 'F')

print(data[selector,2:])

print(data)

data[data < 0.5] =1

print(data)


print("---------------------------")



arr = np.empty((8,4))
for i in range (8) :

    arr[i] = i

print(arr)

print(arr[[-3,-5,-7]])


arr = np.arange(32).reshape(8,4)

print(arr)

print(arr[[1,5,7,2],[0,3,1,2]])

print("----------------")

print(arr[[1,5,7,2]][:,[2,0,3,2]])

print("---------------------------")
print("---------------------------")



data = np.arange(15).reshape((3,5))
print(data)

print(data.T)

data = np.random.rand(6,3)

print(data)

print(np.dot(data.T,data))


data = np.arange(16).reshape((2,2,4))

print(data)

print("---------------------------")
print(data.transpose((1,0,2)))


print(data.swapaxes(1,2))


#  快速的な元素級配列関数

arr = np.arange(10)

print(arr)

print(np.sqrt(arr))

print(np.exp(arr))

x = np.random.rand(8)

print(x)

y = np.random.uniform(-1,1,8)

print(y)

print(np.maximum(x,y))

print("---------------------------")


data = np.arange(-5,5,0.01);

xs , ys = np.meshgrid(data,data)

print(xs, ys)

z = np.sqrt(xs**2 + ys**2 )

print(z)

# plt.imshow(z)

# plt.show()

xarr = np.array([1.1,1.2,1.3,1.4,1.5])

yarr = np.array([2.1,2.2,2.3,3.4,2.5])


cond = np.array([True,False,True,True,False])


result = np.where(cond,xarr,yarr)

print(result)


arr= np.random.randn(4,4)

print(arr)

print(np.where(arr > 0 ,2 ,-2))


arr = np.random.randn(5,4)

print(arr.mean())


print(arr.sum())

result = np.where(arr> 0  ,3 ,-1)

print(result)


print(result.sum(axis=1))

print(result.cumsum())

arr = np.random.randn(8)


print(arr)


arr.sort()

print(arr)


arr = np.arange(10)

print(arr)

np.save("some_array",arr)

st = np.load("some_array.npy")

print(st)

print("------------------===========---")



a = np.arange(1,10).reshape([1,9])

print(a)

print(a.shape)

a = a[:,np.newaxis,:]

print(a)


X_date = np.linspace(-1,1,300)[:,np.newaxis]


print(X_date.shape)





