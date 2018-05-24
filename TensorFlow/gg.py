# Just disables the warning, doesn't enable AVX/FMA
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'



import tensorflow as tf

hello = tf.constant('Hello,world!')

sess = tf.Session()

result = sess.run(hello)

sess.close()

print(result)