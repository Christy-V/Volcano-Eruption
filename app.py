from flask import Flask, jsonify, request,render_template
import numpy as np
import joblib
import pandas as pd
import librosa
import re
from scipy import signal
from numpy.fft import fft,fftshift,fftfreq
import logging

logging.basicConfig(filename='error.log',level=logging.ERROR,format='%(asctime)s:%(levelname)s:%(message)s')
import sys

import flask
app = Flask(__name__)  

@app.route('/')
def hello_world():
    return 'Your Clock Is Ticking'

@app.route('/index')
def index():
    return flask.render_template('index.html')



@app.route('/predict', methods=['POST'])

def predict():

    X=pd.DataFrame()
    sen=['sensor_1','sensor_2','sensor_3','sensor_4','sensor_5','sensor_6','sensor_7','sensor_8','sensor_9','sensor_10']
    dfa=pd.read_csv(request.form['csvfile'])

    col=dfa.columns
    size=len(col)
    return jsonify({'pred': size})


if __name__ == '__main__':
    app.run()
