A = [[1, 2],
    [4, 5]]

B = [[5, 6],
    [7, 8]]

C = [[0, 0],
    [0, 0]]

for i in range(2):       
    for j in range(2): 
        C[i][j] = A[i][j] + B[i][j]

print("Dada a matriz A:")
for linha in A:
    print(linha)

print("E Matriz B:")
for linha in B:
    print(linha)
print("A Matriz C = (A + B) será:")
for linha in C:
    print(linha)