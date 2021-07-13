# import sys

# sys.path.append('/mnt/New_Volume/Work_From_Home/Croma_Campus/06262021/11_00_01_00_06262021/')

import pickle
sys.path.append('.')
from custom import converter,encode

model = pickle.load(open('/mnt/New_Volume/Work_From_Home/Croma_Campus/07132021/09_30_11_00_07132021/housing_linear.bin','rb'))

import numpy as np

# instance = [-122.23,37.88,41.0,880.0,129.0,322.0,126.0,8.3252,'NEAR BAY']


# model.predict([instance])

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    x_new = [x for x in request.form.values()]
    print(x_new)
    pred = model.predict([x_new])
    
    # return render_template('index.html', prediction = f'The prediction is $ {pred}' )
    return 'The prediction is $%f'%pred


if __name__ == '__main__':
    app.run(debug = True)

