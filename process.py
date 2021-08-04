import pandas as pd

df = pd.read_excel('./Athletes.xlsx')
#disciplines = pd.Series(df['Discipline'].unique())
#disciplines.to_csv('./Disciplines.csv')
countries = pd.Series(df['NOC'].unique())
countries.to_csv('./Countries.csv')