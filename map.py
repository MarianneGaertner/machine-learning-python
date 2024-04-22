kmh = [40,50,56,64,73,79,85,96,100,120]

mph1 = []
for i in kmh:
    mph1.append(i/1.61)
print(mph1)    

mph2 = list(map(lambda x: x/1.61, kmh)) 
# a função map pode ser utilizada para subistituir, em alguns casos, o loop for. map(função que queremos fazer, dados que queremos "passar" pela função). precisamos colocar em qual formato queremos exibir o resultado, no caso, lista
print(mph2)