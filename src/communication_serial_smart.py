
"""
ASIGNACIÓN #2
TÓPICOS ESPECIALES DE CONTROL
PROFESOR: DR. VONG CHONG
FECHA: 15-11-2022
ESTUDIANTE: ANGEL HURTADO
"""

"""
Libraries to take audio recordings from Windows Microphone
"""
import wave
import pyaudio

"""
Libraries to process data
"""
import os
from matplotlib import pyplot as plt
import tensorflow as tf
import tensorflow_io as tfio
import librosa
import librosa.display
import IPython.display as ipd
import numpy as np


"""
Libraries to turn on leds.
"""
import time

import serial

"""
Bajando Modelo Previo entrenado
"""
new_model = tf.keras.models.load_model('./oofuntion_model')

#DEFINING DATA LOADING FUNCTION
def load_wav(filename):
    """
    This Function loads audio files in wav format to be decodified by tensorflow.
    """
    file_contents = tf.io.read_file(filename) #loading file
    wav, sample_rate = tf.audio.decode_wav(file_contents, desired_channels=1) #simplfying audio in one dimension representation
    #removes trailing axis
    wav = tf.squeeze(wav, axis=-1)
    sample_rate = tf.cast(sample_rate, dtype=tf.int64)
    #The signal goes from 44100 Hz to 16000hz - amplitude of the audio signal
    wav = tfio.audio.resample(wav, rate_in=sample_rate, rate_out=16000)
    return wav

def preprocess_2(sample,index):
    """
    This function converts audio_file to spectrogram.
    """
    sample = sample[0]
    zero_padding = tf.zeros([25000] - tf.shape(sample), dtype=tf.float32)
    wav = tf.concat([zero_padding, sample],0)
    spectrogram = tf.signal.stft(wav, frame_length=320, frame_step=32)
    spectrogram = tf.abs(spectrogram)
    spectrogram = tf.expand_dims(spectrogram, axis=2)
    return spectrogram

"""
Establishing Connection with Arduino UNO
"""
controller = serial.Serial('COM3', 9600, timeout=1)

"""
Variable to store audio characters array
"""
frames = [] #to store audio

while True:
    try:
        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)  
        controller.write(b'8\n')
        time.sleep(0.5)
        print('*********READY FOR RECORDING*********\n\n')
        for _ in range(1,100):
            data = stream.read(1024)
            frames.append(data)
        time.sleep(1)
        print('sali del loop')
        controller.write(b'9\n')

        """Analizing Recording"""
        stream.stop_stream()
        stream.close()
        audio.terminate()
        sound_file = wave.open("myrecording.wav", "wb")
        sound_file.setnchannels(1)
        sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        sound_file.setframerate(44100)
        sound_file.writeframes(b''.join(frames))
        sound_file.close()
        frames = [] #to store audio

        """Reading File"""
        print('THE FILE WILL BE PROCESSED')
        file_to_test = load_wav("myrecording.wav")
        audio_slices = tf.keras.utils.timeseries_dataset_from_array(file_to_test, file_to_test, sequence_length=25000, sequence_stride=25000, batch_size=1)
        audio_slices = audio_slices.map(preprocess_2)
        audio_slices = audio_slices.batch(1)
        prediction = (float(new_model.predict(audio_slices)))
        if(prediction>0.5):
            controller.write(b'1\n')
        else:
            controller.write(b'0\n')
        print(f'probability is {prediction}', '\n Now 2 Seconds will be to read prediction')
        time.sleep(1)
    except KeyboardInterrupt:
        controller.close()
        break
