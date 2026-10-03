import csv

notas = []

with open("avaliacoes.csv", encoding="utf-8-sig", newline="") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        nota = int(linha["nota"])
        notas.append(nota)

media = sum(notas) / len(notas)
print(f"Nota média geral: {media:.2f}")
    

