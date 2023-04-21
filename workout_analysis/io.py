import pandas as pd


def read_hr_data(infile):
    df = pd.read_csv(infile, sep=",")

    return df