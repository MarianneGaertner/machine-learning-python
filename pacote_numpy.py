import numpy as np
a = np.array([1,2,3])
print(a)

b = np.array([(2,5,7),(5,3,9),(6,7,8)])
print(b)

# matriz de zeros
c = np.zeros((4,3))
print(c)

# matriz com a diagonal com 1's e o resto com zeros
d = np.eye(4)
print(d)

# matriz de 1's
e = np.ones((5,3))
print(e)

print(b.max()) # retorna o maior elemento de b
print(b.min()) # retorna o menor elemento de b
print(b.sum()) # retorna a soma dos elementos de b
print(b.mean()) # retorna a média dos elementos de b
print(b.std()) # retorna o o desvio padrão dos elementos de b
