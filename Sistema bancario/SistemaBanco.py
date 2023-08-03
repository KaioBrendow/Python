from datetime import datetime
#import pytz
#timezone = pytz.timezone('America/Sao_Paulo')
menu = """

    ### Menu ###
    1 - Deposito
    2 - Saque
    3 - Extrato
    0 - Sair

=> """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if(opcao == "1"):
        deposito = float(input("""
        Deposito
    Informe o valor do deposito:
=> """))
        if float(deposito) > 0.0:
            #fuso = timezone('America/Sao_Paulo')
            data_hora = datetime.now()#.astimezone(timezone)
            extrato+= ""+str(data_hora.strftime(f'%d/%m/%Y %H:%M'))+" Deposito de R$ "+ str(deposito)+"\n    "
            saldo+= float(deposito)
        else:
            print("""
        Deposito falhou!
    Não é possivel fazer deposito desse valor.

    Voltando ao menu principal!""")

    elif opcao == "2":
        saque = float(input(f"""
    Saldo:  {saldo:10.2f}

        Saque

    Informe o valor do Saque:

=> """))
        if float(saque) > 0.0:
            if int(numero_saques) <= LIMITE_SAQUES:
                if float(saldo)>= float(saque):
                    if float(saque) <=limite:
                        #fuso = timezone('America/Sao_Paulo')
                        data_hora = datetime.now()#.astimezone(timezone)
                        extrato+= ""+str(data_hora.strftime(f'%d/%m/%Y %H:%M'))+" Saque    de R$ "+ str(saque)+"\n    "
                        saldo-= float(saque)
                        numero_saques += 1
                    else:
                        print("""
        Não é possivel sacar acima de 500 reais!
                          
    Voltando ao menu principal!
""")
                        
                else:
                    print("""
        Saldo insuficiente!
    Não foi possivel fazer saque desse valor.

    Voltando ao menu principal!""")
            elif numero_saques > LIMITE_SAQUES:
                    print("""
        Limite de 3 saques diarios alcançado!
                          
    Voltando ao menu principal!
""")
        else:
            print("""
        Valor invalido!
        
    Voltando ao menu principal!
""")
        
    elif opcao == "3":
        print(f"""
    Saldo:  {saldo:10.2f}

        Extrato
    {extrato}
    """)
    elif opcao == "0":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejava.")