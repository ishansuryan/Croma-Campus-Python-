import pickle

model = pickle.load(open('/mnt/New_Volume/Work_From_Home/Croma_Campus/07132021/09_30_11_00_07132021/housing_linear.bin', 'rb'))

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST', 'GET'])
def predict():
    var = [x for x in request.form.values()]
    pred_val = model.predict([var])
    s = f'The Predicted house price is %f'%pred_val
    # return render_template('index.html', prediction = s)
    return s

if __name__ == '__main__':
    app.run(debug=True)