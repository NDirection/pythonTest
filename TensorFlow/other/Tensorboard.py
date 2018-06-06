import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


def add_layer(inputs,
              in_size,
              out_size,
              n_layer,
              activation_function=None):
    # define layer
    layer_name = 'layer%s'%n_layer
    with tf.name_scope(layer_name):

        with tf.name_scope('weights'):
            Weight = tf.Variable(tf.random_normal([in_size, out_size]), name='W')

            tf.summary.histogram(layer_name + '/weights', Weight)

        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)

            tf.summary.histogram(layer_name + '/biases', biases)

        with tf.name_scope('Wx_plus_b'):
            Wx_plus = tf.matmul(inputs, Weight) + biases

        if activation_function is None:
            outputs = Wx_plus

        else:
            outputs = activation_function(Wx_plus)

        tf.summary.histogram(layer_name + '/outputs', outputs)

        return outputs


# make some data
X_date = np.linspace(-1, 1, 300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, X_date.shape)
y_data = np.square(X_date) - 0.5 + noise

with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32, [None, 1], name='x_in')
    ys = tf.placeholder(tf.float32, [None, 1], name='y_in')

# add hidden layer
l1 = add_layer(xs, 1, 10, 1, activation_function=tf.nn.relu)

# output layer
prediction = add_layer(l1, 10, 1 ,2)

with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))
    tf.summary.scalar('loss', loss)

with tf.name_scope('train'):
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()

sess = tf.Session()

sess.run(init)

merged = tf.summary.merge_all()
writer = tf.summary.FileWriter("logs/", sess.graph)

for i in range(1000):

    # training
    sess.run(train_step, feed_dict={xs: X_date, ys: y_data})

    if i % 50 == 0:
        print(sess.run(loss, feed_dict={xs: X_date, ys: y_data}))
        rs = sess.run(merged,feed_dict={xs: X_date, ys: y_data})

        writer.add_summary(rs,i)