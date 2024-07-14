import tensorflow as tf
import os
os.environ["TF_MIN_GPU_MULTIPROCESSOR_COUNT"]="2"
os.environ["CUDA_VISIBLE_DEVICES"]='0,1'

# Ensure TensorFlow sees both GPUs
gpus = tf.test.gpu_device_name()
print("Available GPUs: ", gpus)

# if gpus:
#     try:
#         # Set the dedicated GPU as visible (index 1 assuming it's the second GPU)
#         tf.config.experimental.set_visible_devices(gpus[0], 'GPU')
#         tf.config.experimental.set_memory_growth(gpus[0], True)
#     except RuntimeError as e:
#         print(e)

# Run a simple computation to verify GPU usage
with tf.device('GPU:0'):
    a = tf.constant([[1.0, 2.0], [3.0, 4.0]])
    b = tf.constant([[1.0, 1.0], [0.0, 1.0]])
    c = tf.matmul(a, b)

print(c)
