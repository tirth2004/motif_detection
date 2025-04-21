#!/bin/bash
#SBATCH --job-name=mfinder
#SBATCH --output=mfinder_%j.out
#SBATCH --error=mfinder_%j.err
#SBATCH --time=06:00:00        # Increased to 6 hours
#SBATCH --nodes=1
#SBATCH --ntasks=1             # Single task
#SBATCH --cpus-per-task=32     # Use 32 CPUs within the task
#SBATCH --mem=16G
#SBATCH --partition=standard
#SBATCH --exclusive
#SBATCH --hint=nomultithread
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=your.email@example.com

# Load necessary modules
module load gcc/9.3.0

# Set OpenMP environment variables for better parallel performance
export OMP_NUM_THREADS=32      # Use all 32 cores
export OMP_PLACES=cores
export OMP_PROC_BIND=close

# Run mfinder with optimized parameters
./mfinder lfr_directed_iter2_5_cleaned.txt -s 3 -r 1000 -f lfr_directed_iter2_5
_OUT.txt -met -t0 0.001 -iter 4 -eth 0.005 -nsr 200
