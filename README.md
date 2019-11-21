## Sleep-Talking

### Download Dataset
1. Create `dataset` directory
2. Download and extract sleepiness dataset in it.
3. Get all the wav filenames in a text file (needed to process wav files). Change to `wav` directory and run command `ls -1a > filenames.txt`.
4. You should see all the filenames now in filenames.txt now.

### Extract linear spectrogram features
1. Go to preprocessing directory and run `python3 dataprep_addlspec.py ../dataset/ComParE2019_ContinuousSleepiness/ filenames.txt`
2. This will create .npy files in `feats` directory in the sleepiness dataset directory.
