import os, sys
FALCON_DIR= '/home/srallaba/projects/text2speech/repos/festvox/src/falcon/'
sys.path.append(FALCON_DIR)
import numpy as np
from utils import audio
from utils.misc import *
import re


'''Syntax
python3.5 $FALCONDIR/dataprep_addtones.py scripts/txt.done.data.interpolatedtones .

'''

### Flags
generate_feats_flag = 0


tdd_file  = sys.argv[1]
vox_dir = sys.argv[2]
feats_dir = vox_dir + '/festival/falcon_tones'
texts_dir = vox_dir + '/festival/falcon_text'
assure_path_exists(feats_dir)


desc_file = vox_dir + '/etc/falcon_feats.desc'



def get_interpolated_tones(text, tones):
    #print("I read ", text, tones)
    print(text)
    print(tones)
    #sys.exit()
    print("The length of text and tones: ", len(text), len(tones))
    assert len(text) == len(tones)
    interpolated_tones = []
    chars = []
    for (word, tone) in list(zip(text, tones)):
        for char in word:
            interpolated_tones.append(tone)
            chars.append(char)
            chars.append(' ')
            interpolated_tones.append(' SPACE ')
        interpolated_tones.append(' SPACE ')
        chars.append(' ')
    print("The length of text and tones: ", len(chars), len(interpolated_tones), chars)
    assert len(chars) == len(interpolated_tones)
    return chars, interpolated_tones
    sys.exit()


f = open(tdd_file, encoding='utf-8')
ctr = 0
for line in f:
 if len(line) > 2:
    ctr += 1
    #print(line)
    line = line.split('\n')[0]
    fname = line.split('|')[0].split('.')[0]
    print(fname)
    g = open(texts_dir + '/' + fname + '.feats')
    for l in g:
        text = l.split('\n')[0].split()
    tones = ['<'] + ''.join(k for k in line.split('|')[1:]).split() + ['>']
    #print(tones)
    #sys.exit()
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
g.write('tones|single|categorical' + '\n')
g.close()

