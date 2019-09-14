import wave
import numpy as np
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

for file in Path(".").glob("*.raw"):
    y = np.fromfile(str(file), dtype=">h").astype('int16')
    with wave.Wave_write(f"{file.stem}.wav") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(22050)
        w.writeframes(y)

    x = np.arange(len(y))
    plt.clf()
    plt.plot(x, y, label=file.stem)
    plt.legend(loc='upper right')
    plt.savefig(f"{file.stem}.png")
