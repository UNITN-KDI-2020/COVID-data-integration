import pandas as pd


# Load the csv file
stato_clinico = pd.read_csv(
    "../../dataset/source/data/stato_clinico_td.csv")
stato_clinico.head()

# select the attributes required 
stato_clinico = stato_clinico[['giorno', 'guariti', 'deceduti',
                               'totale_pos', 'pos_att', 'rsa', 'casa_cura', 'tot_rsa', 'tot_dime']]

stato_clinico.to_csv(
    r"../../dataset/Informal Modeling/data/stato_clinico_td.csv", index=False)
