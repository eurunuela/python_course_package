import argparse
import datetime
import logging
from os import path as op

from workout_analysis.hr_zones import assign_hr_zone
from workout_analysis.io import read_hr_data
from workout_analysis.plotting import create_hr_graph
from workout_analysis.utils import setup_loggers, teardown_loggers

LGR = logging.getLogger("GENERAL")
RepLGR = logging.getLogger("REPORT")

def _get_parser():
    parser = argparse.ArgumentParser(description="Workout Analysis Program")
    parser.add_argument("-f", "--file", help="Input file", required=True, dest="infile")
    parser.add_argument("-o", "--output", help="Output file", required=True, dest="outfile")
    return parser

def workout_analysis(infile, outfile):
    print("Workout Analysis Program v1.0")
    print("Input file: {}".format(infile))
    print("Output file: {}".format(outfile))

    out_dir = "."

    # create logfile name
    basename = "workout_analysis_"
    extension = "tsv"
    start_time = datetime.datetime.now().strftime("%Y-%m-%dT%H%M%S")
    logname = op.join(out_dir, (basename + start_time + "." + extension))
    setup_loggers(logname)

    LGR.info("Reading data")
    df = read_hr_data(infile)

    LGR.info("Assigning HR zones")
    df_hr_assigned = assign_hr_zone(df)

    LGR.info("Creating and saving graph")
    create_hr_graph(df_hr_assigned, outfile)

    LGR.info("Finished")

    teardown_loggers()


def _main(argv=None):
    options = _get_parser().parse_args(argv)
    kwargs = vars(options)
    workout_analysis(**kwargs)

if __name__ == "__main__":
    _main()