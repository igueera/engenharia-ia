import csv

def carregar(caminho):
    avaliacoes = []
    with open(caminho, encoding="utf-8-sig", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        for numero, linha in enumerate(leitor, start=2):
            try:
                linha["nota"] = int(linha["nota"])
            except ValueError:
                print(f"Aviso: linha {numero} ignorada, nota inválida: {linha['nota']!r}")
                continue
            avaliacoes.append(linha)
    return avaliacoes


def calcular_media(notas):
    return sum(notas) / len(notas)

def agrupar_por_categoria(avaliacoes):
    por_categoria = {}
    for linha in avaliacoes:
        categoria = linha["categoria"]
        if categoria not in por_categoria:
            por_categoria[categoria] = []
        por_categoria[categoria].append(linha["nota"])
    return por_categoria

def filtrar_baixas(avaliacoes):
    baixas = []
    for linha in avaliacoes:
        if linha["nota"] <= 2:
            baixas.append(linha)
    return baixas

def main():
    avaliacoes = carregar("avaliacoes.csv")
    if not avaliacoes:
        print("Nenhuma avaliação válida encontrada.")
        return

    notas = []
    for linha in avaliacoes:
        notas.append(linha["nota"])
    print(f"Nota média geral: {calcular_media(notas):.2f}")

    print("Nota média por categoria:")
    for categoria, lista in agrupar_por_categoria(avaliacoes).items():
        print(f"  {categoria}: {calcular_media(lista):.2f}")

    print("Respostas com nota menor ou igual a 2:")
    for linha in filtrar_baixas(avaliacoes):
        print(f"  [{linha['nota']}] {linha['resposta']}")

main()