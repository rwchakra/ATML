# ATML
This repository contains ancilliary code for analysis on the ReBias paper by Bahng et al. (2019), for the Fall 2020 course Advanced Topics in Machine Learning. 

Authors:
Rwiddhi Chakraborty
Shubhayu Das

Biased MNIST contains:

1) csv data file for all runs
2) slurm output files for all runs
3) job files for all runs
4) Plotting code 

ImageNet contains:

1) Code to gather dataset and remove corrupted ids 
2) Job runs (job_download_imagenet.sh added runs both 'download_9class_imagenet.py' and 'rmfiles2.py' sequentially)
3) Seperate slurm output files for download_9class_imagenet,rmfiles2,rebias_training,vanilla_and_bias_training

To Train, refer to README on original code:
https://github.com/clovaai/rebias

NOTE:
It may well be required to change the versions of torchvision and torch on their requirements.txt to the latest versions. Otherwise one could run into a cuda error. 

@inproceedings{bahng2019rebias,
    title={Learning De-biased Representations with Biased Representations},
    author={Bahng, Hyojin and Chun, Sanghyuk and Yun, Sangdoo and Choo, Jaegul and Oh, Seong Joon},
    year={2020},
    booktitle={International Conference on Machine Learning (ICML)},
}
