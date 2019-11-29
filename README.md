## Sleep-Talking

### Download Dataset
1. Create `dataset` directory
2. Download and extract sleepiness dataset in it.
3. Get all the wav filenames in a text file (needed to process wav files). Change to `wav` directory and run command `ls -1a > filenames.txt`.
4. You should see all the filenames now in filenames.txt now.

### Extract linear spectrogram features
1. Go to preprocessing directory and run `python3 dataprep_addlspec.py ../dataset/ComParE2019_ContinuousSleepiness/ filenames.txt`
2. This will create .npy files in `feats` directory in the sleepiness dataset directory.



Docker commands:
docker pull srallaba/projects:projectEmfasys


AWS:
ssh -i speech.pem ubuntu@ec2-44-224-7-113.us-west-2.compute.amazonaws.com
source activate pytorch_p36

"Name: tensorflow
Version: 1.8.0"

bind '"\e[A":history-search-backward'
bind '"\e[B":history-search-forward'

export FALCONDIR=/home/ubuntu/speech-project/srallaba/projects/project_emphasis/repos/festvox/src/falcon

bin/model.py  
bin/util.py  
$FALCONDIR/model.py  
blocks.py  


Acoustic features in:
srallaba/projects/project_emphasis/voices/cmu_us_ljspeech/festival/

Baseline code used the tacotron model TacotronOneSeqwiseTones(TacotronOneSeqwise(TacotronOne))

n_mels = 80  # Number of Mel banks to generate


### Files, functions edited
In utils.misc.py:
1. def collate_fn_xspkmely_sleep(batch):
2. class PyTorchDataset_sleep(object):



