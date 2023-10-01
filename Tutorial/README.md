# README #

## Introduction
OpenFOAM is the free, open source CFD software developed primarily by OpenCFD Ltd since 2004. It has a large user base across most areas of engineering and science, from both commercial and academic organisations. OpenFOAM has an extensive range of features to solve anything from complex fluid flows involving chemical reactions, turbulence and heat transfer, to acoustics, solid mechanics and electromagnetics. The code available at [here](https://https://www.openfoam.com/).

For this training, this repository provides an OpenFOAM tutorial case for OpenFOAM-v2112 and tutorial slides.

***

## SSH
Downloading should be directed to Gadi system.

Make sure you can ssh to Gadi shell.
- **Linux/Mac Users**: Use the following terminal command:
  ```bash
  ssh username@gadi.nci.org.au
  ```
- **Windows Users**, You can use SSH clients like PuTTY or MobaXterm, or access the Gadi Terminal from NCI Web-based platform [ARE](https://are.nci.org.au).

***

## Downloading the Code
Once you land on the Gadi log-in node

```bash
# Create and navigate to a directory under /scratch/nf47
$ mkdir -p /scratch/nf47/$USER/ && cd "$_"

# Clone the repository
$ git clone https://github.com/darrinl2t/HPCD-CFD-OpenFOAM.git
```

***

## Task 1: Run Simulation
 In this tutorial, you are asked to submit an OpenFOAM simulation.

 The OpenFOAM simulation setup is provided to you in dirctory **Tutorial/floating-object** together with the job submission script.


```bash
#To submit the job, navigate to dirctory build_CascadeLake
$qsub job_openfoam_tut_pbs.sh

#Once the job ID returns, you query the job by
$qstat -snw
```


## Task 2: Plot the data output
Upon job completion, the simulation data will be stored in the simulation case folder.

Using NCI's web-based graphical interface ARE (short for Australian Research Environment), you can visualize the data in-situ. Head to [ARE](https://are.nci.org.au) and select VDI Desktop.

Specify the session characteristics as follows:
```
Walltime: 1

Queue: normalbw

Compute Size: Small

Project: nf47

Storage: gdata/nf47+scratch/nf47


```

 Hit Launch and wait until the job starts.

