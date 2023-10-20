from destinatario import Destinatario
from gerenciador_de_email import GerenciadorDeEmail

gerenciador_email = GerenciadorDeEmail('Empresa', 'empresa@email.com.br')

while True:
    titulo = input('Defina o Titulo do Email: ')
    mensagem = input('Defina o assunto: ')
    print()

    gerenciador_email.criar_email(titulo, mensagem)

    command = 's'
    while command == 's':
        nome = input('Defina o nome do destinatário: ')
        email = input('Defina o email do destinatário: ')
        destinatario = Destinatario(nome, email)
        gerenciador_email.adicionar_destinatario(destinatario)
        print()

        command = input('Deseja adicionar outro destinatário?[s/n]: ')

    gerenciador_email.enviar_email()
    print()
