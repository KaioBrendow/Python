from datetime import datetime
#import pytz
#timezone = pytz.timezone('America/Sao_Paulo')
menu = """

    ### Menu ###
    1 - Deposito
    2 - Saque
    3 - Extrato
    4 - Criar Usuario
    5 - 
    0 - Sair

=> """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
lista = []

def deposito(saldo, valor, extrato):
    
    if float(valor) > 0.0:
        #fuso = timezone('America/Sao_Paulo')
        data_hora = datetime.now()#.astimezone(timezone)
        extrato= ""+str(data_hora.strftime(f'%d/%m/%Y %H:%M'))+" Deposito de R$ "+ str(valor)+"\n    "
        saldo+= float(valor)
        return saldo , extrato
    else:
        return False
        
def saque(saldo, valor, extrato, numero_saques, limite_saques):
    
    if float(valor) > 0.0:
        if int(numero_saques) < limite_saques:
            if float(saldo)>= float(valor):
                if float(valor) <=limite:
                    #fuso = timezone('America/Sao_Paulo')
                    data_hora = datetime.now()#.astimezone(timezone)
                    extrato+= ""+str(data_hora.strftime(f'%d/%m/%Y %H:%M'))+" Saque    de R$ "+ str(valor)+"\n    "
                    saldo-= float(valor)
                    numero_saques += 1
                    return saldo, extrato, numero_saques
                else:
                    return 501# retorno nao saca acima de 500 reais
                        
            else:
                    return -1 # saldo insuficiente
        elif numero_saques >= limite_saques:
                    return 4 #Limite de saque diario
    else:
            return 2

def extrato_bancario(saldo , extrato):
    extra = f"""
    Saldo:  {saldo:10.2f}

        Extrato
    {extrato}
    """
    return extra

def cria_usuario(nome, data_nasc, cpf, endereco):
    cliente = {cpf: {"nome": nome, "nascimento": data_nasc, "endereco": endereco}}
    return cliente      

def verifica_cpf(cpf, cliente):
     print(cliente)
     for clientes in cliente:
          print(clientes+" CPF entregue"+cpf)
     return True

while True:

    opcao = input(menu)

    if(opcao == "1"):
        valor = float(input("""
        Deposito
    Informe o valor do deposito:
=> """))
        resp_depo = deposito(saldo, valor, extrato)
        if resp_depo == False:
            print("""
        Deposito falhou!
    Não é possivel fazer deposito desse valor.

    Voltando ao menu principal!""")
        else:
            saldo = resp_depo[0]
            extrato += resp_depo[1]
            print("""
        Deposito Feito!
    
    Voltando ao menu principal!""")
    elif opcao == "2":
        saque_entrada = float(input(f"""
    Saldo:  {saldo:10.2f}

        Saque

    Informe o valor do Saque:

=> """))
        
        resp_saque= saque(saldo= saldo, valor= saque_entrada, extrato= extrato, numero_saques= numero_saques, limite_saques= LIMITE_SAQUES )

        if resp_saque == 501:
            print("""
        Não é possivel sacar acima de 500 reais!
                          
    Voltando ao menu principal!
""")
        elif resp_saque == -1:
             print("""
        Saldo insuficiente!
    Não foi possivel fazer saque desse valor.

    Voltando ao menu principal!""")
        elif resp_saque == 4:
            print("""
        Limite de 3 saques diarios alcançado!
                          
    Voltando ao menu principal!
""")
        elif resp_saque == 2:
            print("""
        Valor invalido!
        
    Voltando ao menu principal!
""")
        else:
            saldo = resp_saque[0]
            extrato = resp_saque[1]
            numero_saques = resp_saque[2]
            print("""
        Saque efetuado!
        
    Voltando ao menu principal!
""")
    elif opcao == "3":
        
        resp_extra = extrato_bancario(saldo , extrato)
        print (resp_extra)
    elif opcao == "0":
        break
    elif opcao == "4":
         nome = input("""
        Cadastro de Usuario...
    Informe o nome completo do usuario:
=> """)
         nascimento = input(f"""
        Cadastro de Usuario...
    Informe data de nascimento do {nome}:
=> """)
         cpf = input(f"""
        Cadastro de Usuario...
    Informe CPF do {nome}(somente números):
=> """)
         valida = verifica_cpf(cpf, lista)
         if valida == False:
                print(f"""
        Cadastro de Usuario...
        
    CPF já cadastrado.
            
        Operação cancelada!
=> """)
                #break
         else:
            endereco = input(f"""
        Cadastro de Usuario...
        Endereço:
    Informe logradouro:
=> """)
            endereco + ", "+ input(f"""
        Cadastro de Usuario...
        Endereço:
    Informe número:
=> """)
            endereco + " - "+ input(f"""
        Cadastro de Usuario...
        Endereço:
    Informe Bairro:
=> """)
            endereco + " - "+ input(f"""
        Cadastro de Usuario...
        Endereço:
    Informe Cidade:
=> """)
            endereco + "/"+ input(f"""
        Cadastro de Usuario...
        Endereço:
    Informe Estado:
=> """)
            lista.append(cria_usuario(nome= nome, data_nasc= nascimento, cpf=cpf, endereco= endereco))
    else:
        print("Operação inválida, por favor selecione novamente a operação desejava.")