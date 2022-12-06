import pandas as pd



df = pd.read_csv('classfiles/gapminder/gapminder.tsv', sep='\t')
pd.read_csv

print(df)
print(df.shape)



print(df.loc[0:9,['country','year']])





