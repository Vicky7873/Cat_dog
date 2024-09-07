from flask import Flask,render_template,request
from pathlib import Path
import tensorflow as tf
import os
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array

app = Flask(__name__)

model = tf.keras.models.load_model('data/training/model.keras')

@app.route('/')
def index():
    return render_template('index.html')


def load_and_prep_image(filename,img_shape=224):
    img = load_img(filename)
    img = img_to_array(img)
    img = img/255
    img = tf.image.resize(img,(img_shape,img_shape))
    return img

@app.route("/predict",methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        filename = load_and_prep_image(filename)
        filename = np.expand_dims(filename, axis=0)
        pred = model.predict(filename)
        pred_class = np.argmax(pred,axis=1)
        if pred_class[0] == 0:
            result = 'cat'
        else:
            result = 'dog'
        return render_template('index.html',prediction=result)

        

if __name__ == "__main__":
    app.run(debug=True,port=8080,host='0.0.0.0')