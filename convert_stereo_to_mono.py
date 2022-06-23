import numpy as np
import librosa
import soundfile as sf
import pathlib
import tensorflow as tf


DATAPATH = "clap"
output_path = "output"
data_dir = pathlib.Path(DATAPATH)
filenames = tf.io.gfile.glob(str(data_dir) + '/*')
print("NUMBER OF FILE :", len(filenames))


def single_image():
    single, sr = librosa.load("sterio.wav", mono=True)
    sf.write("mono.wav", single, sr)
    return single


def save_file():
    for y in filenames:
        signal, sr = librosa.load(y, mono=True)
        sf.write(output_path+"/"+y.split('.')
                 [0]+"_mono_channel.wav", signal, sr)
        print(y)


if __name__ == '__main__':
    # single_image()
    save_file()
