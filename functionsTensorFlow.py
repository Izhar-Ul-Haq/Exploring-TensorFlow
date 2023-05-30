import tensorflow as tf

@tf.function
def my_func(x):
  print('Tracing.\n')
  return tf.reduce_sum(x)

x = tf.constant([1,2,4])
y = tf.constant([100,200,300])
sum = x+y
mul = x*y
print(my_func(x))
print(type(my_func))
print(my_func(y))


print(my_func(sum))
print(my_func(mul))