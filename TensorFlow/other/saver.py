import tensorflow as tf
import  numpy as np
#####

# 先建立 W, b 的容器
W = tf.Variable(np.arange(6).reshape((2, 3)), dtype=tf.float32, name="weights")
b = tf.Variable(np.arange(3), dtype=tf.float32, name="baiase")

# 这里不需要初始化步骤 init= tf.initialize_all_variables()

saver = tf.train.Saver()
with tf.Session() as sess:
    # 提取变量
    saver.restore(sess, "test/save_net.ckpt")
    print("weights:", sess.run(W))
    print("baiase:", sess.run(b))



