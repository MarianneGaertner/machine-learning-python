import pandas as pd

alunosDIC = {'Nome': ['Ricardo', 'Pedro', 'Roberto', 'Carlos'],
          'Nota': [4, 6, 5.5, 9],
          'Aprovado': ['Não', 'Sim', 'Não', 'Sim']}

alunosDF = pd.DataFrame(alunosDIC)
print(alunosDF)

print(alunosDF.head())
print(alunosDF.shape)
print(alunosDF.describe())
