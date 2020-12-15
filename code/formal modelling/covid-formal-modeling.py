import pandas as pd


# Load the xlsx file
covid19 = pd.read_csv("../../dataset/Informal Modeling/data/COVID-19-geographic-disbtribution-worldwide.csv")

covid19['year'] = pd.DatetimeIndex(covid19['dateRep']).year
covid19['month'] = pd.DatetimeIndex(covid19['dateRep']).month
covid19['day'] = pd.DatetimeIndex(covid19['dateRep']).day

covid19.drop(['dateRep', 'Unnamed: 0'], inplace=True, axis=1)

covid19.head()
covid19.to_csv(
    r"../../dataset/Formal Modeling/data/COVID-19-geographic-disbtribution-worldwide.csv", index=False)
