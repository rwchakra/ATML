#!/bin/bash
#SBATCH --job-name=AdvTopicsMlREBIAS    	 # create a short name for your job
#SBATCH --nodes=1                # node count
#SBATCH --ntasks=1               # total number of tasks across all nodes
#SBATCH --cpus-per-task=1        # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --time=47:59:00          # total run time limit (HH:MM:SS)ii
#SBATCH --partition=multi_gpu
#SBATCH --exclusive
#SBATCH --nodelist=icsnode42

module purge 

source ~/.bashrc

python3 download_9class_imagenet.py 
python3 rmfiles2.py

