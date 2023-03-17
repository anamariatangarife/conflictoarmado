#!/bin/bash
#SBATCH -J Tesis_conflicto_Armado
#SBATCH -p high
#SBATCH -N 1
#SBATCH --mem=16G
#SBATCH --gres=gpu:1
#SBATCH --chdir=/homedtcl/atangarife/conflictoarmado/slurm
#SBATCH -o slurm.%N.%J.%u.out # STDOUT
#SBATCH -e slurm.%N.%J.%u.err # STDERR

source "/etc/profile.d/zz_hpcnow-arch.sh"
module load "Python/3.8.6-GCCcore-10.2.0"
module load "CUDA/11.4.3"
source /homedtcl/atangarife/conflictoarmado/venv/bin/activate
python train.py
