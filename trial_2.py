import tensorflow as tf
print("TensorFlow version:", tf.__version__)

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)  # Output layer
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)

test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print("\nTest accuracy:", test_acc)


import numpy as np

# Make predictions on test data
predictions = model.predict(x_test)

# Get predicted labels
predicted_labels = np.argmax(predictions, axis=1)

# Compare with true labels
correct_predictions = np.sum(predicted_labels == y_test)
total_samples = len(y_test)
accuracy = correct_predictions / total_samples

print("Test accuracy:", accuracy)

'''
breakdown of what’s happening:

Training Phase:
During training, the neural network learns to adjust its internal weights and biases.
It sees thousands of labeled examples 
(images of handwritten digits along with their corresponding labels) 
and learns to map the pixel values to the correct digit labels.
The loss function measures how far off the predictions are from the actual labels. 
The optimizer then adjusts the model’s parameters to minimize this loss.
Testing Phase:
After training, we evaluate the model’s performance using a separate set of data (the test set).
The test set contains images that the model has never seen before.
The model makes predictions for each test image and compares them to the true labels.
The accuracy (percentage of correct predictions) on the test set tells us how well the model 
generalizes to new, unseen data.
Generalization:
The goal is for the model to perform well on both the training data 
(which it has seen during training) and the test data (which it hasn’t seen).
If the model achieves high accuracy on the test set, it indicates good 
generalization—meaning it can recognize digits it hasn’t explicitly learned.
In summary, the neural network is being tested on its ability to recognize 
handwritten digits accurately. The better it performs on the test set, the more 
confident we are in its ability to handle real-world digit recognition tasks. 🤖🔢



'''