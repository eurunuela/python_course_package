import os

from workout_analysis.workout_analysis import workout_analysis


def test_integration():
    out_filename = "test.png"
    workout_analysis(infile="https://physionet.org/files/treadmill-exercise-cardioresp/1.0.1/test_measure.csv", outfile=out_filename)
    assert os.path.exists(out_filename)