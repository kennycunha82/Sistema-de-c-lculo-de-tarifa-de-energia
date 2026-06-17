glossario = {
    "Parâmetro": "A variável definida na assinatura de uma função que espera receber um valor.",
    "Argumento": "O valor real que é passado para a função quando ela é executada.",
    "Mutável": "Uma estrutura de dados cujo conteúdo pode ser alterado após a criação (ex: listas e dicionários).",
    "Imutável": "Uma estrutura de dados que não pode ser modificada depois de criada (ex: tuplas e frozensets).",
    "Set": "Um conjunto ordenado por hash que não permite elementos duplicados e não possui índices."
}

for palavra, significado in glossario.items():
    print(f"{palavra}:")
    print(f"\t{significado}\n")