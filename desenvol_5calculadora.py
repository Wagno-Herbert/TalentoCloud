# TalentoCloud 
 escolha = int(input("Digite o número da operação: "))
        if escolha == 0:
            print("Saindo da calculadora")
            break
        elif escolha in range(1, 5):

            
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))

          
            if escolha == 1:
                resultado = num1 + num2
            elif escolha == 2:
                resultado = num1 - num2
            elif escolha == 3:
                resultado = num1 * num2
            elif escolha == 4:
                resultado = num1 / num2 if num2 != 0 else "Erro: divisão por zero"

            print("Resultado:", resultado)
        else:
            print("Essa opção não existe. Tente novamente.")


calculadora()
