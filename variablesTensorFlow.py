import tensorflow as tf

# Normal tf.Tensor objects are immutable. To store model weights 
# (or other mutable state) in TensorFlow use a tf.Variable.

var = tf.Variable([0.0, 0.0, 0.0])

print(var)
var.assign([1, 2, 3])
print(var)

var.assign_add([1,1,1])
print(var)

