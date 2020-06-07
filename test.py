

from __future__ import division
import numpy as np
from scipy.io.wavfile import read
from LBG import EUDistance
from mel_coefficients import mfcc
from LPC import lpc
from train import training
import os
import sounddevice
import shutil
from scipy.io.wavfile import write


fs=44100
second=6
print("recording...")
record_voice=sounddevice.rec(int(second * fs), samplerate=fs,channels=2)
sounddevice.wait()
write("s1.wav",fs,record_voice)
newPath = shutil.move('s1.wav', 'test')


nSpeaker = 8
nfiltbank = 12
orderLPC = 15
(codebooks_mfcc, codebooks_lpc) = training(nfiltbank, orderLPC)
directory = os.getcwd() + '/test';
fname = str()
nCorrect_MFCC = 0
nCorrect_LPC = 0


def minDistance(features, codebooks):
    speaker = 0
    distmin = np.inf
    for k in range(np.shape(codebooks)[0]):
        D = EUDistance(features, codebooks[k,:,:])
        dist = np.sum(np.min(D, axis = 1))/(np.shape(D)[0]) 
        if dist < distmin:
            distmin = dist
            speaker = k
            
    return speaker
    

for i in range(nSpeaker):
    fname = '/s' + str(i+1) + '.wav'
    print('Now speaker ', str(i+1), 'features are being tested')
    (fs,s) = read(directory + fname)
    mel_coefs = mfcc(s,fs,nfiltbank)
    lpc_coefs = lpc(s, fs, orderLPC)
    sp_mfcc = minDistance(mel_coefs, codebooks_mfcc)
    sp_lpc = minDistance(lpc_coefs, codebooks_lpc)
    
    print('Speaker ', (i+1), ' in test matches with speaker ', (sp_mfcc+1), ' in train for training with MFCC')
    print('Speaker ', (i+1), ' in test matches with speaker ', (sp_lpc+1), ' in train for training with LPC')
    
    
file_path = input("Enter filename:- ")
if os.path.exists(file_path):
    os.remove(file_path)
else:
    print("File not found in the directory")

   
    
   


    