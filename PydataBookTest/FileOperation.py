import  numpy as np
import  numpy.random as randn



# arr = np.loadtxt("RawData.txt", delimiter=",")

# print(arr)



# print(arr)

# arr = np.array(arr+1,dtype=int)

# np.savetxt("RawData.txt", arr,fmt='%2.0f',delimiter=",")


position = 0

walk = [position]

# steps = 10000
#
# for i in range(steps):
#     step = 1 if randn.randint(-1,1) else -1
#
#     position += step
#
#     walk.append(position)
#
#
# print(walk)


nsteps = 1000

draws = np.random.randint(0,2,size = nsteps)


print(draws)

steps = np.where(draws >0,1,-1)

walk = steps.cumsum()

print(walk)

print(walk.min())

print(walk.max())