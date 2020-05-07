'''trabalhinho - obs:rodando em linux fica mais bonitinho'''   
option = 0
valor_hambuerguer=0
valor_bebida=0
hamburguer=0
bebida=0
while option != '4':
    print("-=-=-=PODRÃO LANCHES=-=-=-")
    print("1)Hamburgueres")
    print("2)Bebidas")
    print("3)Valor da conta")
    print("4)Fechar pedido")
    option = input('Digite sua opção: ')
    import os
    import time
    time.sleep(2)
    os.system('clear')
    if option == '1':
        print("-=-Hamburgueres-=-")
        print("1)X-Tudo ... R$9,90")
        print("2)X-Bacon ... R$10,90")
        print("3)X-Egg ... R$11,90")
        print("4)X-SuperTudo ... R$12,90")
        hamburguer = input('Digite sua opção: ')
        print("Ok,seu pedido foi anotado!")
        time.sleep(2)
        os.system('clear')
       
    elif option == '2':
        print("-=-Bebidas-=-")
        print("1)Refri ... R$5,90")
        print("2)Suco ... R$5,90")
        print("3)Agua ... R$2,90")
        bebida = input('Digite sua opção: ')
        print("Ok,seu pedido foi anotado!")
        time.sleep(2)
        os.system('clear')
    elif option == '3':
        if hamburguer == '1':
            valor_hambuerguer = 9.90
        elif hamburguer == '2':
            valor_hambuerguer=10.90
        elif hamburguer=='3':
            valor_hambuerguer= 11.90
        elif hamburguer=='4':
            valor_hambuerguer=12.90
            
        if bebida=='1':
            valor_bebida = 5.90
        elif bebida=='2':
            valor_bebida=5.90
        elif bebida=='3':   
            valor_bebida=2.90
        valor_total = valor_bebida+valor_hambuerguer
        time.sleep(2)
        print("O valor da conta é de",valor_total,"reais")
        time.sleep(4)
        os.system('clear')
            
    elif option=='4':
        time.sleep(2)
        print("Conta fechada, muito obrigado e volte sempre! :)")
            
            
