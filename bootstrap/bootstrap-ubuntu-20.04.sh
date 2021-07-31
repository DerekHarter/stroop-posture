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

# some personal aliases and settings
cat > /etc/sudoers.d/dash <<EOF
dash ALL=(ALL) NOPASSWD: ALL
EOF

cat >> /root/.bashrc <<EOF
alias d='ls -Alh'
EOF

cat >> /home/dash/.bashrc <<EOF
alias d='ls -Alh'
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
apt -y install g++ python libusb-1.0-0-dev freeglut3-dev doxygen graphviz
apt -y install default-jre default-jdk

cd /root
git clone https://github.com/OpenNI/OpenNI.git
cd OpenNI/Platform/Linux/CreateRedist
./RedistMaker
cd ../Redist
./install.sh
