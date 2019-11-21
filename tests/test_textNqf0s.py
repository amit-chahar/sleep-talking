import sys, os
from os.path import dirname, join
import json

### This is not supposed to be hardcoded #####
FALCON_DIR = os.environ.get("FALCONDIR")
sys.path.append(FALCON_DIR)
##############################################


from utils import audio
from utils.plot import plot_alignment
from tqdm import tqdm, trange
from utils.misc import *


charids = make_charids_tdd( 'etc/txt.done.data.tacotron')
charids['UNK']
charids['SPACE']
charids['0.0']
charids['1.0']
charids['2.0']
charids['3.0']
charids['4.0']
charids['5.0']
charids['6.0']
charids['7.0']



'''Old
feats_name = 'text'
X = CategoricalDataSource('fnames.train', 'etc/falcon_feats.desc', feats_name, 'festival/falcon_' + feats_name, charids)
feats_name = 'lspec'
Y = FloatDataSource('fnames.train', 'etc/falcon_feats.desc', feats_name, 'festival/falcon_' + feats_name)
feats_name = 'mspec'
Mel = FloatDataSource('fnames.train', 'etc/falcon_feats.desc', feats_name, 'festival/falcon_' + feats_name)
feats_name = 'tones'
tones = CategoricalDataSource('fnames.train', 'etc/falcon_feats.desc', feats_name, 'festival/falcon_' + feats_name, charids)
print(dict(X.get_dict()))
'''

fnamesdataset = FileNameDataSource('fnames.train')
feats_name = 'textNqf0s'
X = CategoricalDataSource_fnames_tones(fnamesdataset, 'etc/falcon_feats.desc', feats_name, 'festival/falcon_' + feats_name, charids)
feats_name = 'lspec'
Y = FloatDataSource('fnames.train', 'etc/falcon_feats.desc', feats_name, 'festival/falcon_' + feats_name)
feats_name = 'mspec'
Mel = FloatDataSource('fnames.train', 'etc/falcon_feats.desc', feats_name, 'festival/falcon_' + feats_name)

dataset = PyTorchDataset(X, Mel, Y)
dataloader = DataLoader(dataset,
                          batch_size=2,
                          shuffle=True,
                          num_workers=0,
                          collate_fn=collate_fn_xspkmely
                          )

id2char = {v:k for (k,v) in charids.items()}

for (x, tones, input_lengths, mel, y) in dataloader:

    #print("Shapes of x and tones: ", x.shape, tones.shape, x, tones)
    text = x[0,:].cpu().numpy()
    tone = tones[0,:].cpu().numpy()
    print(''.join(id2char[k] for k in text))
    print(' '.join(id2char[k] for k in tone))
    assert len(text) == len(tone)
    sys.exit()


