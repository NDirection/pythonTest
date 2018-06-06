import tensorflow as tf
import numpy as np


#create data
X_data = np.random.rand(100).astype(np.float)

print(X_data)

y_data = X_data*0.1 + 0.3

print("yyyyy")

print(y_data)

#create tensorflow structre star##


Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0))

biases = tf.Variable(tf.zeros([1]))

#create tensorflow structre end##

y = Weights*X_data + biases

loss = tf.reduce_mean(tf.square(y-y_data))

optim = tf.train.GradientDescentOptimizer(0.5)

train = optim.minimize(loss)

init = tf.global_variables_initializer()


sess = tf.Session()

sess.run(init)

for step in range(201):

    sess.run(train)

    if step % 20 == 0:

        print(step,sess.run(Weights),sess.run(biases))