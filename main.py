from numpy import ndarray
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Audio
import librosa
import librosa.display

data: ndarray
data, fs = librosa.load('teste.mp3', sr=44100)
Audio(data=data, rate=fs)

D = librosa.amplitude_to_db(np.abs(librosa.stft(data)))
librosa.display.specshow(D, x_axis='time', y_axis='linear', sr=fs, cmap='jet')
plt.xlabel('Time [s]')
plt.ylabel('Frequency [Hz]')
plt.colorbar(format='%+2.0f dB')

plt.interactive(False)
print(data.shape, fs)
plt.show()