from model import RepositorioDeLivros

repositorioDeLivros = RepositorioDeLivros()

while (True):
    escolha = input('1 - Cadastrar livro / 2 - listar livros: ')
    if (escolha == '1'):
        titulo = input('Defina o Titulo: ')
        autor = input('Defina o autor: ')
        ano = input('Defina o ano: ')
        repositorioDeLivros.registrar_livros(titulo, autor, ano)
    
    if (escolha == '2'):
        repositorioDeLivros.listar_livros()
        

