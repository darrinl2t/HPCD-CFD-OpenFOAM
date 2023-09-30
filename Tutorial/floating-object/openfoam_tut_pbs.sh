#!/bin/bash

#PBS -l ncpus=4
#PBS -l mem=10GB
#PBS -l jobfs=10GB
#PBS -l walltime=1:00:00
#PBS -l software=OpenFOAM
#PBS -l wd

# Load module, always specify version number.
module load OpenFOAM/2112

./Allrun p

