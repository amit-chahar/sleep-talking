import os, sys
FALCON_DIR= '/home/srallaba/projects/text2speech/repos/festvox/src/falcon/'
sys.path.append(FALCON_DIR)
import numpy as np
from utils import audio
from utils.misc import *
import re


'''Syntax
python3.5 $FALCONDIR/dataprep_addchars.py etc/tdd .

'''

tdd_file  = sys.argv[1]
vox_dir = sys.argv[2]
feats_dir = vox_dir + '/festival/falcon_chars'
assure_path_exists(feats_dir)

desc_file = vox_dir + '/etc/falcon_feats.desc'

f = open(tdd_file, encoding='utf-8')
ctr = 0
for line in f:
 if len(line) > 2:
    ctr += 1
    line = line.split('\n')[0]

    fname = line.split()[0]
    if ctr % 100 == 1:
       print("Processed ", ctr, "lines")
    text = re.sub(r'[^\w\s]','', ' '.join(k for k in line.split()[1:]))

    fname = line.split()[0]
    text = ' '.join(k.lower() for k in text.split())

    ### This is not a good fix - Sai Krishna 27 May 2019 #########
    # https://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20 
    text = text.encode('ascii', 'ignore').decode('ascii')
    text = '< ' + ' '.join(k for k in text) + ' >'  
    ##############################################################


    g = open(feats_dir + '/' + fname + '.feats', 'w')
    g.write(text + '\n')
    g.close()



g = open(desc_file, 'a')
g.write('chars|single|categorical' + '\n')
g.close()

