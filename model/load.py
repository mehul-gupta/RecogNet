from keras.models import load_model
import tensorflow as tf
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.Session(config=config)

def init():
    model = load_model('digits_deeplearn.h5')
    graph = tf.get_default_graph()
    return model, graph