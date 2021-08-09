#!/usr/bin/env python
"""Extract stroop replication data for data analysis from
raw subject trial files and raw subject trial meta-experiment
data files.

"""
import os
import sys
import argparse
import glob
import pandas as pd


# other global constants / locations.  parameterize these if we need
# flexibility to specify them on command line or move them around
data_dir = '.'
description = """
This script extracts all stroop replication subject trials into
a single file for data analysis.  We extract some information
from the experiment meta file as well.  The result is a tidy
data file, in csv format, with 1 trial per line, and normalized
feature/column names.
"""

# information used in cleaning raw data trials for extraction
# list of practice columns/features to be dropped when extracting
practice_features = ['practice.thisRepN', 'practice.thisTrialN', 'practice.thisN', 'practice.thisIndex']

# list of unuseful features to drop
unused_features = ['instr1.started', 'instr1.stopped', 'word.stopped', 'resp.stopped',
                   'feedback_2.started', 'feedback_2.stopped', 'instrText.started',
                   'instrText.stopped', 'thanksText.started', 'thanksText.stopped',
                   'expName', 'psychopyVersion', 'frameRate']

# final features desired, and order we desire them in
features = ['participant', 'posture', 'session', 'date',
            'text', 'letterColor', 'correctAnswer', 'congruent',
            'trial_loop.thisRepN', 'trials.thisTrialN', 'trials.thisN', 'trials.thisIndex',
	    'word.started', 'resp.keys', 'resp.corr', 'resp.rt', 'resp.started']


def extract_stroop_replication_data():
    """Extract subject trials and create a tidy data file from raw
    trial data.  We extract data from PsychoPy subject .csv raw
    trial output files, and also need some meta information about
    other conditions from the corresponding PsychoPy meta-experiment
    file.  Result is returned as a clean/tidy pandas dataframe.

    Returns
    -------
    df - Returns a pandas dataframe of the extracted and cleaned
         stroop replication data.
    """
    # will hold result to return
    stroop_replication_df = None
    
    # find files matching raw PsychoPy subject trial/data name
    file_pattern = "[0-9][0-9][0-9][0-9]_*_*_*"
    raw_data_pattern = data_dir + "/" + file_pattern + ".csv"
    raw_data_file_list = glob.glob(raw_data_pattern)
    raw_data_file_list.sort()
    for raw_data_file in raw_data_file_list:
        #print('Processing file <%s>' % raw_data_file)
        # read csv into a dataframe
        subject_df = pd.read_csv(raw_data_file)
        
        # clean a bit, drop all rows where trials.thisRepN is empty, this
        # removes practice trials and rows of start/stop info leaving only
        # actual trials
        subject_df.dropna(subset=['trials.thisRepN'], inplace=True)

        # drop feature columns with only practice data
        subject_df.drop(practice_features, axis=1, inplace=True)

        # drop all other features unneded for data analysis
        subject_df.drop(unused_features, axis=1, inplace=True)

        # append this subject data to data frame
        if stroop_replication_df is None:
            stroop_replication_df = subject_df
        else:
            stroop_replication_df = pd.concat([stroop_replication_df, subject_df], ignore_index=True)

    # rearrange feature columns as desired, and final check we have all and exactly the features
    # extracted that we desire
    stroop_replication_df = stroop_replication_df[features]

    # clean date/time stamp to an actual datetime instead of a string
    stroop_replication_df['date'] = pd.to_datetime(stroop_replication_df['date'], format='%Y_%b_%d_%H%M')
    
    # return resulting dataframe
    return stroop_replication_df


def save_stroop_replication_data(data_file_name, stroop_replication_df):
    """Save extracted data fame to output file as a csv formatted
    data file.

    Parameters
    ----------
    data_file_name - Name to save extracted data file to
    stroop_replication_df - A pandas dataframe of the data to save
    """
    stroop_replication_df.to_csv(data_file_name, index=False)


def main():
    """Main entry point for this figure visualizaiton creation
    """
    # parse command line arguments
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--output', default='stroop-replication.csv',
                        help='name of output data file, defaults to stroop-replication.csv')
    args = parser.parse_args()

    # extract the trials and experiment data from the raw files
    stroop_replication_df = extract_stroop_replication_data()
    save_stroop_replication_data(args.output, stroop_replication_df)

if __name__ == "__main__":
    main()
