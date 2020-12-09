# ATML
Biased MNIST contains:

1) csv data file for all runs
2) slurm output files for all runs
3) job files for all runs
4) Plotting code 

ImageNet contains:

1) Code to gather dataset and remove corrupted ids
2) Code to generate 9class ImageNet
3) Job runs and slurm outputs

To Train, refer to README on original code:
https://github.com/clovaai/rebias

NOTE:
It may well be required to change the versions of torchvision and torch on their requirements.txt to the latest versions. Otherwise one could run into a cuda error. 
