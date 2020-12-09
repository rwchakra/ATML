#!/bin/bash
#SBATCH --job-name=AdvTopicsMlREBIAS             # create a short name for your job
#SBATCH --nodes=1                # node count
#SBATCH --ntasks=1               # total number of tasks across all nodes
#SBATCH --cpus-per-task=1        # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --time=47:59:00          # total run time limit (HH:MM:SS)ii
#SBATCH --partition=gpu
#SBATCH --exclusive
#SBATCH --nodelist=icsnode12

module purge

source ~/.bashrc

python3 main_imagenet.py --train_root imagenet9class/train --val_root imagenet9class/val --imageneta_root imagenet-a --batch_size 16 --optim AdamP 
