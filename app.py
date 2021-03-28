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

    if size < 10:
        logging.error('Need 10 Sensor Reading For Prediction')
        return flask.render_template('less_feat.html')
        sys.exit()
    
    #Drooping the least important features (analysed via EDA)
    for i in sen:
        dfa[i]=dfa[i].fillna(0)
        s_arr = dfa[i].to_numpy()
        #sum of signal values
        X.loc[0,'{}_sum'.format(i)]=np.sum(s_arr)
        #mean of signal values
        X.loc[0,'{}_mean'.format(i)]=np.mean(s_arr)
        #max of signal values
        X.loc[0,'{}_max'.format(i)]=np.max(s_arr)
        #min of signal values
        X.loc[0,'{}_min'.format(i)]=np.min(s_arr)
        #std of signal values
        X.loc[0,'{}_std'.format(i)]=np.std(s_arr)
        #difference between min and maximum
        X.loc[0,'{}_diff_min_max'.format(i)]=np.max(s_arr)-abs(np.min(s_arr))
        #difference between min and mean
        X.loc[0,'{}_diff_mean_max'.format(i)]=np.max(s_arr)-abs(np.mean(s_arr))
        #quantile values
        X.loc[0,'{}_quantile25'.format(i)]=np.quantile(s_arr,.25)
        X.loc[0,'{}_quantile50'.format(i)]=np.quantile(s_arr,.50)
        X.loc[0,'{}_quantile75'.format(i)]=np.quantile(s_arr,.75)
        X.loc[0,'{}_quantile99'.format(i)]=np.quantile(s_arr,.99)
        # mean of few intervals
        X.loc[0,'{}_mean_10000'.format(i)]=np.mean(s_arr[:10000])
        X.loc[0,'{}_mean_10000l'.format(i)]=np.mean(s_arr[-10000:])
        X.loc[0,'{}_std_10000'.format(i)]=np.std(s_arr[:10000])
        X.loc[0,'{}_std_10000l'.format(i)]=np.std(s_arr[-10000:])
        X.loc[0,'{}_RMSE'.format(i)]=np.sqrt(np.mean(np.square(s_arr)))
        X.loc[0,'{}_ZCR'.format(i)]=(((s_arr[:-1]*s_arr[1:])<0).sum()) 
        #We are calculating gradients to detect the changes in the signal incuding any sudden changesin the reading
        X.loc[0,'{}_mean_grad'.format(i)]=np.mean(np.gradient(s_arr))
        X.loc[0,'{}_rolling_mean_100'.format(i)]=np.mean(dfa[i].rolling(100, win_type ='hann').mean())
        X.loc[0,'{}_rolling_mean_1000'.format(i)]=np.mean(dfa[i].rolling(1000, win_type ='hann').mean())
        X.loc[0,'{}_rolling_max_100'.format(i)]=np.max(dfa[i].rolling(100, win_type ='hann').sum())
        X.loc[0,'{}_rolling_min_100'.format(i)]=np.min(dfa[i].rolling(100, win_type ='hann').sum())

        #Frequency Features
        amp=fft(s_arr)
        ramp=np.real(amp)
        fq=fftfreq(len(s_arr), 0.01)
        amp1=abs(amp)
        fq1=abs(fq)
        fq_pow=dict(zip(fq1,amp1))
        # fft mean
        X.loc[0,'{}_fft_mean'.format(i)]=np.mean(abs(amp))
        # fft real mean
        X.loc[0,'{}_rfft_mean'.format(i)]=np.mean(abs(ramp))
        # fft standard deviation
        X.loc[0,'{}_fft_std'.format(i)]=np.std(abs(amp))
        # fft real standard deviation
        X.loc[0,'{}_rfft_std'.format(i)]=np.std(abs(ramp))
        # fft maximum amplitude
        X.loc[0,'{}_fft_max'.format(i)]=np.max(abs(amp))
        # fft max real amplitude
        X.loc[0,'{}_rfft_max'.format(i)]=np.max(abs(ramp))
        # fft minimum amplitude
        X.loc[0,'{}_fft_min'.format(i)]=np.min(abs(amp))
        # fft minimum real amplitude
        X.loc[0,'{}_rfft_min'.format(i)]=np.min(abs(ramp))
        # fft RMSE
        X.loc[0,'{}_fft_RMSE'.format(i)]=abs(np.sqrt(np.mean(np.square(amp))))
        # fft real RMSE
        X.loc[0,'{}_rfft_RMSE'.format(i)]=np.sqrt(np.mean(np.square(ramp)))
        # Spectral Centroid
        #http://man.hubwiz.com/docset/LibROSA.docset/Contents/Resources/Documents/generated/librosa.feature.spectral_centroid.html
        X.loc[0,'{}_spectral_centroid'.format(i)]=np.mean(librosa.feature.spectral_centroid(y=s_arr,sr=100)[0])
        #Spectral Roll Off
        #http://man.hubwiz.com/docset/LibROSA.docset/Contents/Resources/Documents/generated/librosa.feature.spectral_rolloff.html
        X.loc[0,'{}_spectral_rolloff'.format(i)]=np.mean(librosa.feature.spectral_rolloff(y=s_arr,sr=100)[0])
        # Spectral Bandwidth
        # http://man.hubwiz.com/docset/LibROSA.docset/Contents/Resources/Documents/generated/librosa.feature.spectral_bandwidth.html
        X.loc[0,'{}_spectral_bandwidth'.format(i)]=np.mean(librosa.feature.spectral_bandwidth(y=s_arr,sr=100)[0])
        f, t, Z = signal.stft(s_arr, fs = 100, window = 'hann', nperseg = 256)
        rZ=np.real(Z)
        # sum of components alon time axis
        rZ=abs(rZ.sum(axis=1))
        Z=abs(Z.sum(axis=1))
        fq_pow=dict(zip(f,Z))
        X.loc[0,'{}_sum_stft'.format(i)] =np.sum(Z)
        X.loc[0,'{}_mean_stft'.format(i)] =np.mean(Z)
        X.loc[0,'{}_stft_RMSE'.format(i)]=np.sqrt(np.mean(np.square(Z))) 
        X.loc[0,'{}_max_stft'.format(i)] =np.max(Z)
        X.loc[0,'{}_min_stft'.format(i)] =np.min(Z)
        X.loc[0,'{}_max_rstft'.format(i)] =np.max(rZ)
        X.loc[0,'{}_min_rstft'.format(i)] =np.min(rZ)
        X.loc[0,'{}_rsum_stft'.format(i)] =np.sum(rZ)
        X.loc[0,'{}_rmean_stft'.format(i)] =np.mean(rZ)
        X.loc[0,'{}_rstft_RMSE'.format(i)]=np.sqrt(np.mean(np.square(rZ)))    
        #STFT separating the volcanoes based on their frequencies
        #https://dsp.stackexchange.com/questions/55889/how-to-extract-frequency-bands-from-short-time-fourier-transform 
        X.loc[0,'{}_A_stft_pow'.format(i)] =np.sum(list( value for (key, value) in fq_pow.items() if key >=10 ))
        X.loc[0,'{}_BH_stft_pow'.format(i)] =np.sum(list( value for (key, value) in fq_pow.items() if key >=5 and key <=8 ))
        X.loc[0,'{}_BL_stft_pow'.format(i)] =np.sum(list( value for (key, value) in fq_pow.items() if key >=1.5 and key <=2.5 ))
        X.loc[0,'{}_C_stft_pow'.format(i)] =np.sum(list( value for (key, value) in fq_pow.items() if key >=0.6 and key <=1.2 ))
        X.loc[0,'{}_D_stft_pow'.format(i)] =np.sum(list( value for (key, value) in fq_pow.items() if key >=2 and key <=4 ))  

        #Mel Features
        mfcc=librosa.feature.mfcc(y=s_arr, sr=0.01)
        mean_mfcc=np.mean(mfcc,axis=1)
        delta_mfcc=librosa.feature.delta(mfcc)
        mean_delta=np.mean(delta_mfcc,axis=1)
        delta2_mfcc=librosa.feature.delta(mfcc,order=2)
        mean_delta2=np.mean(delta2_mfcc,axis=1)   
        # We taking the mean of 20  features of MFCC ,its 1st and @nd derivatives
        #https://dsp.stackexchange.com/questions/38830/whats-the-correct-graphical-interpretation-of-a-series-of-mfcc-vectors
        #https://www.youtube.com/watch?v=WJI-17MNpdE
        for j in range(0, len(mfcc)):
            X.loc[0,'{}_mfcc_{}_mean'.format(i,j)] = mean_mfcc[j]
            X.loc[0,'{}_delta_mfcc_{}_max'.format(i,j)] = mean_delta[j]
            X.loc[0,'{}_delta2_mfcc_{}_max'.format(i,j)] = mean_delta2[j] 
    X=X.reset_index()  
    X.drop(columns=["index"],inplace=True)
    print(X)
    #loading Minmax file
    loaded_model =joblib.load('minmax.sav')
    scaled=loaded_model.transform(X)
    X = pd.DataFrame(scaled, columns =X.columns.values)
    #Selecting Best Features
    loaded_model1 = joblib.load('Kbest.sav')
    scores=pd.DataFrame(loaded_model1.scores_)
    columns=pd.DataFrame(X.columns)
    ft_score_df=pd.concat([columns,scores],axis=1)
    ft_score_df.columns=["Name","Score"]      
    ft_score_df=ft_score_df.nlargest(500,"Score")
    rd_columns = list(ft_score_df["Name"])
    X_rd=X[rd_columns]

    # loading LGBM with selected Features
    loaded_model2 = joblib.load('lgbm.sav')
    y_pred = loaded_model2.predict(X_rd)
    return jsonify({'pred': y_pred[0]})




if __name__ == '__main__':
    app.run()
