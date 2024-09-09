# Sistema de banco simples - Pedro Ivo - 05/09/24 - XX/09/24
import curses
import datetime
import sys

# TODO: APÓS TERMINAR SISTEMA FAZER INTERFACE COM CURSES

# Valores do cliente são salvos aqui:
DADOS = {
    'novo_nome': None,
    'novo_nascimento': None,
    'novo_cpf': None,
    'novo_rg': None,
    'novo_senha': None
    }

def extrato():
    print("extrato")
    pass

def encerrar_conta():
    print("encerrar")
    pass
    
def deposito():
    print("deposito")
    pass

def saque():
    print("saque")
    pass

def transferencia():
    print("transf")
    pass

def saldo():
    print("saldo")
    pass
    
def menu():
    print("""    SISTEMA BANCARIO - Menu
    Escolha as opções:
        
        1) Ver saldo
        2) Fazer depósito
        3) Fazer saque
        4) Extrato da conta
        5) Encerrar conta
        6) Sair""")
        
    while True:
        ch = input("> ")

        if ch == '1':
            saldo()
        elif ch == '2':
            deposito()
        elif ch == '3':
            saque()
        elif ch == '4':
            extrato()   
        elif ch == '5':
            encerrar_conta()
        elif ch == '6':
            print("\nSaindo.")
            sys.exit()
        else:
            print("\nTente novamente.")
    
def criar_conta():
    print("    SISTEMA BANCARIO - Criar conta")
    date = datetime.date.today()
    ano = date.strftime("%Y")   
    
    while True:
        # NOME
        DADOS['novo_nome'] = input("Insira seu nome completo: ") 
        # Se não é string -> erro
        if DADOS['novo_nome'].isdecimal():
            print("Use apenas caracteres.")
            continue # Volta pro campo, não pro inicio do loop
        # Se tem menos de 3 caracteres -> erro
        if len(DADOS['novo_nome']) < 3:
            print("Nome muito curto.")
            continue
        
        # ANO
        DADOS['novo_nascimento'] = input("Insira o ano do seu nascimento: ")
        # Se possui caracteres -> erro
        if not DADOS['novo_nascimento'].isdecimal():
            print("Use apenas números.")
            continue
        # Se o ano tem menos de 4 caracteres -> erro
        if len(DADOS['novo_nascimento']) != 4:
            print("Ano escrito de forma errada.")
            continue
        # Se tem menos de 18 anos -> erro
        if int(ano) - int(DADOS['novo_nascimento']) < 18: 
            print("Você precisa ter 18 anos para criar uma conta.")
            continue
            
        # CPF
        DADOS['novo_cpf'] = input("Insira seu CPF (somente números): ")
        # Se possui caracteres  -> erro
        if not DADOS['novo_cpf'].isdecimal():
            print("Use apenas números.")
            continue
        # Se o cpf tem menos de 11 caracteres -> erro
        if len(DADOS['novo_cpf']) != 11:
            print("CPF muito curto.")
            continue
            
        # RG
        DADOS['novo_rg'] = input("Insira seu RG (somente números): ") 
        # Se possui caracteres  -> erro
        if not DADOS['novo_rg'].isdecimal():
            print("Use apenas números.")
            continue
        # Se o rg tem menos de 9 caracteres -> erro
        if len(DADOS['novo_rg']) != 9:
            print("RG muito curto.")
            continue
            
        # SENHA
        DADOS['novo_senha'] = input("Crie uma senha: ")  
        # Se a senha tem menos de 4 caracteres -> erro
        if len(DADOS['novo_senha']) < 4:
            print("Senha muito curta.")
            continue
        
        print("Conta criada com sucesso!")
        entrar_conta()
    
def entrar_conta():
    print("    SISTEMA BANCARIO - Entrar na conta")
    
    while True:
        cpf = input("CPF: ")
        senha = input("Senha: ")
        
        if cpf == DADOS['novo_cpf'] and senha == DADOS['novo_senha']:
            print("Entrou na conta com sucesso!")
            menu()
        else:
            print("Credenciais erradas. Tente novamente.")

def main():
    print("""    SISTEMA BANCARIO 
    Escolha as opções:
        
        1) Criar conta
        2) Entrar na conta
        3) Sair""")
        
    while True:
        ch = input("\n  > ")
        
        if ch == '1':
            criar_conta()
        elif ch == '2':
            entrar_conta()
        elif ch == '3':
            print("\nSaindo...")
            sys.exit()
        else:
            print("\nOpção inválida.")
        
if __name__ == "__main__": 
    main()
