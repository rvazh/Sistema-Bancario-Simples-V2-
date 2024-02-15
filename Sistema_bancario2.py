import textwrap

# O "\t" da um Tab para deixar certinho 

def  Menu(): 

    menu = """
    ===========================================================
            ========== Bem-vindo ao Dubank ==========

    [1] Depósitar       [5] Criar conta corrente
    [2] Sacar           [6] Listar contas
    [3] Ver extrato     [7] Sair
    [4] Criar usúario

    => """

    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR${valor:.2f}\n"
        print("\n== Depósito realizado com sucesso ")
    else:
        print("$$$ Operação falhou, o formato do valor é inválido $$$")
    
    return saldo, valor, extrato

def saque(*, saldo, saques_feitos, saques_diarios, limite_de_saque_por_vez, extrato, valor ):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite_de_saque_por_vez
    excedeu_saques = saques_feitos >= saques_diarios
    

    if excedeu_saldo:
        print("Operação falhou, você não tem saldo para essa ação.")

    elif excedeu_limite:
        print(f"Operação falhou, o valor de saque é maior do que o seu saldo \nesse é o seu saldo: {saldo}")

    elif excedeu_saques:
        print("Operação falhou, você atingiu o seu limite de saques diarios, volte amanhã.")

    elif valor > 0:
        saldo -= valor
        saques_feitos += 1

        extrato += f"Saque:\t\t R${valor:.2f} \n"

        print(f"Saque feito com sucesso!")
    else:
        print("/n$$$ Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):

    print("================== Extrato ====================")
    print("Não foram realizadas movimentações" if not extrato else extrato) # Aqui será exibido a mensagem se a variavel extrato estiver vazia, mas se não ele irá mostrar oque tem dentro da variavel
    print("")
    print(f"Saldo:\t\t R${saldo:.2f}")
    print("===============================================")

def criar_usuario(usuarios):
     
    cpf = input("Informe o seu CPF (Somente números): ")  
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print(" Já existe um usuário criado com esse CPF.")


    nome = input("Infome o seu nome: ")
    data_de_nascimento = input("Informe a sua data de nascimento (dd-mm-aa): ")
    endereco = input("Informe o seu endereço (logradouro, número - bairro - cidade/sigla estado): ")

    usuarios.append({"Nome": nome, "Data de nascimento": data_de_nascimento, "cpf": cpf, "Endereço": endereco})
    
    print(f"Usuário criado com sucesso!\n\n\n {usuarios}")

def filtrar_usuarios(cpf, usuarios):   

      usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
      return usuarios_filtrados[0] if usuarios_filtrados else None
      
def criar_conta(agencia, numero_conta, usuarios):

    cpf = input("Informe o seu CPF:  ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "Numero conta": numero_conta, "Usuario": usuario}
    
    print("\nUsuario não encontrado.")

def listar_contas(contas) :

    for conta in contas:
        linha = f"""
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['Numero conta']}
            Titular:\t{conta['Usuario']['Nome']}
        """

        print("=" * 100)
        print(textwrap.dedent(linha))
  
def main(opcao):
    AGENCIA = "0001"
    saques_diarios = 3

    saldo = 0
    deposito = 0
    saques_feitos = 0
    extrato = ""
    limite_de_saque_por_vez = 500 
    usuarios = []  
    contas = []


    while True:
    
        opcao = Menu()

        if opcao == "1":
            valor = float(input("Quanto deseja depósitar?: "))

            saldo, valor, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "2":
            valor = float(input("Quanto deseja sacar?: "))

            saldo, extrato = saque(
                saldo = saldo, 
                valor = valor,
                saques_feitos=saques_feitos,    
                saques_diarios=saques_diarios, 
                limite_de_saque_por_vez = limite_de_saque_por_vez,      
                extrato=extrato,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
    
        elif opcao == "4":
            criar_usuario (usuarios)

        elif opcao == "5" : 

            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "7":
            print("Obrigado por utilizar o serviço do Dubank, tenha uma ótima semana! ")
            break
        else:
            print("Operação falhou, a opção escolhida não é existente no sistema, escolha alguma em exibição \npor favor!") 


main(Menu)




