import pandas as pd


# Load the csv file
summary_stats = pd.read_csv(
    "../../dataset/Informal Modeling/data/Summary_stats_all_locs.csv")

# # select the attributes required
# summary_stats = summary_stats[['location_name', 'location_id', 'travel_limit_start_date', 'travel_limit_end_date', 
# 'stay_home_start_date', 'stay_home_end_date', 
# 'educational_fac_start_date', 'educational_fac_end_date',
#  'any_gathering_restrict_start_date', 'any_gathering_restrict_end_date',
#  'any_business_start_date', 'any_business_end_date', 
# 'all_non-ess_business_start_date', 'all_non-ess_business_end_date']]

summary_stats.columns = summary_stats.columns.str.strip()

new_summary = pd.DataFrame(columns=['location_name', 'restriction_type', 'closure_start', 'closure_end'])

for row in summary_stats.itertuples(index=True, name='Pandas'):
    if not (pd.isnull(row.travel_limit_start_date) or row.travel_limit_start_date == "" or pd.isna(row.travel_limit_start_date)):
        new_summary = new_summary.append({'location_name': row.location_name, 'restriction_type': 'Travel', 'closure_start': row.travel_limit_start_date, 'closure_end': row.travel_limit_end_date}, ignore_index=True)

    if not (pd.isnull(row.stay_home_start_date) or row.stay_home_start_date == "" or pd.isna(row.stay_home_start_date)):
        new_summary = new_summary.append({'location_name': row.location_name, 'restriction_type': 'Lockdown', 'closure_start': row.travel_limit_start_date, 'closure_end': row.travel_limit_end_date}, ignore_index=True)

    if not (pd.isnull(row.educational_fac_start_date) or row.educational_fac_start_date == "" or pd.isna(row.educational_fac_start_date)):
        new_summary = new_summary.append({'location_name': row.location_name, 'restriction_type': 'Institutional', 'closure_start': row.travel_limit_start_date, 'closure_end': row.travel_limit_end_date}, ignore_index=True)

    if not (pd.isnull(row.any_gathering_restrict_start_date) or row.any_gathering_restrict_start_date == "" or pd.isna(row.any_gathering_restrict_start_date)):
        new_summary = new_summary.append({'location_name': row.location_name, 'restriction_type': 'Gathering', 'closure_start': row.travel_limit_start_date, 'closure_end': row.travel_limit_end_date}, ignore_index=True)

    if not (pd.isnull(row.any_business_start_date) or row.any_business_start_date == "" or pd.isna(row.any_business_start_date)):
        new_summary = new_summary.append({'location_name': row.location_name, 'restriction_type': 'Essential Business', 'closure_start': row.travel_limit_start_date, 'closure_end': row.travel_limit_end_date}, ignore_index=True)

    if not (pd.isnull(row[12]) or row[13] == "" or pd.isna(row[13])):
        new_summary = new_summary.append({'location_name': row.location_name, 'restriction_type': 'Non-Essential Business', 'closure_start': row.travel_limit_start_date, 'closure_end': row.travel_limit_end_date}, ignore_index=True)

new_summary.to_csv(
    r"../../dataset/Formal Modeling/data/Summary_stats_all_locs.csv", index=False)
