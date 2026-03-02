import tensorflow as tf
import numpy as np
model = tf.keras.models.load_model('CommentToxicity.h5')

loaded_model = tf.keras.models.load_model("model.h5")

result = loaded_model.predict(np.array([["hello tensorflow"]]))
print(result)

