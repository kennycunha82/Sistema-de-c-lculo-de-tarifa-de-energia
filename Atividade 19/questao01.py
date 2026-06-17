matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
for linha in matriz:
    print(linha)

k = int(input("Digite o valor de para multiplicar com a diagonal da matriz: "))
for i in range(3):
    for j in range(3):
        if i == j:
            matriz[i][j] *= k
print(f"A matriz com a diagonal multiplicada por {k} é ")
for linha in matriz:
    print(linha)