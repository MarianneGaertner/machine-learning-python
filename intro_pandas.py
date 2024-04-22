import pandas as pd
dados = pd.read_excel("testepandas.xlsx")
print(dados.head(8))


dados2 = pd.read_csv("athlete_events.csv")
print(dados2.head(5))
