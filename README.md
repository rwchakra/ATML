# ATML
This repository contains ancilliary code for analysis on the ReBias paper by Bahng et al. (2020), for the Fall 2020 course Advanced Topics in Machine Learning. 

Authors:
Rwiddhi Chakraborty
Shubhayu Das


## Biased MNIST contains:

1) csv data file for all runs
2) job files for all runs
3) Plotting code 

## ImageNet contains:

1) Code to gather dataset and remove corrupted ids 
2) Job runs (job_download_imagenet.sh added runs both 'download_9class_imagenet.py' and 'rmfiles2.py' sequentially)
3) Seperate slurm output files for download_9class_imagenet,rmfiles2,rebias_training,vanilla_and_bias_training

## To Train, refer to README on original code:
https://github.com/clovaai/rebias


## A sample ImageNet training command : 

python main_imagenet.py --train_root /path/to/your/imagenet/train
    --val_root /path/to/your/imagenet/val
    --imageneta_root /path/to/your/imagenet_a
    --optim AdamP

## Important hyperparameters:
1) Batch Size (256 for Biased MNIST; 128 for ImageNet)  , Optimizer Parameters (Default Biased MNIST : Type = Adam, Learning Rate = 0.001 ; Default InageNet : Type = AdamP, Learning Rate = 0.001)
2) f_lambda_outer=1, g_lambda_inner=1 : These are factors the HSIC is multiplied with when optimizing for the 'f' and the 'g' model respectively. For vanilly and biased training both of these are set to 0. For RUBi and LearnedMixin the g_lambda_inner should be set to 0.
3) rbf_sigma_x = 1, rbf_sigma_y = 1:  These are hyperparamets specifically for the Radial Basis Function Kernel radius usied in computing the HSIC. For Biased MNIST these are fixed to 1. For ImageNet these are updated every epoch based on the median of f(x) and g(x), with 25% of the training data chosen randomly.



NOTE:
It may well be required to change the versions of torchvision and torch on their requirements.txt to the latest versions. Otherwise one could run into a cuda error.

Inorder to run jobs with the modified trainer, which atrificially increases the batch size, import the trainer_with_gradient_accumulation.py file instead for the traininer.py in the main_imagenet.py file on the original repository. 

@inproceedings{bahng2019rebias,
    title={Learning De-biased Representations with Biased Representations},
    author={Bahng, Hyojin and Chun, Sanghyuk and Yun, Sangdoo and Choo, Jaegul and Oh, Seong Joon},
    year={2020},
    booktitle={International Conference on Machine Learning (ICML)},
}
