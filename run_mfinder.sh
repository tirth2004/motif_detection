#!/bin/bash
#SBATCH --job-name=mfinder
#SBATCH --output=mfinder_%j.out
#SBATCH --error=mfinder_%j.err
#SBATCH --time=02:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32    # Use 32 CPU cores
#SBATCH --mem=128G            # Request 128GB of RAM
#SBATCH --partition=standard  # Use the standard partition

# Load any necessary modules
module load gcc/9.3.0

# Run mfinder with optimized parameters
./mfinder lfr_directed_3_cleaned.txt -s 3 -r 1000 -f lfr_directed_3_OUT.txt -met -t0 0.001 -iter 4 -eth 0.005
