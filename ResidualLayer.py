import tensorflow as tf

class ResidualLayer(tf.keras.layers.Layer):
    def __init__(self, module):
        super().__init__()
        self.module = module
    
    def call(self, input_tensor, training=False):
        shortcut = input_tensor
        return tf.keras.layers.Add()([self.module(input_tensor), shortcut])
  
    # def __init__(self, kernel_size, filters):
    #     super(ResnetIdentityBlock, self).__init__(name='')
    #     filters1, filters2, filters3 = filters

    #     self.conv2a = tf.keras.layers.Conv2D(filters1, (1, 1))
    #     self.bn2a = tf.keras.layers.BatchNormalization()

    #     self.conv2b = tf.keras.layers.Conv2D(filters2, kernel_size, padding='same')
    #     self.bn2b = tf.keras.layers.BatchNormalization()

    #     self.conv2c = tf.keras.layers.Conv2D(filters3, (1, 1))
    #     self.bn2c = tf.keras.layers.BatchNormalization()

    # def call(self, input_tensor, training=False):
    #     x = self.conv2a(input_tensor)
    #     x = self.bn2a(x, training=training)
    #     x = tf.nn.relu(x)

    #     x = self.conv2b(x)
    #     x = self.bn2b(x, training=training)
    #     x = tf.nn.relu(x)

    #     x = self.conv2c(x)
    #     x = self.bn2c(x, training=training)
    #     x += input_tensor
    #     return tf.nn.relu(x)


# block = ResnetIdentityBlock(2, [1, 2, 3])
# print(block(tf.ones([1, 2, 3, 3])))
# print(block.submodules)
