R=1
lista_vazia = []
lista_livros = ["Como_eu_era_antes_de_voce", "As_quatro_rainhas_mortas", "O_grande_conflito"]
printe=lista_livros
print(printe)   

R=2
print(lista_livros[1:3])
print(print)
print(lista_livros[1])
print(lista_livros[-1])

R=3
lista_livros.append("e_a_biblia_tinha_rasao")
print(lista_livros)
lista_livros.append("humildade")
print(lista_livros)

R=4
lista_livros.insert(2, "duna")
print(lista_livros)

R=5
lista_livros[0] = "o_silencio_dos_inocentes"
print(lista_livros)
lista_livros.remove("o_silencio_dos_inocentes")
if "o_silencio_dos_inocentes" in lista_livros:
    print("Livro encontrado")
else:
    print("Livro nao encontrado")

R=6
lista_vazia=[]
lista_numeros=[1,2,3,2,4,2,5]
print(lista_numeros.count(2))

R=7
print(lista_livros)
for livro in lista_livros:
    print(f"o livro {livro} é interessante")

R=8
lista_vazia=[]
lista_idades=[12,18,25,14,30]
for idade in lista_idades:
    if idade >= 18:
        lista_vazia.append(idade)
print(lista_vazia)

R=9
lista_vazia=[]
lista_numeros=[10,20,30,40]
total=sum(lista_numeros)
print(total)

R=10
lista_vazia=[]
lista_medias_alunos=[[7,8,9],[6,5,7]]
matriz = [[lista_medias_alunos for i in range(1)] for j in range(1)]
print(matriz)

R=11



