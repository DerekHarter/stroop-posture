#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.0),
    on Thu 26 Aug 2021 09:12:40 AM CDT
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.0'
expName = 'stroop'  # from the Builder filename that created this script
expInfo = {'participant': '1000', 'session': '01'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + '../data' + os.sep + '%s_%s' % (expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/home/dash/repos/stroop-posture/exp/stroop-replication.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.WARNING)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "initializeExperiment"
initializeExperimentClock = core.Clock()
# create conditions based on participant number
participantId = int(expInfo['participant'])

# 4 condition ranges
if participantId >= 1000 and participantId <= 1999:
    # condition 1 start standing use red-green l/r keymap
    posture = 'standing'
    correctKeyRed = 'left'
    correctKeyGreen = 'right'
elif participantId >= 2000 and participantId <= 2999:
    # condition 2 start standing use green-red l/r keymap
    posture = 'standing'
    correctKeyRed = 'right'
    correctKeyGreen = 'left'
elif participantId >= 3000 and participantId <= 3999:
    # condition 3 start sitting use red-green l/r keymap
    posture = 'sitting'
    correctKeyRed = 'left'
    correctKeyGreen = 'right'
elif participantId >= 4000 and participantId <= 4999:
    # condition 4 start sitting use green-red l/r keymap
    posture = 'sitting'
    correctKeyRed = 'right'
    correctKeyGreen = 'left'
else:
    # croak immediately if experimenter gives invalid
    # participant id, maybe make this for testing?
    print("Invalid participant id entered: ", participantId)
    print("Use range 1000-4999 for participant")
    sys.exit(0)

# put correct keys in experiment info so saved in
# trial output
expInfo['posture'] = posture
expInfo['correctKeyRed'] = correctKeyRed
expInfo['correctKeyGreen'] = correctKeyGreen

# Initialize components for Routine "setupPosture"
setupPostureClock = core.Clock()
setupPostureInstructions = """
Before beginning, the experiment
supervisor will position you in the
correct initial posture.

Posture: %s

Once you are ready, press any key
to begin practicing the  experiment.
""" % (posture.upper())
setupPostureText = visual.TextStim(win=win, name='setupPostureText',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
setupPostureReady = keyboard.Keyboard()
setupPostureAlert = sound.Sound('F', secs=-1, stereo=True, hamming=True,
    name='setupPostureAlert')
setupPostureAlert.setVolume(1000.0)

# Initialize components for Routine "instructPractice"
instructPracticeClock = core.Clock()
practiceLoopIteration = 1
instructPracticeText = visual.TextStim(win=win, name='instructPracticeText',
    text='',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=10, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instructPracticeReady = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
word = visual.TextStim(win=win, name='word',
    text='',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
resp = keyboard.Keyboard()

# Initialize components for Routine "practiceFeedback"
practiceFeedbackClock = core.Clock()
#msg variable just needs some value at start
msg=''
sound_hz=60
feedbackPracticeMessage = visual.TextStim(win=win, name='feedbackPracticeMessage',
    text='',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color=[1,1,1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
feedbackPracticeSound = sound.Sound(sound_hz, secs=0.5, stereo=True, hamming=True,
    name='feedbackPracticeSound')
feedbackPracticeSound.setVolume(1.0)

# Initialize components for Routine "instructTrial"
instructTrialClock = core.Clock()
trialLoopIteration = 1
instructTrialText = visual.TextStim(win=win, name='instructTrialText',
    text='',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=10, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instructTrialReady = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
word = visual.TextStim(win=win, name='word',
    text='',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
resp = keyboard.Keyboard()

# Initialize components for Routine "trialFeedback"
trialFeedbackClock = core.Clock()
#msg variable just needs some value at start
msg=''
sound_hz=60
feedback_3 = visual.TextStim(win=win, name='feedback_3',
    text=msg,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
sound_2 = sound.Sound(sound_hz, secs=0.5, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)

# Initialize components for Routine "initializeExperiment2"
initializeExperiment2Clock = core.Clock()

# Initialize components for Routine "setupPosture2"
setupPosture2Clock = core.Clock()
setupPosture2Text = visual.TextStim(win=win, name='setupPosture2Text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
setupPosture2Ready = keyboard.Keyboard()
setupPosture2Sound = sound.Sound('F', secs=-1, stereo=True, hamming=True,
    name='setupPosture2Sound')
setupPosture2Sound.setVolume(1.0)

# Initialize components for Routine "instructPractice"
instructPracticeClock = core.Clock()
practiceLoopIteration = 1
instructPracticeText = visual.TextStim(win=win, name='instructPracticeText',
    text='',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=10, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instructPracticeReady = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
word = visual.TextStim(win=win, name='word',
    text='',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
resp = keyboard.Keyboard()

# Initialize components for Routine "practiceFeedback"
practiceFeedbackClock = core.Clock()
#msg variable just needs some value at start
msg=''
sound_hz=60
feedbackPracticeMessage = visual.TextStim(win=win, name='feedbackPracticeMessage',
    text='',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color=[1,1,1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
feedbackPracticeSound = sound.Sound(sound_hz, secs=0.5, stereo=True, hamming=True,
    name='feedbackPracticeSound')
feedbackPracticeSound.setVolume(1.0)

# Initialize components for Routine "instructTrial"
instructTrialClock = core.Clock()
trialLoopIteration = 1
instructTrialText = visual.TextStim(win=win, name='instructTrialText',
    text='',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=10, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instructTrialReady = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
word = visual.TextStim(win=win, name='word',
    text='',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
resp = keyboard.Keyboard()

# Initialize components for Routine "trialFeedback"
trialFeedbackClock = core.Clock()
#msg variable just needs some value at start
msg=''
sound_hz=60
feedback_3 = visual.TextStim(win=win, name='feedback_3',
    text=msg,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
sound_2 = sound.Sound(sound_hz, secs=0.5, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thanksText = visual.TextStim(win=win, name='thanksText',
    text='This is the end of the experiment.\n\nThanks!',
    font='arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "initializeExperiment"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
initializeExperimentComponents = []
for thisComponent in initializeExperimentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
initializeExperimentClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "initializeExperiment"-------
while continueRoutine:
    # get current time
    t = initializeExperimentClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=initializeExperimentClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in initializeExperimentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "initializeExperiment"-------
for thisComponent in initializeExperimentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "initializeExperiment" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "setupPosture"-------
continueRoutine = True
# update component parameters for each repeat
setupPostureText.setText(setupPostureInstructions)
setupPostureReady.keys = []
setupPostureReady.rt = []
_setupPostureReady_allKeys = []
setupPostureAlert.setSound('F', secs=5, hamming=True)
setupPostureAlert.setVolume(1000.0, log=False)
# keep track of which components have finished
setupPostureComponents = [setupPostureText, setupPostureReady, setupPostureAlert]
for thisComponent in setupPostureComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
setupPostureClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setupPosture"-------
while continueRoutine:
    # get current time
    t = setupPostureClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setupPostureClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *setupPostureText* updates
    if setupPostureText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        setupPostureText.frameNStart = frameN  # exact frame index
        setupPostureText.tStart = t  # local t and not account for scr refresh
        setupPostureText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(setupPostureText, 'tStartRefresh')  # time at next scr refresh
        setupPostureText.setAutoDraw(True)
    
    # *setupPostureReady* updates
    waitOnFlip = False
    if setupPostureReady.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        setupPostureReady.frameNStart = frameN  # exact frame index
        setupPostureReady.tStart = t  # local t and not account for scr refresh
        setupPostureReady.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(setupPostureReady, 'tStartRefresh')  # time at next scr refresh
        setupPostureReady.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(setupPostureReady.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(setupPostureReady.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if setupPostureReady.status == STARTED and not waitOnFlip:
        theseKeys = setupPostureReady.getKeys(keyList=None, waitRelease=False)
        _setupPostureReady_allKeys.extend(theseKeys)
        if len(_setupPostureReady_allKeys):
            setupPostureReady.keys = _setupPostureReady_allKeys[-1].name  # just the last key pressed
            setupPostureReady.rt = _setupPostureReady_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # start/stop setupPostureAlert
    if setupPostureAlert.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        setupPostureAlert.frameNStart = frameN  # exact frame index
        setupPostureAlert.tStart = t  # local t and not account for scr refresh
        setupPostureAlert.tStartRefresh = tThisFlipGlobal  # on global time
        setupPostureAlert.play(when=win)  # sync with win flip
    if setupPostureAlert.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > setupPostureAlert.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            setupPostureAlert.tStop = t  # not accounting for scr refresh
            setupPostureAlert.frameNStop = frameN  # exact frame index
            win.timeOnFlip(setupPostureAlert, 'tStopRefresh')  # time at next scr refresh
            setupPostureAlert.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupPostureComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setupPosture"-------
for thisComponent in setupPostureComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('setupPostureText.started', setupPostureText.tStartRefresh)
thisExp.addData('setupPostureText.stopped', setupPostureText.tStopRefresh)
# check responses
if setupPostureReady.keys in ['', [], None]:  # No response was made
    setupPostureReady.keys = None
thisExp.addData('setupPostureReady.keys',setupPostureReady.keys)
if setupPostureReady.keys != None:  # we had a response
    thisExp.addData('setupPostureReady.rt', setupPostureReady.rt)
thisExp.addData('setupPostureReady.started', setupPostureReady.tStartRefresh)
thisExp.addData('setupPostureReady.stopped', setupPostureReady.tStopRefresh)
thisExp.nextEntry()
setupPostureAlert.stop()  # ensure sound has stopped at end of routine
thisExp.addData('setupPostureAlert.started', setupPostureAlert.tStartRefresh)
thisExp.addData('setupPostureAlert.stopped', setupPostureAlert.tStopRefresh)
# the Routine "setupPosture" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_loop = data.TrialHandler(nReps=2.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='practice_loop')
thisExp.addLoop(practice_loop)  # add the loop to the experiment
thisPractice_loop = practice_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
if thisPractice_loop != None:
    for paramName in thisPractice_loop:
        exec('{} = thisPractice_loop[paramName]'.format(paramName))

for thisPractice_loop in practice_loop:
    currentLoop = practice_loop
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
    if thisPractice_loop != None:
        for paramName in thisPractice_loop:
            exec('{} = thisPractice_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instructPractice"-------
    continueRoutine = True
    # update component parameters for each repeat
    if correctKeyRed == 'left':
        practiceInstructions="""
    In the %s posture
    
    Please press;
    %s for red  LETTERS     %s for green  LETTERS
    
    Please respond as quickly and accuractly as possible to the color
    (red or green) in which the  letter-string appeared.  Ignore all other
    aspects of the letter-string, including its meaning.
    
    Let's start with a few practice trials
    This is block %d out of 2 practice blocks
    
    Press any key to start
    """ % (posture, correctKeyRed, correctKeyGreen, practiceLoopIteration)
    else:
        practiceInstructions="""
    In the %s posture
    
    Please press;
    %s for green LETTERS    %s for red LETTERS
    
    Please respond as quickly and accuractly as possible to the color
    (red or green) in which the  letter-string appeared.  Ignore all other
    aspects of the letter-string, including its meaning.
    
    Let's start with a few practice trials
    This is block %d out of 2 practice blocks
    
    Press any key to start
    """ % (posture, correctKeyGreen, correctKeyRed, practiceLoopIteration)
        
    instructPracticeText.setText(practiceInstructions)
    instructPracticeReady.keys = []
    instructPracticeReady.rt = []
    _instructPracticeReady_allKeys = []
    # keep track of which components have finished
    instructPracticeComponents = [instructPracticeText, instructPracticeReady]
    for thisComponent in instructPracticeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructPracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructPractice"-------
    while continueRoutine:
        # get current time
        t = instructPracticeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructPracticeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructPracticeText* updates
        if instructPracticeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructPracticeText.frameNStart = frameN  # exact frame index
            instructPracticeText.tStart = t  # local t and not account for scr refresh
            instructPracticeText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructPracticeText, 'tStartRefresh')  # time at next scr refresh
            instructPracticeText.setAutoDraw(True)
        
        # *instructPracticeReady* updates
        waitOnFlip = False
        if instructPracticeReady.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructPracticeReady.frameNStart = frameN  # exact frame index
            instructPracticeReady.tStart = t  # local t and not account for scr refresh
            instructPracticeReady.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructPracticeReady, 'tStartRefresh')  # time at next scr refresh
            instructPracticeReady.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instructPracticeReady.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instructPracticeReady.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instructPracticeReady.status == STARTED and not waitOnFlip:
            theseKeys = instructPracticeReady.getKeys(keyList=None, waitRelease=False)
            _instructPracticeReady_allKeys.extend(theseKeys)
            if len(_instructPracticeReady_allKeys):
                instructPracticeReady.keys = _instructPracticeReady_allKeys[-1].name  # just the last key pressed
                instructPracticeReady.rt = _instructPracticeReady_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructPracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructPractice"-------
    for thisComponent in instructPracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practiceLoopIteration += 1
    practice_loop.addData('instructPracticeText.started', instructPracticeText.tStartRefresh)
    practice_loop.addData('instructPracticeText.stopped', instructPracticeText.tStopRefresh)
    # the Routine "instructPractice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practice = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('stroop-replication-trialtypes.xlsx'),
        seed=None, name='practice')
    thisExp.addLoop(practice)  # add the loop to the experiment
    thisPractice = practice.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice:
            exec('{} = thisPractice[paramName]'.format(paramName))
    
    for thisPractice in practice:
        currentLoop = practice
        # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
        if thisPractice != None:
            for paramName in thisPractice:
                exec('{} = thisPractice[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        if letterColor == 'red':
            expInfo['correctAnswer'] = correctKeyRed
            correctAnswer = correctKeyRed
        elif letterColor == 'green':
            expInfo['correctAnswer'] = correctKeyGreen
            correctAnswer = correctKeyGreen
        else:
            print("Error, unexpected letterColor:", letterColor)
            sys.exit(0)
        word.setColor(letterColor, colorSpace='rgb')
        word.setText(text)
        resp.keys = []
        resp.rt = []
        _resp_allKeys = []
        # keep track of which components have finished
        trialComponents = [fixation, word, resp]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation* updates
            if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                fixation.setAutoDraw(True)
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                    fixation.setAutoDraw(False)
            
            # *word* updates
            if word.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                word.frameNStart = frameN  # exact frame index
                word.tStart = t  # local t and not account for scr refresh
                word.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(word, 'tStartRefresh')  # time at next scr refresh
                word.setAutoDraw(True)
            if word.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > word.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    word.tStop = t  # not accounting for scr refresh
                    word.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(word, 'tStopRefresh')  # time at next scr refresh
                    word.setAutoDraw(False)
            
            # *resp* updates
            waitOnFlip = False
            if resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                resp.frameNStart = frameN  # exact frame index
                resp.tStart = t  # local t and not account for scr refresh
                resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
                resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > resp.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    resp.tStop = t  # not accounting for scr refresh
                    resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(resp, 'tStopRefresh')  # time at next scr refresh
                    resp.status = FINISHED
            if resp.status == STARTED and not waitOnFlip:
                theseKeys = resp.getKeys(keyList=['left', 'right'], waitRelease=False)
                _resp_allKeys.extend(theseKeys)
                if len(_resp_allKeys):
                    resp.keys = _resp_allKeys[-1].name  # just the last key pressed
                    resp.rt = _resp_allKeys[-1].rt
                    # was this correct?
                    if (resp.keys == str(correctAnswer)) or (resp.keys == correctAnswer):
                        resp.corr = 1
                    else:
                        resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        practice.addData('fixation.started', fixation.tStartRefresh)
        practice.addData('fixation.stopped', fixation.tStopRefresh)
        practice.addData('word.started', word.tStartRefresh)
        practice.addData('word.stopped', word.tStopRefresh)
        # check responses
        if resp.keys in ['', [], None]:  # No response was made
            resp.keys = None
            # was no response the correct answer?!
            if str(correctAnswer).lower() == 'none':
               resp.corr = 1;  # correct non-response
            else:
               resp.corr = 0;  # failed to respond (incorrectly)
        # store data for practice (TrialHandler)
        practice.addData('resp.keys',resp.keys)
        practice.addData('resp.corr', resp.corr)
        if resp.keys != None:  # we had a response
            practice.addData('resp.rt', resp.rt)
        practice.addData('resp.started', resp.tStartRefresh)
        practice.addData('resp.stopped', resp.tStopRefresh)
        
        # ------Prepare to start Routine "practiceFeedback"-------
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        if resp.corr:#stored on last run routine
          msg="Correct! RT=%.3f" %(resp.rt)
          sound_hz=60
        else:
          msg="Oops! That was wrong.\nPlease respond as fast and accuractly as you can."
          sound_hz=440
        feedbackPracticeMessage.setText(msg)
        feedbackPracticeSound.setSound(sound_hz, secs=0.5, hamming=True)
        feedbackPracticeSound.setVolume(1.0, log=False)
        # keep track of which components have finished
        practiceFeedbackComponents = [feedbackPracticeMessage, feedbackPracticeSound]
        for thisComponent in practiceFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        practiceFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "practiceFeedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = practiceFeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=practiceFeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedbackPracticeMessage* updates
            if feedbackPracticeMessage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedbackPracticeMessage.frameNStart = frameN  # exact frame index
                feedbackPracticeMessage.tStart = t  # local t and not account for scr refresh
                feedbackPracticeMessage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedbackPracticeMessage, 'tStartRefresh')  # time at next scr refresh
                feedbackPracticeMessage.setAutoDraw(True)
            if feedbackPracticeMessage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedbackPracticeMessage.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    feedbackPracticeMessage.tStop = t  # not accounting for scr refresh
                    feedbackPracticeMessage.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedbackPracticeMessage, 'tStopRefresh')  # time at next scr refresh
                    feedbackPracticeMessage.setAutoDraw(False)
            # start/stop feedbackPracticeSound
            if feedbackPracticeSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedbackPracticeSound.frameNStart = frameN  # exact frame index
                feedbackPracticeSound.tStart = t  # local t and not account for scr refresh
                feedbackPracticeSound.tStartRefresh = tThisFlipGlobal  # on global time
                feedbackPracticeSound.play(when=win)  # sync with win flip
            if feedbackPracticeSound.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedbackPracticeSound.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    feedbackPracticeSound.tStop = t  # not accounting for scr refresh
                    feedbackPracticeSound.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedbackPracticeSound, 'tStopRefresh')  # time at next scr refresh
                    feedbackPracticeSound.stop()
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practiceFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "practiceFeedback"-------
        for thisComponent in practiceFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        practice.addData('feedbackPracticeMessage.started', feedbackPracticeMessage.tStartRefresh)
        practice.addData('feedbackPracticeMessage.stopped', feedbackPracticeMessage.tStopRefresh)
        feedbackPracticeSound.stop()  # ensure sound has stopped at end of routine
        practice.addData('feedbackPracticeSound.started', feedbackPracticeSound.tStartRefresh)
        practice.addData('feedbackPracticeSound.stopped', feedbackPracticeSound.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'practice'
    
    # get names of stimulus parameters
    if practice.trialList in ([], [None], None):
        params = []
    else:
        params = practice.trialList[0].keys()
    # save data for this loop
    practice.saveAsExcel(filename + '.xlsx', sheetName='practice',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'practice_loop'

# get names of stimulus parameters
if practice_loop.trialList in ([], [None], None):
    params = []
else:
    params = practice_loop.trialList[0].keys()
# save data for this loop
practice_loop.saveAsExcel(filename + '.xlsx', sheetName='practice_loop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
trial_loop = data.TrialHandler(nReps=4.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trial_loop')
thisExp.addLoop(trial_loop)  # add the loop to the experiment
thisTrial_loop = trial_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_loop.rgb)
if thisTrial_loop != None:
    for paramName in thisTrial_loop:
        exec('{} = thisTrial_loop[paramName]'.format(paramName))

for thisTrial_loop in trial_loop:
    currentLoop = trial_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_loop.rgb)
    if thisTrial_loop != None:
        for paramName in thisTrial_loop:
            exec('{} = thisTrial_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instructTrial"-------
    continueRoutine = True
    # update component parameters for each repeat
    if correctKeyRed == 'left':
        trialInstructions="""
    Take a small break and then CHECK  your posture before continuing
    
    You should still be in the %s posture
    
    OK. Ready for the real thing?
    
    Remember, ignore the word itself; press:
    %s for red LETTERS   %s for green LETTERS
    
    Please respond as quickly and accuractly as possible to the color
    (red or green) in which the  letter-string appeared.  Ignore all other
    aspects of the letter-string, including its meaning.
    
    This is block %d out of 4 experiment blocks
    
    Press any key to start
    """ % (posture, correctKeyRed, correctKeyGreen, trialLoopIteration)
    else:
        trialInstructions="""
    Take a small break and then CHECK  your posture before continuing
    
    You should still be in the %s posture
    
    OK. Ready for the real thing?
    
    Remember, ignore the word itself; press:
    %s for green LETTERS   %s for red LETTERS
    
    Please respond as quickly and accuractly as possible to the color
    (red or green) in which the  letter-string appeared.  Ignore all other
    aspects of the letter-string, including its meaning.
    
    This is block %d out of 4 experiment blocks
    
    Press any key to start
    """ % (posture, correctKeyGreen, correctKeyRed, trialLoopIteration)
    
    
    instructTrialText.setText(trialInstructions)
    instructTrialReady.keys = []
    instructTrialReady.rt = []
    _instructTrialReady_allKeys = []
    # keep track of which components have finished
    instructTrialComponents = [instructTrialText, instructTrialReady]
    for thisComponent in instructTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructTrial"-------
    while continueRoutine:
        # get current time
        t = instructTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructTrialText* updates
        if instructTrialText.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            instructTrialText.frameNStart = frameN  # exact frame index
            instructTrialText.tStart = t  # local t and not account for scr refresh
            instructTrialText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructTrialText, 'tStartRefresh')  # time at next scr refresh
            instructTrialText.setAutoDraw(True)
        
        # *instructTrialReady* updates
        waitOnFlip = False
        if instructTrialReady.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            instructTrialReady.frameNStart = frameN  # exact frame index
            instructTrialReady.tStart = t  # local t and not account for scr refresh
            instructTrialReady.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructTrialReady, 'tStartRefresh')  # time at next scr refresh
            instructTrialReady.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instructTrialReady.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instructTrialReady.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instructTrialReady.status == STARTED and not waitOnFlip:
            theseKeys = instructTrialReady.getKeys(keyList=None, waitRelease=False)
            _instructTrialReady_allKeys.extend(theseKeys)
            if len(_instructTrialReady_allKeys):
                instructTrialReady.keys = _instructTrialReady_allKeys[-1].name  # just the last key pressed
                instructTrialReady.rt = _instructTrialReady_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructTrial"-------
    for thisComponent in instructTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialLoopIteration += 1
    trial_loop.addData('instructTrialText.started', instructTrialText.tStartRefresh)
    trial_loop.addData('instructTrialText.stopped', instructTrialText.tStopRefresh)
    # the Routine "instructTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('stroop-replication-trialtypes.xlsx'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        if letterColor == 'red':
            expInfo['correctAnswer'] = correctKeyRed
            correctAnswer = correctKeyRed
        elif letterColor == 'green':
            expInfo['correctAnswer'] = correctKeyGreen
            correctAnswer = correctKeyGreen
        else:
            print("Error, unexpected letterColor:", letterColor)
            sys.exit(0)
        word.setColor(letterColor, colorSpace='rgb')
        word.setText(text)
        resp.keys = []
        resp.rt = []
        _resp_allKeys = []
        # keep track of which components have finished
        trialComponents = [fixation, word, resp]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation* updates
            if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                fixation.setAutoDraw(True)
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                    fixation.setAutoDraw(False)
            
            # *word* updates
            if word.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                word.frameNStart = frameN  # exact frame index
                word.tStart = t  # local t and not account for scr refresh
                word.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(word, 'tStartRefresh')  # time at next scr refresh
                word.setAutoDraw(True)
            if word.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > word.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    word.tStop = t  # not accounting for scr refresh
                    word.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(word, 'tStopRefresh')  # time at next scr refresh
                    word.setAutoDraw(False)
            
            # *resp* updates
            waitOnFlip = False
            if resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                resp.frameNStart = frameN  # exact frame index
                resp.tStart = t  # local t and not account for scr refresh
                resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
                resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > resp.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    resp.tStop = t  # not accounting for scr refresh
                    resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(resp, 'tStopRefresh')  # time at next scr refresh
                    resp.status = FINISHED
            if resp.status == STARTED and not waitOnFlip:
                theseKeys = resp.getKeys(keyList=['left', 'right'], waitRelease=False)
                _resp_allKeys.extend(theseKeys)
                if len(_resp_allKeys):
                    resp.keys = _resp_allKeys[-1].name  # just the last key pressed
                    resp.rt = _resp_allKeys[-1].rt
                    # was this correct?
                    if (resp.keys == str(correctAnswer)) or (resp.keys == correctAnswer):
                        resp.corr = 1
                    else:
                        resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('fixation.started', fixation.tStartRefresh)
        trials.addData('fixation.stopped', fixation.tStopRefresh)
        trials.addData('word.started', word.tStartRefresh)
        trials.addData('word.stopped', word.tStopRefresh)
        # check responses
        if resp.keys in ['', [], None]:  # No response was made
            resp.keys = None
            # was no response the correct answer?!
            if str(correctAnswer).lower() == 'none':
               resp.corr = 1;  # correct non-response
            else:
               resp.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('resp.keys',resp.keys)
        trials.addData('resp.corr', resp.corr)
        if resp.keys != None:  # we had a response
            trials.addData('resp.rt', resp.rt)
        trials.addData('resp.started', resp.tStartRefresh)
        trials.addData('resp.stopped', resp.tStopRefresh)
        
        # ------Prepare to start Routine "trialFeedback"-------
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        if resp.corr:#stored on last run routine
          msg="."
          sound_hz=60
        else:
          msg="."
          sound_hz=440
        sound_2.setSound(sound_hz, secs=0.5, hamming=True)
        sound_2.setVolume(1.0, log=False)
        # keep track of which components have finished
        trialFeedbackComponents = [feedback_3, sound_2]
        for thisComponent in trialFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trialFeedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialFeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialFeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_3* updates
            if feedback_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_3.frameNStart = frameN  # exact frame index
                feedback_3.tStart = t  # local t and not account for scr refresh
                feedback_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_3, 'tStartRefresh')  # time at next scr refresh
                feedback_3.setAutoDraw(True)
            if feedback_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_3.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_3.tStop = t  # not accounting for scr refresh
                    feedback_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedback_3, 'tStopRefresh')  # time at next scr refresh
                    feedback_3.setAutoDraw(False)
            # start/stop sound_2
            if sound_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sound_2.frameNStart = frameN  # exact frame index
                sound_2.tStart = t  # local t and not account for scr refresh
                sound_2.tStartRefresh = tThisFlipGlobal  # on global time
                sound_2.play(when=win)  # sync with win flip
            if sound_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_2.tStop = t  # not accounting for scr refresh
                    sound_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(sound_2, 'tStopRefresh')  # time at next scr refresh
                    sound_2.stop()
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trialFeedback"-------
        for thisComponent in trialFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('feedback_3.started', feedback_3.tStartRefresh)
        trials.addData('feedback_3.stopped', feedback_3.tStopRefresh)
        sound_2.stop()  # ensure sound has stopped at end of routine
        trials.addData('sound_2.started', sound_2.tStartRefresh)
        trials.addData('sound_2.stopped', sound_2.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    
    # get names of stimulus parameters
    if trials.trialList in ([], [None], None):
        params = []
    else:
        params = trials.trialList[0].keys()
    # save data for this loop
    trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'trial_loop'

# get names of stimulus parameters
if trial_loop.trialList in ([], [None], None):
    params = []
else:
    params = trial_loop.trialList[0].keys()
# save data for this loop
trial_loop.saveAsExcel(filename + '.xlsx', sheetName='trial_loop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "initializeExperiment2"-------
continueRoutine = True
# update component parameters for each repeat
if posture == 'sitting':
    posture = 'standing'
elif posture == 'standing':
    posture = 'sitting'
else:
    print("unknown posture: ", posture)
    sys.exit(0)
    
expInfo['posture'] = posture

practiceLoopIteration = 1
trialLoopIteration = 1
# keep track of which components have finished
initializeExperiment2Components = []
for thisComponent in initializeExperiment2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
initializeExperiment2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "initializeExperiment2"-------
while continueRoutine:
    # get current time
    t = initializeExperiment2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=initializeExperiment2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in initializeExperiment2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "initializeExperiment2"-------
for thisComponent in initializeExperiment2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "initializeExperiment2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "setupPosture2"-------
continueRoutine = True
# update component parameters for each repeat
setupPosture2Instructions = """
Before continuing, the experiment
supervisor will position you in the
next experiment posture:

Posture: %s

Once you are ready, press any key
to begin practicing the experiment.
""" % (posture.upper())
setupPosture2Text.setText(setupPosture2Instructions)
setupPosture2Ready.keys = []
setupPosture2Ready.rt = []
_setupPosture2Ready_allKeys = []
setupPosture2Sound.setSound('F', secs=5, hamming=True)
setupPosture2Sound.setVolume(1.0, log=False)
# keep track of which components have finished
setupPosture2Components = [setupPosture2Text, setupPosture2Ready, setupPosture2Sound]
for thisComponent in setupPosture2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
setupPosture2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setupPosture2"-------
while continueRoutine:
    # get current time
    t = setupPosture2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setupPosture2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *setupPosture2Text* updates
    if setupPosture2Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        setupPosture2Text.frameNStart = frameN  # exact frame index
        setupPosture2Text.tStart = t  # local t and not account for scr refresh
        setupPosture2Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(setupPosture2Text, 'tStartRefresh')  # time at next scr refresh
        setupPosture2Text.setAutoDraw(True)
    
    # *setupPosture2Ready* updates
    waitOnFlip = False
    if setupPosture2Ready.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        setupPosture2Ready.frameNStart = frameN  # exact frame index
        setupPosture2Ready.tStart = t  # local t and not account for scr refresh
        setupPosture2Ready.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(setupPosture2Ready, 'tStartRefresh')  # time at next scr refresh
        setupPosture2Ready.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(setupPosture2Ready.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(setupPosture2Ready.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if setupPosture2Ready.status == STARTED and not waitOnFlip:
        theseKeys = setupPosture2Ready.getKeys(keyList=None, waitRelease=False)
        _setupPosture2Ready_allKeys.extend(theseKeys)
        if len(_setupPosture2Ready_allKeys):
            setupPosture2Ready.keys = _setupPosture2Ready_allKeys[-1].name  # just the last key pressed
            setupPosture2Ready.rt = _setupPosture2Ready_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # start/stop setupPosture2Sound
    if setupPosture2Sound.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        setupPosture2Sound.frameNStart = frameN  # exact frame index
        setupPosture2Sound.tStart = t  # local t and not account for scr refresh
        setupPosture2Sound.tStartRefresh = tThisFlipGlobal  # on global time
        setupPosture2Sound.play(when=win)  # sync with win flip
    if setupPosture2Sound.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > setupPosture2Sound.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            setupPosture2Sound.tStop = t  # not accounting for scr refresh
            setupPosture2Sound.frameNStop = frameN  # exact frame index
            win.timeOnFlip(setupPosture2Sound, 'tStopRefresh')  # time at next scr refresh
            setupPosture2Sound.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupPosture2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setupPosture2"-------
for thisComponent in setupPosture2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('setupPosture2Text.started', setupPosture2Text.tStartRefresh)
thisExp.addData('setupPosture2Text.stopped', setupPosture2Text.tStopRefresh)
# check responses
if setupPosture2Ready.keys in ['', [], None]:  # No response was made
    setupPosture2Ready.keys = None
thisExp.addData('setupPosture2Ready.keys',setupPosture2Ready.keys)
if setupPosture2Ready.keys != None:  # we had a response
    thisExp.addData('setupPosture2Ready.rt', setupPosture2Ready.rt)
thisExp.addData('setupPosture2Ready.started', setupPosture2Ready.tStartRefresh)
thisExp.addData('setupPosture2Ready.stopped', setupPosture2Ready.tStopRefresh)
thisExp.nextEntry()
setupPosture2Sound.stop()  # ensure sound has stopped at end of routine
thisExp.addData('setupPosture2Sound.started', setupPosture2Sound.tStartRefresh)
thisExp.addData('setupPosture2Sound.stopped', setupPosture2Sound.tStopRefresh)
# the Routine "setupPosture2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_loop2 = data.TrialHandler(nReps=2.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='practice_loop2')
thisExp.addLoop(practice_loop2)  # add the loop to the experiment
thisPractice_loop2 = practice_loop2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_loop2.rgb)
if thisPractice_loop2 != None:
    for paramName in thisPractice_loop2:
        exec('{} = thisPractice_loop2[paramName]'.format(paramName))

for thisPractice_loop2 in practice_loop2:
    currentLoop = practice_loop2
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_loop2.rgb)
    if thisPractice_loop2 != None:
        for paramName in thisPractice_loop2:
            exec('{} = thisPractice_loop2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instructPractice"-------
    continueRoutine = True
    # update component parameters for each repeat
    if correctKeyRed == 'left':
        practiceInstructions="""
    In the %s posture
    
    Please press;
    %s for red  LETTERS     %s for green  LETTERS
    
    Please respond as quickly and accuractly as possible to the color
    (red or green) in which the  letter-string appeared.  Ignore all other
    aspects of the letter-string, including its meaning.
    
    Let's start with a few practice trials
    This is block %d out of 2 practice blocks
    
    Press any key to start
    """ % (posture, correctKeyRed, correctKeyGreen, practiceLoopIteration)
    else:
        practiceInstructions="""
    In the %s posture
    
    Please press;
    %s for green LETTERS    %s for red LETTERS
    
    Please respond as quickly and accuractly as possible to the color
    (red or green) in which the  letter-string appeared.  Ignore all other
    aspects of the letter-string, including its meaning.
    
    Let's start with a few practice trials
    This is block %d out of 2 practice blocks
    
    Press any key to start
    """ % (posture, correctKeyGreen, correctKeyRed, practiceLoopIteration)
        
    instructPracticeText.setText(practiceInstructions)
    instructPracticeReady.keys = []
    instructPracticeReady.rt = []
    _instructPracticeReady_allKeys = []
    # keep track of which components have finished
    instructPracticeComponents = [instructPracticeText, instructPracticeReady]
    for thisComponent in instructPracticeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructPracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructPractice"-------
    while continueRoutine:
        # get current time
        t = instructPracticeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructPracticeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructPracticeText* updates
        if instructPracticeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructPracticeText.frameNStart = frameN  # exact frame index
            instructPracticeText.tStart = t  # local t and not account for scr refresh
            instructPracticeText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructPracticeText, 'tStartRefresh')  # time at next scr refresh
            instructPracticeText.setAutoDraw(True)
        
        # *instructPracticeReady* updates
        waitOnFlip = False
        if instructPracticeReady.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructPracticeReady.frameNStart = frameN  # exact frame index
            instructPracticeReady.tStart = t  # local t and not account for scr refresh
            instructPracticeReady.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructPracticeReady, 'tStartRefresh')  # time at next scr refresh
            instructPracticeReady.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instructPracticeReady.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instructPracticeReady.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instructPracticeReady.status == STARTED and not waitOnFlip:
            theseKeys = instructPracticeReady.getKeys(keyList=None, waitRelease=False)
            _instructPracticeReady_allKeys.extend(theseKeys)
            if len(_instructPracticeReady_allKeys):
                instructPracticeReady.keys = _instructPracticeReady_allKeys[-1].name  # just the last key pressed
                instructPracticeReady.rt = _instructPracticeReady_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructPracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructPractice"-------
    for thisComponent in instructPracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practiceLoopIteration += 1
    practice_loop2.addData('instructPracticeText.started', instructPracticeText.tStartRefresh)
    practice_loop2.addData('instructPracticeText.stopped', instructPracticeText.tStopRefresh)
    # the Routine "instructPractice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practice2 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('stroop-replication-trialtypes.xlsx'),
        seed=None, name='practice2')
    thisExp.addLoop(practice2)  # add the loop to the experiment
    thisPractice2 = practice2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice2.rgb)
    if thisPractice2 != None:
        for paramName in thisPractice2:
            exec('{} = thisPractice2[paramName]'.format(paramName))
    
    for thisPractice2 in practice2:
        currentLoop = practice2
        # abbreviate parameter names if possible (e.g. rgb = thisPractice2.rgb)
        if thisPractice2 != None:
            for paramName in thisPractice2:
                exec('{} = thisPractice2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        if letterColor == 'red':
            expInfo['correctAnswer'] = correctKeyRed
            correctAnswer = correctKeyRed
        elif letterColor == 'green':
            expInfo['correctAnswer'] = correctKeyGreen
            correctAnswer = correctKeyGreen
        else:
            print("Error, unexpected letterColor:", letterColor)
            sys.exit(0)
        word.setColor(letterColor, colorSpace='rgb')
        word.setText(text)
        resp.keys = []
        resp.rt = []
        _resp_allKeys = []
        # keep track of which components have finished
        trialComponents = [fixation, word, resp]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation* updates
            if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                fixation.setAutoDraw(True)
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                    fixation.setAutoDraw(False)
            
            # *word* updates
            if word.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                word.frameNStart = frameN  # exact frame index
                word.tStart = t  # local t and not account for scr refresh
                word.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(word, 'tStartRefresh')  # time at next scr refresh
                word.setAutoDraw(True)
            if word.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > word.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    word.tStop = t  # not accounting for scr refresh
                    word.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(word, 'tStopRefresh')  # time at next scr refresh
                    word.setAutoDraw(False)
            
            # *resp* updates
            waitOnFlip = False
            if resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                resp.frameNStart = frameN  # exact frame index
                resp.tStart = t  # local t and not account for scr refresh
                resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
                resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > resp.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    resp.tStop = t  # not accounting for scr refresh
                    resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(resp, 'tStopRefresh')  # time at next scr refresh
                    resp.status = FINISHED
            if resp.status == STARTED and not waitOnFlip:
                theseKeys = resp.getKeys(keyList=['left', 'right'], waitRelease=False)
                _resp_allKeys.extend(theseKeys)
                if len(_resp_allKeys):
                    resp.keys = _resp_allKeys[-1].name  # just the last key pressed
                    resp.rt = _resp_allKeys[-1].rt
                    # was this correct?
                    if (resp.keys == str(correctAnswer)) or (resp.keys == correctAnswer):
                        resp.corr = 1
                    else:
                        resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        practice2.addData('fixation.started', fixation.tStartRefresh)
        practice2.addData('fixation.stopped', fixation.tStopRefresh)
        practice2.addData('word.started', word.tStartRefresh)
        practice2.addData('word.stopped', word.tStopRefresh)
        # check responses
        if resp.keys in ['', [], None]:  # No response was made
            resp.keys = None
            # was no response the correct answer?!
            if str(correctAnswer).lower() == 'none':
               resp.corr = 1;  # correct non-response
            else:
               resp.corr = 0;  # failed to respond (incorrectly)
        # store data for practice2 (TrialHandler)
        practice2.addData('resp.keys',resp.keys)
        practice2.addData('resp.corr', resp.corr)
        if resp.keys != None:  # we had a response
            practice2.addData('resp.rt', resp.rt)
        practice2.addData('resp.started', resp.tStartRefresh)
        practice2.addData('resp.stopped', resp.tStopRefresh)
        
        # ------Prepare to start Routine "practiceFeedback"-------
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        if resp.corr:#stored on last run routine
          msg="Correct! RT=%.3f" %(resp.rt)
          sound_hz=60
        else:
          msg="Oops! That was wrong.\nPlease respond as fast and accuractly as you can."
          sound_hz=440
        feedbackPracticeMessage.setText(msg)
        feedbackPracticeSound.setSound(sound_hz, secs=0.5, hamming=True)
        feedbackPracticeSound.setVolume(1.0, log=False)
        # keep track of which components have finished
        practiceFeedbackComponents = [feedbackPracticeMessage, feedbackPracticeSound]
        for thisComponent in practiceFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        practiceFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "practiceFeedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = practiceFeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=practiceFeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedbackPracticeMessage* updates
            if feedbackPracticeMessage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedbackPracticeMessage.frameNStart = frameN  # exact frame index
                feedbackPracticeMessage.tStart = t  # local t and not account for scr refresh
                feedbackPracticeMessage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedbackPracticeMessage, 'tStartRefresh')  # time at next scr refresh
                feedbackPracticeMessage.setAutoDraw(True)
            if feedbackPracticeMessage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedbackPracticeMessage.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    feedbackPracticeMessage.tStop = t  # not accounting for scr refresh
                    feedbackPracticeMessage.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedbackPracticeMessage, 'tStopRefresh')  # time at next scr refresh
                    feedbackPracticeMessage.setAutoDraw(False)
            # start/stop feedbackPracticeSound
            if feedbackPracticeSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedbackPracticeSound.frameNStart = frameN  # exact frame index
                feedbackPracticeSound.tStart = t  # local t and not account for scr refresh
                feedbackPracticeSound.tStartRefresh = tThisFlipGlobal  # on global time
                feedbackPracticeSound.play(when=win)  # sync with win flip
            if feedbackPracticeSound.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedbackPracticeSound.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    feedbackPracticeSound.tStop = t  # not accounting for scr refresh
                    feedbackPracticeSound.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedbackPracticeSound, 'tStopRefresh')  # time at next scr refresh
                    feedbackPracticeSound.stop()
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practiceFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "practiceFeedback"-------
        for thisComponent in practiceFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        practice2.addData('feedbackPracticeMessage.started', feedbackPracticeMessage.tStartRefresh)
        practice2.addData('feedbackPracticeMessage.stopped', feedbackPracticeMessage.tStopRefresh)
        feedbackPracticeSound.stop()  # ensure sound has stopped at end of routine
        practice2.addData('feedbackPracticeSound.started', feedbackPracticeSound.tStartRefresh)
        practice2.addData('feedbackPracticeSound.stopped', feedbackPracticeSound.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'practice2'
    
    # get names of stimulus parameters
    if practice2.trialList in ([], [None], None):
        params = []
    else:
        params = practice2.trialList[0].keys()
    # save data for this loop
    practice2.saveAsExcel(filename + '.xlsx', sheetName='practice2',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'practice_loop2'

# get names of stimulus parameters
if practice_loop2.trialList in ([], [None], None):
    params = []
else:
    params = practice_loop2.trialList[0].keys()
# save data for this loop
practice_loop2.saveAsExcel(filename + '.xlsx', sheetName='practice_loop2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
trial_loop2 = data.TrialHandler(nReps=4.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trial_loop2')
thisExp.addLoop(trial_loop2)  # add the loop to the experiment
thisTrial_loop2 = trial_loop2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_loop2.rgb)
if thisTrial_loop2 != None:
    for paramName in thisTrial_loop2:
        exec('{} = thisTrial_loop2[paramName]'.format(paramName))

for thisTrial_loop2 in trial_loop2:
    currentLoop = trial_loop2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_loop2.rgb)
    if thisTrial_loop2 != None:
        for paramName in thisTrial_loop2:
            exec('{} = thisTrial_loop2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instructTrial"-------
    continueRoutine = True
    # update component parameters for each repeat
    if correctKeyRed == 'left':
        trialInstructions="""
    Take a small break and then CHECK  your posture before continuing
    
    You should still be in the %s posture
    
    OK. Ready for the real thing?
    
    Remember, ignore the word itself; press:
    %s for red LETTERS   %s for green LETTERS
    
    Please respond as quickly and accuractly as possible to the color
    (red or green) in which the  letter-string appeared.  Ignore all other
    aspects of the letter-string, including its meaning.
    
    This is block %d out of 4 experiment blocks
    
    Press any key to start
    """ % (posture, correctKeyRed, correctKeyGreen, trialLoopIteration)
    else:
        trialInstructions="""
    Take a small break and then CHECK  your posture before continuing
    
    You should still be in the %s posture
    
    OK. Ready for the real thing?
    
    Remember, ignore the word itself; press:
    %s for green LETTERS   %s for red LETTERS
    
    Please respond as quickly and accuractly as possible to the color
    (red or green) in which the  letter-string appeared.  Ignore all other
    aspects of the letter-string, including its meaning.
    
    This is block %d out of 4 experiment blocks
    
    Press any key to start
    """ % (posture, correctKeyGreen, correctKeyRed, trialLoopIteration)
    
    
    instructTrialText.setText(trialInstructions)
    instructTrialReady.keys = []
    instructTrialReady.rt = []
    _instructTrialReady_allKeys = []
    # keep track of which components have finished
    instructTrialComponents = [instructTrialText, instructTrialReady]
    for thisComponent in instructTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructTrial"-------
    while continueRoutine:
        # get current time
        t = instructTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructTrialText* updates
        if instructTrialText.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            instructTrialText.frameNStart = frameN  # exact frame index
            instructTrialText.tStart = t  # local t and not account for scr refresh
            instructTrialText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructTrialText, 'tStartRefresh')  # time at next scr refresh
            instructTrialText.setAutoDraw(True)
        
        # *instructTrialReady* updates
        waitOnFlip = False
        if instructTrialReady.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            instructTrialReady.frameNStart = frameN  # exact frame index
            instructTrialReady.tStart = t  # local t and not account for scr refresh
            instructTrialReady.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructTrialReady, 'tStartRefresh')  # time at next scr refresh
            instructTrialReady.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instructTrialReady.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instructTrialReady.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instructTrialReady.status == STARTED and not waitOnFlip:
            theseKeys = instructTrialReady.getKeys(keyList=None, waitRelease=False)
            _instructTrialReady_allKeys.extend(theseKeys)
            if len(_instructTrialReady_allKeys):
                instructTrialReady.keys = _instructTrialReady_allKeys[-1].name  # just the last key pressed
                instructTrialReady.rt = _instructTrialReady_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructTrial"-------
    for thisComponent in instructTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialLoopIteration += 1
    trial_loop2.addData('instructTrialText.started', instructTrialText.tStartRefresh)
    trial_loop2.addData('instructTrialText.stopped', instructTrialText.tStopRefresh)
    # the Routine "instructTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials2 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('stroop-replication-trialtypes.xlsx'),
        seed=None, name='trials2')
    thisExp.addLoop(trials2)  # add the loop to the experiment
    thisTrials2 = trials2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials2.rgb)
    if thisTrials2 != None:
        for paramName in thisTrials2:
            exec('{} = thisTrials2[paramName]'.format(paramName))
    
    for thisTrials2 in trials2:
        currentLoop = trials2
        # abbreviate parameter names if possible (e.g. rgb = thisTrials2.rgb)
        if thisTrials2 != None:
            for paramName in thisTrials2:
                exec('{} = thisTrials2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        if letterColor == 'red':
            expInfo['correctAnswer'] = correctKeyRed
            correctAnswer = correctKeyRed
        elif letterColor == 'green':
            expInfo['correctAnswer'] = correctKeyGreen
            correctAnswer = correctKeyGreen
        else:
            print("Error, unexpected letterColor:", letterColor)
            sys.exit(0)
        word.setColor(letterColor, colorSpace='rgb')
        word.setText(text)
        resp.keys = []
        resp.rt = []
        _resp_allKeys = []
        # keep track of which components have finished
        trialComponents = [fixation, word, resp]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation* updates
            if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                fixation.setAutoDraw(True)
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                    fixation.setAutoDraw(False)
            
            # *word* updates
            if word.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                word.frameNStart = frameN  # exact frame index
                word.tStart = t  # local t and not account for scr refresh
                word.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(word, 'tStartRefresh')  # time at next scr refresh
                word.setAutoDraw(True)
            if word.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > word.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    word.tStop = t  # not accounting for scr refresh
                    word.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(word, 'tStopRefresh')  # time at next scr refresh
                    word.setAutoDraw(False)
            
            # *resp* updates
            waitOnFlip = False
            if resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                resp.frameNStart = frameN  # exact frame index
                resp.tStart = t  # local t and not account for scr refresh
                resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
                resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > resp.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    resp.tStop = t  # not accounting for scr refresh
                    resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(resp, 'tStopRefresh')  # time at next scr refresh
                    resp.status = FINISHED
            if resp.status == STARTED and not waitOnFlip:
                theseKeys = resp.getKeys(keyList=['left', 'right'], waitRelease=False)
                _resp_allKeys.extend(theseKeys)
                if len(_resp_allKeys):
                    resp.keys = _resp_allKeys[-1].name  # just the last key pressed
                    resp.rt = _resp_allKeys[-1].rt
                    # was this correct?
                    if (resp.keys == str(correctAnswer)) or (resp.keys == correctAnswer):
                        resp.corr = 1
                    else:
                        resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials2.addData('fixation.started', fixation.tStartRefresh)
        trials2.addData('fixation.stopped', fixation.tStopRefresh)
        trials2.addData('word.started', word.tStartRefresh)
        trials2.addData('word.stopped', word.tStopRefresh)
        # check responses
        if resp.keys in ['', [], None]:  # No response was made
            resp.keys = None
            # was no response the correct answer?!
            if str(correctAnswer).lower() == 'none':
               resp.corr = 1;  # correct non-response
            else:
               resp.corr = 0;  # failed to respond (incorrectly)
        # store data for trials2 (TrialHandler)
        trials2.addData('resp.keys',resp.keys)
        trials2.addData('resp.corr', resp.corr)
        if resp.keys != None:  # we had a response
            trials2.addData('resp.rt', resp.rt)
        trials2.addData('resp.started', resp.tStartRefresh)
        trials2.addData('resp.stopped', resp.tStopRefresh)
        
        # ------Prepare to start Routine "trialFeedback"-------
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        if resp.corr:#stored on last run routine
          msg="."
          sound_hz=60
        else:
          msg="."
          sound_hz=440
        sound_2.setSound(sound_hz, secs=0.5, hamming=True)
        sound_2.setVolume(1.0, log=False)
        # keep track of which components have finished
        trialFeedbackComponents = [feedback_3, sound_2]
        for thisComponent in trialFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trialFeedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialFeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialFeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_3* updates
            if feedback_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_3.frameNStart = frameN  # exact frame index
                feedback_3.tStart = t  # local t and not account for scr refresh
                feedback_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_3, 'tStartRefresh')  # time at next scr refresh
                feedback_3.setAutoDraw(True)
            if feedback_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_3.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_3.tStop = t  # not accounting for scr refresh
                    feedback_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedback_3, 'tStopRefresh')  # time at next scr refresh
                    feedback_3.setAutoDraw(False)
            # start/stop sound_2
            if sound_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sound_2.frameNStart = frameN  # exact frame index
                sound_2.tStart = t  # local t and not account for scr refresh
                sound_2.tStartRefresh = tThisFlipGlobal  # on global time
                sound_2.play(when=win)  # sync with win flip
            if sound_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_2.tStop = t  # not accounting for scr refresh
                    sound_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(sound_2, 'tStopRefresh')  # time at next scr refresh
                    sound_2.stop()
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trialFeedback"-------
        for thisComponent in trialFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials2.addData('feedback_3.started', feedback_3.tStartRefresh)
        trials2.addData('feedback_3.stopped', feedback_3.tStopRefresh)
        sound_2.stop()  # ensure sound has stopped at end of routine
        trials2.addData('sound_2.started', sound_2.tStartRefresh)
        trials2.addData('sound_2.stopped', sound_2.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials2'
    
    # get names of stimulus parameters
    if trials2.trialList in ([], [None], None):
        params = []
    else:
        params = trials2.trialList[0].keys()
    # save data for this loop
    trials2.saveAsExcel(filename + '.xlsx', sheetName='trials2',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'trial_loop2'

# get names of stimulus parameters
if trial_loop2.trialList in ([], [None], None):
    params = []
else:
    params = trial_loop2.trialList[0].keys()
# save data for this loop
trial_loop2.saveAsExcel(filename + '.xlsx', sheetName='trial_loop2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "thanks"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [thanksText]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thanksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thanksClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanksText* updates
    if thanksText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanksText.frameNStart = frameN  # exact frame index
        thanksText.tStart = t  # local t and not account for scr refresh
        thanksText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanksText, 'tStartRefresh')  # time at next scr refresh
        thanksText.setAutoDraw(True)
    if thanksText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thanksText.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            thanksText.tStop = t  # not accounting for scr refresh
            thanksText.frameNStop = frameN  # exact frame index
            win.timeOnFlip(thanksText, 'tStopRefresh')  # time at next scr refresh
            thanksText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thanksText.started', thanksText.tStartRefresh)
thisExp.addData('thanksText.stopped', thanksText.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
