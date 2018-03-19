
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-3,3,50)


y1 = 2*x+1

y2 = x**2

# plt.figure(num=1)
#
# plt.plot(x,y1);


plt.figure(num=2)
plt.plot(x,y2)

plt.plot(x,y1,color="red", linestyle="--")

plt.xlim((-10,10))
plt.ylim((-10,10))

plt.xlabel("good")
plt.ylabel("test")

new_ticks = np.linspace(-10,10,21)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks(new_ticks)


ax = plt.gca()

ax.spines['right'].set_color('red')

ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")


# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')
# ax.spines['bottom'].set_position(('data',-1))
# ax.spines['left'].set_position(('data',0.5))

plt.show()

