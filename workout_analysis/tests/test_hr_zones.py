import pandas as pd

from workout_analysis.hr_zones import assign_hr_zone


def test_assign_hr_zone():

    hr_data = {
        "HR": [100, 115, 142, 167, 178, 198, 200]
    }
    original_zones = [0, 1, 2, 3, 4, 5, 5]
    df = pd.DataFrame(hr_data)
    
    assigned_hr_zones = assign_hr_zone(df)

    assigned_hr_zones = assigned_hr_zones["HR zone"].to_list()

    assert assigned_hr_zones == original_zones


def test_assign_hr_zone_two():
    hr_data = {
        "HR": [115, 198, 142, 100, 200, 167, 178]
    }
    original_zones = [1, 5, 2, 0, 5, 3, 4]
    df = pd.DataFrame(hr_data)
    
    assigned_hr_zones = assign_hr_zone(df)

    assigned_hr_zones = assigned_hr_zones["HR zone"].to_list()

    assert assigned_hr_zones == original_zones