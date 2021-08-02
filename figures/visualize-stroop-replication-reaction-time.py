#!/usr/bin/env python
"""Create figure visualization of stroop replication
experiment reaction time results.  This figure summarizes
reaction times broken down by posture (sitting vs. standing)
and congruancy (congruant vs. incongruant) conditions.

"""
import argparse
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd


# other global constants / locations.  parameterize these if we need
# flexibility to specify them on command line or move them around
figure_dir = '.'
description = """ This script creates a figure visualization of the stroop
replication experiment reaction time results.  The figure summarizes
reaction times of subjects broken down by posture (sitting
vs. standing) and congruancy (congruant vs. incongruant) conditions.
"""


def create_reaction_time_figure(data_file, output_file):
    """Create and save the summarized reaction time figure broken down
    by posture and congruancy conditions.

    Parameters
    ----------
    data_file - The name of the input data file to load and process for
      figure visualization.  This is assumed to be a csv formatted file
      suitable to be read in by pandas read_csv() function.
    output_file - The resulting figure file name to create.
    """
    # load in data to dataframe for processing
    df = pd.read_csv(data_file)

    # using seaborn high-level df, visualize reaction time by posture, and
    # using the hue (color) to split by congruent/incongruent
    fig, ax1 = plt.subplots(figsize=(12, 8))
    sb.barplot(x='posture', y='resp.rt', hue='congruent', data=df, ci=95)

    # add in figure information and labels
    plt.xlabel('Posture condition (sitting vs. standing)')
    plt.ylabel('Reaction Time (ms)')
    plt.title('Summary of Reaction Time of Stroop Repliction, Posture and Congruancy conditions')
    
    # save the resulting figure
    plt.savefig(output_file, transparent=True, dpi=300)


def main():
    """Main entry point for this figure visualizaiton creation
    """
    # parse command line arguments
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('data',
                        help='the name of the input data file to load and create figure from')
    parser.add_argument('--output', default=None,
                        help='name of output figure, defaults to figure-stroop-replication-reaction-time.png')
    args = parser.parse_args()

    # determine output file name if not given explicitly
    output_file = args.output
    if output_file is None:
        # make full output file name, assume .png output by default
        output_file = 'figure-stroop-replication-reaction-time.png'

    # generate and save the figure for the asked for model
    create_reaction_time_figure(args.data, output_file)


if __name__ == "__main__":
    main()
