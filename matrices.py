v = [0]*8
print(v) # matrix de 1*8 - 1 fila por 8 columnas 

# m = [[0]*8]*8 # matris de 8 por 8
# print(m)

m = [] # lista vacia 
for i in range(8): # ocho filas 
    m.append([]) #agregando lista vacias ala lita 
    for j in range(8): # el numero de columnas 
        m[i].append(i*8+j)

print(m)
print(m[2][4]) # m es la "matrix" y busca la fila, columna 4
