# This bootstrap assumes a clean install of
# 20.04 LTS Ubuntu Focal Fossa w/ Gnome Desktop
# as a starting point

# make sure all packages up to date before starting
apt -y update
apt -y upgrade
apt -y autoremove

# configure some machine settings for convenience
# modify for yur correct timezone if desired
timedatectl set-timezone America/Chicago
hostnamectl set-hostname stroop

# need some basic dev tools available and editor
# remove emacs or vim if you don't use
apt -y install emacs vim build-essential git curl wget

# some personal aliases and settings, let dash user administor
# with passwordless sudo
cat > /etc/sudoers.d/dash <<EOF
dash ALL=(ALL) NOPASSWD: ALL
EOF

cat >> /root/.bashrc <<EOF
alias d='ls -Alh'
export EDITOR=vi
EOF

cat >> /home/dash/.bashrc <<EOF
alias d='ls -Alh'
export EDITOR=vi
EOF

# Configure NeuroDebian package repository to install psych toolbox and other
# tools for experiments
wget -O- http://neuro.debian.net/lists/focal.us-tn.full | sudo tee /etc/apt/sources.list.d/neurodebian.sources.list
sudo apt-key adv --recv-keys --keyserver hkps://keyserver.ubuntu.com 0xA5D32F012649A5A9
apt -y update

# install octave psychtoolbox v3
apt -y install octave-psychtoolbox-3

# install freenect from NeuroDebian for kinect library access, and
# other libfreenect development api and demos
apt -y install freenect libfreenect-dev libfreenect-demos

# add user(s) that need to access kinect video to video group
adduser dash video 

# blacklist standard Linux kinect driver so doesn't interfer
# with psychtoolbox access and use
# can run octave InstallKinect as well.
cp /usr/share/psychtoolbox-3/PsychContributed/linux_blacklist_kinectvideo /etc/modprobe.d/


# OpenNi library for skeleton tracking, some of it written in java so install
# jdk java development kit
#apt -y install g++ python libusb-1.0-0-dev freeglut3-dev doxygen graphviz
#apt -y install default-jre default-jdk
#cd /root
#git clone https://github.com/OpenNI/OpenNI.git
#cd OpenNI/Platform/Linux/CreateRedist
#./RedistMaker
#cd ../Redist
#./install.sh


# Install Anaconda Python for better package management of scientific
# python toolstack.  Install for all users so can set up additional
# log in accounts for experimenters to run experiments
cd /root
wget -c https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh
bash Anaconda3-2021.05-Linux-x86_64.sh -b -p /opt/anaconda3

# add any user accounts that need to run the anaconda python distribution
# to anaconda group
groupadd anaconda
chgrp -R anaconda /opt/anaconda3
chmod 770 -R /opt/anaconda3
usermod -a -G anaconda dash

# set up user environments to run anaconda python by default
cat >> /root/.bashrc <<"EOF"

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/opt/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/opt/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/opt/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/opt/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

EOF

cat >> /home/dash/.bashrc <<"EOF"

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/opt/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/opt/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/opt/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/opt/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

EOF


# install PsychoPy 3 api wrapper to Psychtoolbox
# if done after successful anaconda install before, pip should come
# from anaconda, and the pip install should be installing in anaconda
# python distriubtion
pip install psychopy
wget -c https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-20.04/wxPython-4.1.1-cp38-cp38-linux_x86_64.whl
pip install wxPython-4.1.1-cp38-cp38-linux_x86_64.whl
apt install libwebkit2gtk-4.0-37 libwebkit2gtk-4.0-dev


# second attempt, based on this note:
# https://discourse.psychopy.org/t/unable-to-properly-install-psychopy-on-ubuntu-20-04/12760/8
# so currently we have anaconda installed, but PsychoPy runs from
# the standard ubuntu python 3 install location instead.
# Not sure if need or worth fixing so that PsychoPy runs from
# anaconda python installation
apt -y install psychopy
apt -y install python3-pip python3-wxgtk-webview4.0
pip3 install -U psychopy
pip3 install cffi==1.14.0 psychtoolbox==3.0.16
pip3 install pyqt5
pip3 install SpeechRecognition

groupadd --force psychtoolbox
usermod -a -G psychtoolbox dash

cat > /etc/security/limits.d/99-psychopylimits.conf <<EOF
@psychtoolbox   -  nice       -20
@psychtoolbox   -  rtprio     50
@psychtoolbox   -  memlock    unlimited

EOF


# install packages in anaconda needed for data cleaning
# and analysis, and for pweave markdown document
# generation
apt install -y texlive-base texlive-fonts-recommended texlive-fonts-extra texlive-bibtex-extra texlive-latex-base texlive-latex-extra texlive-latex-recommended texlive-science biber
conda install -c conda-forge pweave pandoc pygments pandas seaborn
chgrp -R anaconda /opt/anaconda3
chmod 770 -R /opt/anaconda3

