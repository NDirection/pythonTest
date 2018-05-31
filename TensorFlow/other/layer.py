import tensorflow as tf
import numpy as np
import  matplotlib.pyplot as plt

def add_layer(inputs ,in_size ,out_size , activation_function =None):


    Weight = tf.Variable(tf.random_normal([in_size,out_size]))

    biases = tf.Variable(tf.zeros([1,out_size])+0.1)

    Wx_plus = tf.matmul(inputs,Weight)+biases


    print("****")
    print(Wx_plus)
    print(biases)

    if activation_function is None:
        outputs = Wx_plus

    else:
        outputs = activation_function(Wx_plus)

    return  outputs



X_date = np.linspace(-1,1,300)[:,np.newaxis]

noise = np.random.normal(0,0.05,X_date.shape)

y_data = np.square(X_date)-0.5+noise

xs = tf.placeholder(tf.float32,[None,1])
ys = tf.placeholder(tf.float32,[None,1])

#add hidden layer
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)


# output layer
prediction = add_layer(l1,10,1)


loss = tf.reduce_mean(tf.reduce_sum(tf.square(y_data-prediction),reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()

sess = tf.Session()


sess.run(init)

print(X_date.shape)


fig = plt.figure()

ax = fig.add_subplot(1,1,1)
ax.scatter(X_date,y_data)

plt.ion()
plt.show()

for i in range(1000):


    # training
    sess.run(train_step, feed_dict={xs: X_date, ys: y_data})

    if i % 50 == 0:
        print(X_date.shape , X_date[0])

        # to see the step improvement
        print(sess.run(loss, feed_dict={xs: X_date, ys: y_data}))

        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        prediction_value = sess.run(prediction,feed_dict={xs: X_date})

        lines = ax.plot(X_date,prediction_value,'r-',lw =5)


       # plt.pause(5)

