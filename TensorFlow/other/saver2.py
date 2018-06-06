import tensorflow as tf
import  numpy as np

W = tf.Variable([[1,3,4],[2,3,4]] ,dtype= tf.float32 ,name= "weights")

b = tf.Variable([1,3,3],dtype= tf.float32 ,name= "baiase")

init = tf.initialize_all_variables()

saver = tf.train.Saver()

sess = tf.Session()

sess.run(init)

save_path = saver.save(sess,"test/save_net.ckpt")
print(save_path)
