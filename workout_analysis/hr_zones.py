import numpy as np


def assign_hr_zone(df):
    """Assigns HR zone to each HR value in the dataframe

    Parameters
    ----------
    df : pandas.DataFrame
        Dataframe containing HR data

    Returns
    -------
    df : pandas.DataFrame
        Dataframe containing HR data with HR zone column
    """
    hr_zone = np.zeros(len(df["HR"]))

    for hr_idx, hr in enumerate(df["HR"]):
        if hr < 105:
            hr_zone[hr_idx] = 0
        elif hr >= 105 and hr < 140:
            hr_zone[hr_idx] = 1
        elif hr >= 140 and hr < 157:
            hr_zone[hr_idx] = 2
        elif hr >= 157 and hr < 170:
            hr_zone[hr_idx] = 3
        elif hr >= 170 and hr < 188:
            hr_zone[hr_idx] = 4
        elif hr >= 188:
            hr_zone[hr_idx] = 5

    df["HR zone"] = hr_zone

    return df