import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import numpy as np 
import matplotlib.pyplot as plt

#create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1+0.3

plt.figure()
plt.plot(x_data,y_data)
plt.show()

weights = tf.Variable(tf.random_uniform([1],-1.0,1.0))
bias = tf.Variable(tf.zeros([1]))

y = weights*x_data+bias

loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for step in range(2001):
    sess.run(train)
    if step%20 == 0:
        # y = weights*x_data+bias
        # plt.figure()
        # plt.plot(x_data,y_data)
        print(step,sess.run(weights),sess.run(bias))
#plt.show()