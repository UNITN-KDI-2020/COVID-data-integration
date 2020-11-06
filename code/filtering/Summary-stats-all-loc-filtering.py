import pandas as pd


# Load the csv file
summary_stats = pd.read_csv(
    "../../dataset/source/data/Summary_stats_all_locs.csv")

# select the attributes required 
summary_stats = summary_stats[['location_name', 'location_id', 'travel_limit_start_date', 'travel_limit_end_date', 'stay_home_start_date', 'stay_home_end_date', 'educational_fac_start_date', 'educational_fac_end_date',
                               'any_gathering_restrict_start_date', 'any_gathering_restrict_end_date', 'any_business_start_date', 'any_business_end_date', 'all_non-ess_business_start_date', 'all_non-ess_business_end_date']]


summary_stats.to_csv(
    r"../../dataset/Informal Modeling/data/Summary_stats_all_locs.csv", index=False)
