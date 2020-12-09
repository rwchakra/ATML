#!/bin/bash
#SBATCH --job-name=AdvTopicsMlREBIAS    	 # create a short name for your job
#SBATCH --nodes=1                # node count
#SBATCH --ntasks=1               # total number of tasks across all nodes
#SBATCH --cpus-per-task=1        # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --time=47:59:00          # total run time limit (HH:MM:SS)ii
#SBATCH --partition=tflow
#SBATCH --exclusive
#SBATCH --nodelist=icsnode09

source ~/.bashrc

python3 rebias/main_biased_mnist.py --root rebias/datasets --train-correlation 0.999 --outer_criterion RUBi --g_lambda_inner 0
python3 rebias/main_biased_mnist.py --root rebias/datasets --train-correlation 0.997 --outer_criterion RUBi --g_lambda_inner 0
python3 rebias/main_biased_mnist.py --root rebias/datasets --train-correlation 0.995 --outer_criterion RUBi --g_lambda_inner 0
python3 rebias/main_biased_mnist.py --root rebias/datasets --train-correlation 0.990 --outer_criterion RUBi --g_lambda_inner 0
python3 rebias/main_biased_mnist.py --root rebias/datasets --train-correlation 0.98 --outer_criterion RUBi --g_lambda_inner 0
python3 rebias/main_biased_mnist.py --root rebias/datasets --train-correlation 0.95 --outer_criterion RUBi --g_lambda_inner 0
python3 rebias/main_biased_mnist.py --root rebias/datasets --train-correlation 0.9 --outer_criterion RUBi --g_lambda_inner 0
python3 rebias/main_biased_mnist.py --root rebias/datasets --train-correlation 0.85 --outer_criterion RUBi --g_lambda_inner 0

python3 rebias/main_biased_mnist.py --root rebias/datasets --train-correlation 0.999 --outer_criterion RUBi --g_lambda_inner 0
python3 rebias/main_biased_mnist.py --root rebias/datasets --train-correlation 0.997 --outer_criterion RUBi --g_lambda_inner 0
python3 rebias/main_biased_mnist.py --root rebias/datasets --train-correlation 0.995 --outer_criterion RUBi --g_lambda_inner 0
python3 rebias/main_biased_mnist.py --root rebias/datasets --train-correlation 0.990 --outer_criterion RUBi --g_lambda_inner 0
python3 rebias/main_biased_mnist.py --root rebias/datasets --train-correlation 0.98 --outer_criterion RUBi --g_lambda_inner 0
python3 rebias/main_biased_mnist.py --root rebias/datasets --train-correlation 0.95 --outer_criterion RUBi --g_lambda_inner 0
python3 rebias/main_biased_mnist.py --root rebias/datasets --train-correlation 0.9 --outer_criterion RUBi --g_lambda_inner 0
python3 rebias/main_biased_mnist.py --root rebias/datasets --train-correlation 0.85 --outer_criterion RUBi --g_lambda_inner 0

python3 rebias/main_biased_mnist.py --root rebias/datasets --train-correlation 0.999 --outer_criterion RUBi --g_lambda_inner 0
python3 rebias/main_biased_mnist.py --root rebias/datasets --train-correlation 0.997 --outer_criterion RUBi --g_lambda_inner 0
python3 rebias/main_biased_mnist.py --root rebias/datasets --train-correlation 0.995 --outer_criterion RUBi --g_lambda_inner 0
python3 rebias/main_biased_mnist.py --root rebias/datasets --train-correlation 0.990 --outer_criterion RUBi --g_lambda_inner 0
python3 rebias/main_biased_mnist.py --root rebias/datasets --train-correlation 0.98 --outer_criterion RUBi --g_lambda_inner 0
python3 rebias/main_biased_mnist.py --root rebias/datasets --train-correlation 0.95 --outer_criterion RUBi --g_lambda_inner 0
python3 rebias/main_biased_mnist.py --root rebias/datasets --train-correlation 0.9 --outer_criterion RUBi --g_lambda_inner 0
python3 rebias/main_biased_mnist.py --root rebias/datasets --train-correlation 0.85 --outer_criterion RUBi --g_lambda_inner 0

