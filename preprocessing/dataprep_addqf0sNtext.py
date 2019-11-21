import os, sys
FALCON_DIR= '/home/srallaba/projects/text2speech/repos/festvox/src/falcon/'
sys.path.append(FALCON_DIR)
import numpy as np
from utils import audio
from utils.misc import *
import re

'''Syntax
python3.5 $FALCONDIR/dataprep_addqf0sNtext.py scripts/txt.done.data.interpolatedtones .

'''

### Flags
generate_feats_flag = 0


tdd_file  = sys.argv[1]
vox_dir = sys.argv[2]
feats_dir = vox_dir + '/festival/falcon_textNqf0s'
assure_path_exists(feats_dir)

desc_file = vox_dir + '/etc/falcon_feats.desc'


def get_interpolated_tones(text, tones):
    print(text)
    print(tones)
    #sys.exit()
    print("The length of text and tones: ", len(text), len(tones))
    assert len(text.split()) == len(tones.split())
    interpolated_tones = []
    chars = []
    for (word, tone) in list(zip(text.split(), tones.split())):
        word = re.sub(r'[^\w\s]','',word)
        for char in word:
            interpolated_tones.append(char.lower() + '_' + tone )
        interpolated_tones.append('SPACE_SPACE' )
    return chars, interpolated_tones


f = open(tdd_file, encoding='utf-8')
ctr = 0
for line in f:
 if len(line) > 2:
    ctr += 1
    line = line.split('\n')[0]
    fname = line.split()[0].split('.')[0]
    words_tones = ' '.join(k for k in line.split()[1:]) 
    print(fname, words_tones)
    text = ' '.join(k.split('_')[0] for k in words_tones.split())
    tones = ' '.join(k.split('_')[1] for k in words_tones.split())
    text, tones = get_interpolated_tones(text, tones)
    if ctr % 100 == 1:
       print("Processed ", ctr, "lines")

    try:
      g = open(feats_dir + '/' + fname + '.feats', 'w')
      g.write( ' '.join(k for k in tones) +'\n')
      g.close()
    except UnicodeEncodeError:
      print(line)
      sys.exit()

g = open(desc_file, 'a')
g.write('textNqf0s|single|categorical' + '\n')
g.close()

