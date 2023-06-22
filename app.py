import pickle
import numpy as np
from flask import Flask, render_template, request,jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():

    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

    championship_rank = request.form['championshipRank']
    # additional_input = request.form['additionalInput']
    try:
        soft_data= []
        rough_data = championship_rank.split(',')
        for item in rough_data:
            if (item =='R')|(item =='D')|(item == ''): 
                soft_data.append(100)
            else:
                soft_data.append(int(item))
        m = sum(soft_data)/len(soft_data)
        std = np.std(soft_data)
        sn = len(soft_data)
        # r = additional_input
        br = min(soft_data)

        model_input = [[m,std,sn,br]]
        prediction = model.predict(model_input)[0][0]
        prediction = np.round(prediction,3) * 100
        response = {'prediction': prediction}
        return jsonify(response)
    except Exception as e:
        error_message = str(e)
        return jsonify({'error': error_message}), 500

@app.route('/other_page')
def other_page():
    return render_template('other_page.html')

if __name__ == '__main__':
    app.run(debug=True)