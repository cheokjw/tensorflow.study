# The process of stopping the training when the model reached to a certain accuracy is called Call Backs

import tensorflow as tf
from tensorflow.keras.callbacks import Callback

# Initializing Callback class
class myCallBack(Callback):
    def on_epoch_end(self, epoch, logs = {}):
        # Giving us details about the logs for each epochs
        if(logs.get('accuracy') > 0.95):
            print("\nAccuracy reached 95%...... Cancelling Training......")
            self.model.stop_training = True

callbacks = myCallBack()

# As usual, handle data, create neural network, train, evaluate
# But the different part is the call back statement where it stops the training when the model's accuracy reached a certain value. 

model.fit(training_images, training_labels, epochs = 50, callbacks = [callbacks])

