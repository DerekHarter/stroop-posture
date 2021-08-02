# Body Posture Effects on Cognitive Control Experiments

Replication and extension of experiments examining the effects of
cognitive performance on cognitive control using Stroop and other
tasks while varying body posture.  Original Stroop body posture
experiments that are part of this replication efforts are from:

- [Smith, K. C., Davoli, C. C., Knapp, W. H., & Abrams, R. A. (2019). Standing enhances cognitive control and alters visual search. Attention, Perception, & Psychophysics, 81(7), 2320-2329.](https://link.springer.com/article/10.3758/s13414-019-01723-6)


# Getting Started

Experiments and data analysis workflows originally developed
Summer 2021 using a baseline 
[Ubuntu 20.04 LTS Focal Fossa Desktop](https://releases.ubuntu.com/20.04/)
distribution.  The `bootstrap` subdirectory contains
scripts of all additional packages and libraries installed into
the base Ubuntu 20.04 install.  The experiments performed
in this project make use of the 
[Psychtoolbox-3](http://psychtoolbox.org)
and the
[PsychoPy 3](https://www.psychopy.org/)
python library bindings of the psycho toolbox.  We used
the [NeuroDebian](http://neuro.debian.net/pkgs/octave-psychtoolbox-3.html)
distribution to setup Psychtoolbox and additional tools.

On a clean Ubuntu 20.04 desktop installation, the bootstrap
script can be run to install the tools and libraries used
in this project:

```
$ cd bootstrap
$ ./bootstrap-ubuntu-20.04.sh
```

Any Linux distribution will probably work fine for this project,
as long as the tools or equivalents shown in the bootstrap
script are installed and available.

# Running Experiments

The project bootstrap installs the Psychtoolbox and the PsychoPy
python AIP of the toolbox.  Experiments for subject can be
run in the `exp` subdirectory.  To run the `stroop-replication`
experiment, do the following

```
$ cd exp
$ /usr/bin/python3 stroop-replication.py
```

# Reproducing Project Workflow

All project products and data analysis workflow may be reproduced
from this project.  The project workflow performs all steps from
the collected raw subject experiment data files to final paper
and manuscript products.  The general workflow is to

1. Perform data cleaning and data tidying of collected raw
   subject data files for more detailed analysis.
2. Generate table products summarizing results and for use in
   project papers and documents.
3. Generate figure / visualization products to visualize
   important results and analysis.
4. Create papers and documents that incorparate figures and
   tables, and also using literate programming tools to allow
   directly for code snippts and execution in final documents.
   
The complete project workflow may be reproduced using the following
commands from the top level project directory

```
$ make clean
$ make
```

This will change into each subdirectory and perform a recursive make
to generate the products of the project workflow in the order given
above.  You may generate and individual product products by changing
into the directory and building it.  For example, to recreate all
data cleaning and data tidying steps, make the data directory

```
$ cd data
$ make
```

# Reproducible Research and Open Science

This project follows princiiples of reproducible research and
open science. A few good general resources to learn more about
the principles and best practices of open reproducable research:

- [What are the principles of reproducable research?](https://ropensci.github.io/reproducibility-guide/sections/introduction/)
- [Erik Gundersen, O. (2021). The fundamental principles of reproducibility. Philosophical Transactions of the Royal Society A, 379(2197), 20200210.](https://royalsocietypublishing.org/doi/10.1098/rsta.2020.0210)
- [Alston, J. M., & Rick, J. A. (2021). A Beginner’s Guide to Conducting Reproducible Research. Bulletin of the Ecological Society of America, 102(2), 1-14.](https://esajournals.onlinelibrary.wiley.com/doi/full/10.1002/bes2.1801)
- [What is open science?](https://www.fosteropenscience.eu/content/what-open-science-introduction)

![The six core principles of Open Science which guide the Open Traits Network.](https://www.researchgate.net/profile/Caterina-Penone/publication/332352194/figure/fig1/AS:747912753586180@1555327704672/The-six-core-principles-of-Open-Science-which-guide-the-Open-Traits-Network.png)

This project repository strives to support reprodcible research
and open science in many of the ways outlined in the above resources.

- The project code is open source, all code used for data analysis
  and collecting data is stored and viewable in this open repository.
- This project data is open data /  open access.  All raw data is collected in this
  project so that reanalysis and replication from collected data may be
  performed by any researcher.
- Documentation of software tools, versions and environments is part of this
  repository so that anyone may recreate the environemnt and (re)run all of the
  experiments, tools and data analysis collected in this project.
- This project repository strives for a reproducible workflow.  No data analysis
  products or tools are performed by hand.  All parts of the workflow of this
  project, from the raw data to final papers, can be fully reproduced by
  running the project workflow contained in this repository.
