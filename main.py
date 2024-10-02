# Sistema de banco simples - Pedro Ivo - 05/09/24 - 01/10/24 
import curses
import datetime
import sys
import pickle
import os

# Menu de seleção com as teclas do teclado
def menu_selection(screen, text, options):
    curses.echo()
    curses.curs_set(0)
    selected_option = 0

    while True:
        screen.clear()
        screen.addstr(text)

        # Percorre cada opção e a exibe, destacando a opção selecionada
        for x, option in enumerate(options):
            if x == selected_option:
                # Se esta for a opção selecionada a exibe com destaque (curses.A_REVERSE)
                screen.addstr(x + 2, 0, f"> {option}", curses.A_REVERSE)
            else:
                # Se não, exibe a opção normalmente
                screen.addstr(x + 2, 0, f"  {option}")
        screen.refresh()

        key = screen.getch()

        # Navegação do menu
        if key == curses.KEY_UP and selected_option > 0:
            selected_option -= 1
        elif key == curses.KEY_DOWN and selected_option < len(options) - 1:
            selected_option += 1
        elif key == ord('\n'):
            # Se a tecla pressionada for 'Enter', retorna o índice da opção selecionada
            return selected_option

# Ver o extrato da conta - historico de saques e depositos
def extrato(screen):
    curses.curs_set(0)
    screen.addstr("\n" + DADOS['extrato'])
    screen.addstr("\nPressione qualquer tecla para voltar ao menu.")
    screen.refresh()
    screen.getch()
    menu_conta(screen)

# Apagar os dados da conta salva em 'dados.p'
def encerrar_conta(screen):
    curses.echo()
    curses.curs_set(0)
    
    # Menu - espaço depois da opções para ficar mais bonitinho quando é selecionado
    options = ["Sim ", "Não "]
    escolha = menu_selection(screen, "Tem certeza que deseja deletar sua conta?", options)

    if escolha == 0:
        os.remove("dados.p")
        screen.addstr("\nConta deletada. Voltando para o menu inicial.")
        screen.refresh()
        screen.getch()
        menu(screen)
    elif escolha == 1:
        menu_conta(screen)

# Adicionar dinheiro ao saldo
def deposito(screen):
    curses.echo()
    curses.curs_set(0)
    data = date.strftime("%d/%m/%Y")

    while True:
        screen.addstr("\nInsira a quantidade que será depositado na conta:")
        screen.refresh()
        try:
            curses.curs_set(1)
            screen.addstr("\n> ")
            valor = float(screen.getstr().decode('utf-8').strip())
            screen.refresh()
            curses.curs_set(0)
            
            if valor >= 0:
                screen.addstr(f"R$ {valor} foram depositados a sua conta.")
                DADOS['saldo'] += valor
                DADOS['extrato'] += (f"Deposito de R$ {valor} em {data}\n")
                # Salva os dados no arquivo
                with open('dados.p', 'wb') as f:
                    pickle.dump(DADOS, f)
                screen.refresh()
                screen.getch()
                menu_conta(screen)
            # Não vou fazer um else pois se o usuário quiser sair da tela ele pode
            # depositar R$ 0.
        except ValueError:
            screen.addstr("Insira apenas numeros.")
            continue

# Retirar dinheiro do saldo
def saque(screen):
    curses.echo()
    curses.curs_set(0)
    data = date.strftime("%d/%m/%Y")
    
    while True:
        screen.addstr("\nInsira a quantidade que será sacado da conta:")
        screen.refresh()
        try:
            curses.curs_set(1)
            screen.addstr("\n> ")
            valor = float(screen.getstr().decode('utf-8').strip())
            screen.refresh()
            curses.curs_set(0)
            
            if valor <= DADOS['saldo']:
                screen.addstr(f"R$ {valor} foram sacados da sua conta.")
                DADOS['saldo'] -= valor
                DADOS['extrato'] += (f"Saque de R$ {valor} em {data}\n")
                # Salva os dados no arquivo
                with open('dados.p', 'wb') as f:
                    pickle.dump(DADOS, f)
                screen.refresh()
                screen.getch()
                menu_conta(screen)
            else:
                screen.addstr("Você não tem saldo suficiente.")
                screen.refresh()
                screen.getch()
                menu_conta(screen)
        except ValueError:
            screen.addstr("Insira apenas numeros.")
            continue

# Visualizar o saldo atual
def saldo(screen):
    curses.curs_set(0)
    screen.addstr(f"\nSaldo da conta: R$ {DADOS['saldo']}")
    screen.addstr("\nPressione qualquer tecla para voltar ao menu.")
    screen.refresh()
    screen.getch()
    menu_conta(screen)

# Menu da conta do usuário 
def menu_conta(screen):
    screen.clear()
    curses.echo()
    curses.curs_set(0)

    # Cria as opções do menu
    options = ["Ver saldo ", "Fazer depósito ", "Fazer saque ", "Extrato da conta ", "Encerrar conta ", "Sair "]
    escolha = menu_selection(screen, "SISTEMA BANCÁRIO - Menu da Conta", options)

    if escolha == 0:
        saldo(screen)
    elif escolha == 1:
        deposito(screen)
    elif escolha == 2:
        saque(screen)
    elif escolha == 3:
        extrato(screen)
    elif escolha == 4:
        encerrar_conta(screen)
    elif escolha == 5:
        curses.endwin()
        sys.exit()

# Função para entrar na conta salva em 'dados.p'
def entrar_conta(screen):
    screen.clear()
    curses.echo()
    curses.curs_set(0)

    while True:
        screen.clear()
        screen.addstr("SISTEMA BANCÁRIO - Entrar na Conta\n")
        screen.refresh()
        curses.curs_set(1)
        
        screen.addstr("CPF: ")
        cpf = screen.getstr().decode('utf-8').strip()
        
        screen.addstr("Senha: ")
        curses.noecho()  # Para ocultar o que o usuario digita
        senha = screen.getstr().decode('utf-8').strip()
        curses.echo()

        if cpf == DADOS['novo_cpf'] and senha == DADOS['novo_senha']:
            menu_conta(screen)
            break
        else:
            screen.addstr("\nCredenciais incorretas. Pressione qualquer tecla para tentar novamente.")
            screen.getch()

# Criar uma conta nova e depois salvá-la
def criar_conta(screen):
    screen.clear()
    curses.echo()
    curses.curs_set(0)
    ano = date.strftime("%Y") 

    while True:
        screen.addstr("SISTEMA BANCÁRIO - Criar Conta\n")
        curses.curs_set(1)
        screen.refresh()
        
        # Entrada de nome - varios while true para caso o usuario cometa um erro ele não
        # tenha que preencher os dados desde o inicio
        while True:
            screen.clear()
            screen.addstr("Insira seu nome completo: ")
            DADOS['novo_nome'] = screen.getstr().decode('utf-8').strip()

            if DADOS['novo_nome'].isdecimal() or len(DADOS['novo_nome']) < 3:
                screen.addstr("Nome inválido. Pressione qualquer tecla para tentar novamente.")
                screen.getch()
                continue
            break
        
        # Entrada do ano de nascimento
        while True:
            screen.clear()
            screen.addstr("Insira o ano do seu nascimento: ")
            DADOS['novo_nascimento'] = screen.getstr().decode('utf-8').strip()

            if not DADOS['novo_nascimento'].isdecimal() or len(DADOS['novo_nascimento']) != 4 or int(ano) - int(DADOS['novo_nascimento']) < 18:
                screen.addstr("Ano inválido ou menor de idade. Pressione qualquer tecla para tentar novamente.")
                screen.getch()
                continue
            break
        
        # Entrada do CPF
        while True:
            screen.clear()
            screen.addstr("Insira seu CPF (somente números): ")
            DADOS['novo_cpf'] = screen.getstr().decode('utf-8').strip()

            if not DADOS['novo_cpf'].isdecimal() or len(DADOS['novo_cpf']) != 11:
                screen.addstr("CPF inválido. Pressione qualquer tecla para tentar novamente.")
                screen.getch()
                continue
            break
        
        # Entrada do RG
        while True:
            screen.clear()
            screen.addstr("Insira seu RG (somente números): ")
            DADOS['novo_rg'] = screen.getstr().decode('utf-8').strip()

            if not DADOS['novo_rg'].isdecimal() or len(DADOS['novo_rg']) != 9:
                screen.addstr("RG inválido. Pressione qualquer tecla para tentar novamente.")
                screen.getch()
                continue
            break
        
        # Entrada da senha
        while True:
            screen.clear()
            screen.addstr("Crie uma senha: ")
            DADOS['novo_senha'] = screen.getstr().decode('utf-8').strip()

            if len(DADOS['novo_senha']) < 4:
                screen.addstr("Senha curta demais. Pressione qualquer tecla para tentar novamente.")
                screen.getch()
                continue
            break

        # Salva os dados em um arquivo
        with open('dados.p', 'wb') as f:
            pickle.dump(DADOS, f)
        
        screen.addstr("\nConta criada com sucesso! Pressione qualquer tecla para continuar.")
        screen.getch()
        menu(screen)

# Menu inicial
def menu(screen):
    # Cria as opções do menu
    curses.curs_set(0)
    options = ["Criar Conta ", "Entrar na Conta ", "Sair "]
    escolha = menu_selection(screen, "SISTEMA BANCARIO\n", options)
    
    if escolha == 0:
        criar_conta(screen)
    elif escolha == 1:
        entrar_conta(screen)
    elif escolha == 2:
        curses.endwin()
        sys.exit()

# Inicializa o curses e o programa
def main(screen):
    # Configuração inicial do curses
    curses.curs_set(0)  # Esconde o cursor
    screen.clear()  # Limpa a tela

    # Exibe a tela principal com opções para o usuário
    menu(screen)

if __name__ == "__main__":
    # Verifica se o arquivo de dados existe e carrega os dados, se não
    # os cria e armazena em um arquivo
    if not os.path.exists('dados.p'):
        DADOS = {
            'novo_nome': None,
            'novo_nascimento': None,
            'novo_cpf': None,
            'novo_rg': None,
            'novo_senha': None,
            'saldo': 0.00,
            'limite': 100.00,
            'extrato': ""
        }
        with open('dados.p', 'wb') as f:
            pickle.dump(DADOS, f)
    else:
        # Carrega os dados salvos no arquivo 'dados.p'
        with open('dados.p', 'rb') as f:
            DADOS = pickle.load(f)
    # Pega a data de hoje
    date = datetime.date.today()
    curses.wrapper(main) # Inicializa e finaliza o curses de forma mais eficiente
