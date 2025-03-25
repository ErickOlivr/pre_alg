#infolivros
mensagem_inicial = '''Olá, bem vindo ao info livros escolha quais desses livros vocÇe quer saber mais sobre:
(senhor dos anéis, harry potter, it a coisa)
'''

pergunta = """Qual livro você quer saber mais sobre?(Escreva corretamente)"""

livros ={
"senhor dos anéis" : '''Título: O Senhor dos Anéis
Autor: J.R.R. Tolkien
Ano de Publicação: 1954
Número de Páginas: 1178
''',
"harry potter": '''Título: Harry Potter
Autor: J.K. Rowling
Ano de Publicação: 1997
Número de Páginas: 223
''',
"it a coisa": '''Título: It
Autor: Stephen King
Ano de Publicação: 1986
Número de Páginas: 1138
'''
}

print(mensagem_inicial)

while True:
    while True:
      livro = input(pergunta).strip().lower()
      if livro in livros:
          print(livros[livro])
          break
      else:
          print("livro não encontrado, informe um livro válido")

    continuar = input("Deseja continuar? (s/n)").strip().lower()
    if continuar != "s":
        print("obrigado por usar o programa")
        break