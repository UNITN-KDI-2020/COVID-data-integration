import pandas as pd


# Load the xlsx file
covid19 = pd.read_excel("../../dataset/source/data/COVID-19-geographic-disbtribution-worldwide.xlsx",
                        sheet_name="COVID-19-geographic-disbtributi")

# select the attributes required 
covid19 = covid19[['dateRep', 'cases', 'deaths', 'countriesAndTerritories']]

covid19.to_csv(
    r"../../dataset/Informal Modeling/data/COVID-19-geographic-disbtribution-worldwide.csv", index=False)
