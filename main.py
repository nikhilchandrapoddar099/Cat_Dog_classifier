
import pickle
from keras.preprocessing import image
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def student():
   return render_template('home.html')
@app.route('/result',methods = ['POST', 'GET'])

def fun1():
   if request.method == 'POST':
      result1= request.form["message"]
      with open('model_pickle', 'rb') as f1:
         model = pickle.load(f1)
      test_image = image.load_img(result1, target_size=(64, 64))
      test_image = image.img_to_array(test_image)
      test_image = np.expand_dims(test_image, axis=0)
      result = model.predict(test_image)

      if result[0][0] == 1:
          prediction = 'dog'
      else:
          prediction = 'cat'
      d = {}
      d[1] = prediction


      return render_template("result.html",result = d)


if __name__ == '__main__':
   app.run(host="127.0.0.1",port=8080,debug=True)