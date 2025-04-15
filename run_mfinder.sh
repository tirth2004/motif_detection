#!/bin/bash
#SBATCH --job-name=mfinder
#SBATCH --output=mfinder_%j.out
#SBATCH --error=mfinder_%j.err
#SBATCH --time=02:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1

# Run mfinder with the correct command format
./mfinder lfr_directed_2_cleaned.txt -s 3 -r 1000 -f lfr_directed_2_OUT.txt
