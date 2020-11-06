import pandas as pd


# Unzip the "Reference_hospitalization_all_locs.zip" file and
# load the csv
hospitalization_all_loc = pd.read_csv(
    "../../dataset/source/data/Reference_hospitalization_all_locs.csv")
hospitalization_all_loc.head()

# select the attributes required
hospitalization_all_loc = hospitalization_all_loc[['location_id', 'date', 'location_name', 'admis_mean', 'deaths_mean', 'deaths_lower', 'deaths_upper', 'totdea_mean', 'deaths_mean_smoothed', 'deaths_lower_smoothed', 'deaths_upper_smoothed', 'totdea_mean_smoothed', 'totdea_lower_smoothed', 'totdea_upper_smoothed',
                                                   'mobility_data_type', 'mobility_composite', 'total_tests_data_type', 'confirmed_infections', 'est_infections_mean', 'est_infections_lower', 'est_infections_upper', 'confirmed_infections_p100k_rate', 'est_infections_mean_p100k_rate', 'est_infections_lower_p100k_rate', 'est_infections_upper_p100k_rate']]

hospitalization_all_loc.to_csv(
    r"../../dataset/Informal Modeling/data/Reference_hospitalization_all_locs.csv", index=False)
