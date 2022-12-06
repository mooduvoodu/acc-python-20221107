import pandas as pd

df=pd.read_csv('classfiles/gapminder/gapminder.tsv', sep='\t')
pd.read_csv


#print(df)


#print(df.info())

coltosee=df[['country','lifeExp']]
#print(coltosee.head(10))
#print(coltosee.tail(10))

print(df.loc[155:162])