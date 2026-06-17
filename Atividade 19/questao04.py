matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
for linha in matriz:
    print(linha)

lista = []
for i in range(3):
    soma = 0
    for j in range(3):
        soma += matriz[i][j]
    lista.append(soma)
    print(f"A soma da linha {i+1} é {soma}")

print(f"A maior soma é {max(lista)} que se encontra na linha {i+1}:")
print(f"Linha : {matriz[i]}")