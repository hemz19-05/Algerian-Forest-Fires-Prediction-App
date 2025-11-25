from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

#import ridge reg and std scaler pickle
ridge_model = pickle.load(open('model/ridg.pkl', 'rb'))
stdscaler = pickle.load(open('model/scaler.pkl', 'rb'))


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method=='POST':
        Temperature=float(request.form.get('Temperature'))
        RH=float(request.form.get('RH'))
        Ws=float(request.form.get('Ws'))
        Rain=float(request.form.get('Rain'))
        FFMC=float(request.form.get('FFMC'))
        DMC=float(request.form.get('DMC'))
        ISI=float(request.form.get('ISI'))
        Classes=float(request.form.get('Classes'))
        Region=float(request.form.get('Region'))
        
             
        X=np.array([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])

        X_scaled=stdscaler.transform(X)

        preds=ridge_model.predict(X_scaled)

        return render_template('home.html', results=round(preds[0], 3))

    else:
        return render_template('home.html', result=None)


if __name__=='__main__':
    app.run(host='0.0.0.0')


