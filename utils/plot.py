"""Trainining script for Tacotron speech synthesis model.

usage: plot.py [options]

options:
    --dir=<dir>         Directory contains preprocessed features.
    -h, --help                Show this help message and exit
"""
from docopt import docopt

import os, sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np



def plot_alignment(alignment, path, info=None):
  fig, ax = plt.subplots()
  im = ax.imshow(
    alignment,
    aspect='auto',
    origin='lower',
    interpolation='none')
  fig.colorbar(im, ax=ax)
  xlabel = 'Decoder timestep'
  if info is not None:
    xlabel += '\n\n' + info
  plt.xlabel(xlabel)
  plt.ylabel('Encoder timestep')
  plt.tight_layout()
  plt.savefig(path, format='png')


def visualize_f0_distribution(dir):

  files = sorted(os.listdir(dir))
  arr = []
  for file in files:
      A = np.loadtxt(dir + '/' + file, usecols=0)
      arr.append(A)
  arr = np.concatenate(arr, axis=0)
  plt.hist(arr, density=True, range=[10,max(arr)])
  plt.savefig('/tmp/f0.png', format='png')  


if __name__ == "__main__":
    args = docopt(__doc__)
    print("Command line args:\n", args)
    dir = args["--dir"]
    if dir is not None:
        visualize_f0_distribution(dir)
