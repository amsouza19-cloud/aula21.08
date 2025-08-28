aluno = {"nome": "Angela", "idade": 40, "nota": 9.0}
print(aluno)

produto = {"nome": "òculos", "preço": 180, "estoque": 100}
print(f"Nome do produto: {produto['nome']}")
print(f"Quantidade em estoque: {produto['estoque']}")

pessoa = {"nome": "Angela", "idade": 40}
pessoa = {"cidade":"Jaboatão dos Guararapes"}
print("cidade")

carro = {"marca": " Jeep", "Modelo": "Commander Overland", "ano": 2025}
del carro ["ano"]
print(carro)
if carro["marca"] == "Jeep":
    print("É um carro da marca Jeep")

contato = {"nome": "Agela", "email": "angelasouza@email.com"}
if "telefone" in contato:
    print("A chave 'telefone' existe no dicionário.")
else:
    print("A chave 'telefone' NÃO existe no dicionário.")

def contar_frequencia(lista_palavras):
        frequencia = {}
        for palavra in lista_palavras:
                frequencia[palavra] = frequencia.get(palavra, 0) + 1
        return frequencia

palavras = ["Maria", "Joaquina", "João", "Maria", "Pedro", "José","Maria", "Joaquina"]
contagem = contar_frequencia(palavras)
print(contagem)

