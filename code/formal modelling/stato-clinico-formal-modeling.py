import pandas as pd


# Load the csv file
stato_clinico = pd.read_csv(
    "../../dataset/Informal Modeling/data/stato_clinico_td.csv")
stato_clinico.head()

# select the attributes required 
# stato_clinico = stato_clinico[['giorno', 'guariti', 'deceduti',
#                                'totale_pos', 'pos_att', 'rsa', 'casa_cura', 'tot_rsa', 'tot_dime']]
stato_clinico['year'] = pd.DatetimeIndex(stato_clinico['giorno']).year
stato_clinico['month'] = pd.DatetimeIndex(stato_clinico['giorno']).month
stato_clinico['day'] = pd.DatetimeIndex(stato_clinico['giorno']).day

stato_clinico.drop(['giorno', 'totale_pos','tot_dime', 'tot_rsa', 'casa_cura'], inplace=True, axis=1)


stato_clinico.to_csv(
    r"../../dataset/Formal Modeling/data/stato_clinico_td.csv", index=False)
