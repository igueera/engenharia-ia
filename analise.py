import csv

with open("avaliacoes.csv", encoding="utf-8", newline="") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(linha["nota"], linha["categoria"])
    

