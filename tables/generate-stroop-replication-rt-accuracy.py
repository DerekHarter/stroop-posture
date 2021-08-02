#!/usr/bin/env python
"""Generate a LaTeX table of results of accuracy and
reaction time means and standard deviations for 
stroop replication grouped by posture and congruancy
conditions.

"""
import argparse
import pandas as pd


# other global constants / locations.  parameterize these if we need
# flexibility to specify them on command line or move them around
table_dir = '.'
description = """
This script will generate a table of results summarizing
the accuracy and reaction time experimental data for all
subjects, grouped by the experiment posture and congruancy
conditions.
"""


def generate_rt_accuracy_df(data_file):
    """Generate summary dataframe or reaction time and accuracy results
    from input data file.

    Parameters
    ----------
    data_file - The name of the data file to open and load in for processing.
      Expected to be a csv file suitable for load by pandas read_csv.

    Returns
    -------
    rt_accuracy_df - Returns a pandas dataframe summarizing reaction time and
      accuracy data collected from experiments.
    """
    # load input data frame
    df = pd.read_csv(data_file)

    # group data by posture and congruant conditions
    gdf = df.groupby(['posture', 'congruent'])

    # construct a resulting summary dataframe of this grouped
    # data
    summary_dict = {
        'accuracy.mean': gdf['resp.corr'].mean(),
        'accuracy.std': gdf['resp.corr'].std(),
        'rt.mean': gdf['resp.rt'].mean(),
        'rt.std': gdf['resp.rt'].std()
    }
    rt_accuracy_df = pd.DataFrame(summary_dict)    

    # return the resulting dataframe
    return rt_accuracy_df


def save_table(rt_accuracy_df, output_file):
    """Create and save a generated LaTeX table of this dataframe.

    Parameters
    ----------
    rt_accuracy_df - A dataframe of the summarized reaction time and
      accuracy data.
    output_file - The name of the file to save the table into.
    """
    caption = "Accuracy and reaction time performance of subjects broken down by posture (sitting, standing) and congruancy (congruant, incongruant) conditions."
    label = "table-stroop-replication-rt-accuracy"
    rt_accuracy_df.to_latex(output_file,
                            index=True,
                            header=True,
                            bold_rows=False,
                            float_format="%0.4f",
                            caption=caption,
                            label=label,
                            longtable=False,
                            )


def main():
    """Main entry point for this figure visualizaiton creation
    """
    # parse command line arguments
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('data', 
                        help='the name of the experiment (cleaned) data file to open and process')
    parser.add_argument('--output', default=None,
                        help='name of output table, defaults to table-stroop-replication-rt-accuracy.tex')
    args = parser.parse_args()

    # determine output file name if not given explicitly
    output_file = args.output
    if output_file is None:
        # make full output file name, assume .png output by default
        output_file = 'table-stroop-replication-rt-accuracy.tex'


    # generate and save the table for the asked for models
    rt_accuracy_df = generate_rt_accuracy_df(args.data)
    save_table(rt_accuracy_df, output_file)


if __name__ == "__main__":
    main()
