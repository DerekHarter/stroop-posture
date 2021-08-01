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

# Reproducible Research
