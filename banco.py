op = -1
deposito = 0
limite_de_saque = 3
saque_realizado = 0 
extrato = []

while op != 0:
    op = int(input("1 - deposito \n2 - Sacar \n3 - Extrato \n0 - Sair \n" ))

    if op == 1:
     valor = float(input("\n digite valor desejado para deposito: \n"))
     if valor < 0:
          print("Valor invalido para deposito !")
     else:
        print(f"Deposito no valor de {valor:.2f} realizado com sucesso !")
        deposito += valor
    elif op == 2:
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
                 print(f"Saque no valor de {saque:.2f} realizado com sucesso!")   
                 extrato.append(f"saque: {saque:.2f}")
                 saque_realizado += 1
                 deposito -= saque
    elif op == 3:
          if extrato:
               for item in extrato:
                    print(item)
               print(f"Seu saldo é de: R${deposito:.2f} e as movimentações:{extrato}")
          else:          
           print(f"Sem Transações realiz")
          



    elif op == 0:
         print("Operação finalizada !!!")
         
    else:
         print("\n❌ Opção Invalida ❌ \n")