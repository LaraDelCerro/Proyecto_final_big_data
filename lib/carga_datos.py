import pandas as pd


#datos Europa
df_europa = pd.read_csv('./data/Europa.csv')
#print(df_europa)

#datos África
df_africa = pd.read_csv('./data/Africa.csv')
#print(df_africa)

#datos Asia
df_asia = pd.read_csv('./data/Asia.csv')
#print(df_asia)

#datos América
df_america = pd.read_csv('./data/America.csv')
#print(df_america)

#datos Oceanía
df_oceania = pd.read_csv('./data/Oceania.csv')
#print(df_oceania)

#unir todos los dataframes en uno solo
df_continentes = pd.concat([df_europa, df_africa, df_asia, df_america, df_oceania], ignore_index=True)
print(df_continentes)

