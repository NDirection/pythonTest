import  numpy as np

import  matplotlib.pyplot as plt


greyhouse = 500
labs = 50

grey_height = 28 + 4*np.random.rand(greyhouse)
lab_height = 24 + 4*np.random.rand(labs)

print(grey_height)

plt.hist([grey_height,lab_height],stacked= True ,color=['r','b'])

plt.show()