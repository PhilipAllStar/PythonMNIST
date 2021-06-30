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
    # calculate validation loss and accuarcy
    val_loss, val_acc = model.evaluate(x_test, y_test)
    print(val_loss, val_acc)

def predict(testImg):
    model = load_model('Mnist')
    predictions = model.predict([testImg])

    #print the highest propability
    import numpy as np
    print(np.argmax(predictions[0]))







def predict2():
    model = load_model('Mnist')
    
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    #nomalize data
    x_train = tf.keras.utils.normalize(x_train, axis=1)
    x_test = tf.keras.utils.normalize(x_test, axis=1)

    predictions = model.predict([x_test])

    #print the highest propability
    import numpy as np
    print(np.argmax(predictions[0]))