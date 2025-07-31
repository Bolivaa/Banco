op = -1
deposito = 0
limite_de_saque = 3
saque_realizado = 0 


while opcao != 0:
    opcao = int(input("1 - deposito \n2 - Sacar \n3 - Extrato \n0 - Sair \n" ))

    if opcao == 1:
        valor = float(input("\n digite valor desejado para deposito: \n"))
        print(f"Deposito no valor de {valor:.2f} realizado com sucesso !")
        deposito += valor
    elif opcao == 2:
           if saque_realizado >= limite_de_saque:
                print("Você atingiu o limite de saque diario !")
                continue

           saque = float(input("\nDigite o valor para saque: "))
           
           if saque > deposito:
                print("\n❌ Saldo insuficiente ❌\n ")
           elif saque > 500:
                print("\n❌ Valor maior que o permitido ❌ \n")
                continue
           else:  
                 print(f"Saque no valor de {saque:.2f} realizado com sucesso !")   
                 saque_realizado += 1
                 deposito -= saque
    elif opcao == 3:
     
          print(f"Seu saldo é de: R${deposito:.2f} e as movimentações de saque {saque}")
    
    else:
         print("\n❌ Opção Invalida ❌ \n")