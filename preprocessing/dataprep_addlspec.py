import sys
sys.path.append("../")

from utils import audio
from utils.misc import *

base_dir = sys.argv[1]
filenames = base_dir + "/" + sys.argv[2]
feats_dir = base_dir + "/feats2"
wav_dir = base_dir + '/wav'
assure_path_exists(feats_dir)

with open(filenames, encoding='utf-8') as f:
    ctr = 0
    for line in f:
        ctr += 1
        fname = line.strip()
        print("fname: ", fname)
        wav_fname = wav_dir + '/' + fname
        wav = audio.load_wav(wav_fname)
        spectrogram = audio.spectrogram(wav).astype(np.float32)
        lspec_fname = feats_dir + '/' + fname + '.feats'
        np.save(lspec_fname, spectrogram.T, allow_pickle=False)

        break
        if ctr % 100 == 0:
            print("Processed ", ctr, "lines")

print("done")
