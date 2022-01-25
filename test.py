import tensorflow as tf 
from tensorflow.keras import callbacks

class myCallBack(callbacks):
    def on_epoch_end(self, epoch, logs = {}):
        if (logs.get('accuracy') > 0.95):
            self.model.stop_training = True
            