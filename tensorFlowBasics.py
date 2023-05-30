# TensorFlow Basics


# import tensorflow
import tensorflow as tf

x = tf.constant([[1., 2., 3.],
                 [4., 5., 6.]])
y = tf.constant([[1, 2, 3],
                 [4, 5, 6]])



print(x)
print(x.shape)
print(x.dtype)

print(y)
print(y.shape)
print(y.dtype)

xplusx = x+x
print(xplusx)


yplusy = y + y
print(yplusy)
print()

print(5*x)

print(10*y)

# Transposing x
print(tf.transpose(x))

# concating x 
print("Concatenation")

concatenation1 = tf.concat([x, x, x], axis=0)
print(concatenation1)

concatenation2 = tf.concat([x, x, x], axis=1)
print(concatenation2)
