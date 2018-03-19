
import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)

Y1 = (1-X/(float(n)))*np.random.uniform(0.5,1.0,n)
Y2 = (1-X/(float(n)))*np.random.uniform(0.5,1.0,n)

plt.xlim(-5,n)
plt.xticks(())


plt.ylim(-1.25,1.25)
plt.yticks(())



plt.bar(X,+Y1 ,facecolor = 'pink' ,edgecolor = 'white')
plt.bar(X,-Y2 ,facecolor = 'cyan')

for x , y in zip(X,Y1):
    plt.text(x+0.2 ,y +0.05 , s = "%.2f" % y , ha = 'center' ,va = 'bottom')


plt.show()

