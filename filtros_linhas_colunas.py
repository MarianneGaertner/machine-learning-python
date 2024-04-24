import pandas as pd

alunosDIC = {'Nome': ['Ricardo', 'Pedro', 'Roberto', 'Carlos'],
          'Nota': [4, 6, 5.5, 9],
          'Aprovado': ['Não', 'Sim', 'Não', 'Sim']}

alunosDF = pd.DataFrame(alunosDIC)

#print(alunosDF['Nome']) # filtrar colunas específicas
print(alunosDF.loc[[0]])
print(alunosDF.loc[1:3])

localiza1 = alunosDF.loc[alunosDF['Nome']=='Pedro'] # localizar dentro do dataframe
print(localiza1)

localiza2 = alunosDF.loc[alunosDF['Nota']==9]
print(localiza2)

localiza3 = alunosDF.loc[alunosDF['Aprovado']=='Sim']
print(localiza3)