import csv

notas = []
por_categoria = {}
baixas = []

with open("avaliacoes.csv", encoding="utf-8-sig", newline="") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        nota = int(linha["nota"])
        categoria = linha["categoria"]
        notas.append(nota)

        if categoria not in por_categoria:
            por_categoria[categoria] = []
        por_categoria[categoria].append(nota)

        if nota <= 2:
            baixas.append(linha)



media = sum(notas) / len(notas)
print(f"Nota média geral: {media:.2f}")
print("Nota média por categoria:")

for categoria, lista in por_categoria.items():
    media_categoria = sum(lista) / len(lista)
    print(f"{categoria}: {media_categoria: .2f}")
    
print("Respostas com nota menor ou igual a 2:")
for linha in baixas:
    print(f"  [{linha['nota']}] {linha['resposta']}")
