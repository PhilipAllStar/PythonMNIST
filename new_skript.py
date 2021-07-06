import tensorflow as tf
from tensorflow.python.framework.tensor_shape import disable_v2_tensorshape
from tensorflow.python.keras.saving.save import load_model

from PIL import Image

def train():
    mnist = tf.keras.datasets.mnist

    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    #nomalize data
    x_train = tf.keras.utils.normalize(x_train, axis=1)
    x_test = tf.keras.utils.normalize(x_test, axis=1)
    #train model
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=3)

    model.save('Mnist')
    print("Done with training :)")

def printLossNAcc():
    model = load_model('Mnist')

    mnist = tf.keras.datasets.mnist

    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    #nomalize data
    x_train = tf.keras.utils.normalize(x_train, axis=1)
    x_test = tf.keras.utils.normalize(x_test, axis=1)

    # calculate validation loss and accuarcy
    val_loss, val_acc = model.evaluate(x_test, y_test)
    print(val_loss, val_acc)

def predict(testImg):
    import numpy as np
    model = load_model('Mnist')
    img = testImg.convert('L').resize((28,28), Image.ANTIALIAS)
    img = np.array(img)
    img = img.astype('float32')
    img /= 255
    predictions = model.predict(img[None,:,:])
    return predictions[0]