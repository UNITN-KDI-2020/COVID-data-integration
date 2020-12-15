import pandas as pd


hospitalization_all_loc = pd.read_csv(
    "../../dataset/Informal Modeling/data/Reference_hospitalization_all_locs.csv")

hospitalization_all_loc['year'] = pd.DatetimeIndex(
    hospitalization_all_loc['date']).year
hospitalization_all_loc['month'] = pd.DatetimeIndex(
    hospitalization_all_loc['date']).month
hospitalization_all_loc['day'] = pd.DatetimeIndex(
    hospitalization_all_loc['date']).day

# ,est_infections_mean,est_infections_lower,est_infections_upper,confirmed_infections_p100k_rate,est_infections_mean_p100k_rate,est_infections_lower_p100k_rate,est_infections_upper_p100k_rate
hospitalization_all_loc.drop(['location_id', 'date', 'admis_mean', 'deaths_mean', 'deaths_lower', 'deaths_upper', 
                             'totdea_mean', 'deaths_mean_smoothed', 'deaths_lower_smoothed', 
                             'deaths_upper_smoothed', 'totdea_mean_smoothed', 'totdea_lower_smoothed', 
                             'totdea_upper_smoothed', 'mobility_data_type', 'mobility_composite', 
                             'total_tests_data_type', 'confirmed_infections', 'est_infections_mean',
                             'confirmed_infections_p100k_rate', 'est_infections_mean_p100k_rate', 'est_infections_lower_p100k_rate', 'est_infections_upper_p100k_rate'],
                              inplace=True, axis=1)

hospitalization_all_loc.head()
hospitalization_all_loc.to_csv(
    r"../../dataset/Formal Modeling/data/Reference_hospitalization_all_locs.csv", index=False)
