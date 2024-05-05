class Calculadora:
        #Classe de definição das operações.        
        def adc(self, num1, num2, resultado=None):
            return num1 + num2
            
        def sub(self, num1, num2, resultado=None):
            return num1 - num2
            
        def mul(self, num1, num2, resultado=None):
            return num1 * num2
            
        def div(self, num1, num2, resultado=None):
            return num1 / num2
            
class Exibir:
        #Classe de exibições na tela do usuário.
        def mostrar_boas_vindas(self):
            print(30 * "#")
            print("Seja bem-vindo a nossa calculadora!\nVamos começar!")

        def mostrar_resultado(self, resultado):
            print(f"O resultado da operação é {resultado}.")
            print(30 * "#")

        def mostrar_operacao_invalida(self):
            print("Operação inválida. Por favor, digite uma operação válida.")

        def continuar_calculando(self):
            return input("Deseja continuar calculando com o resultado? (s/n)").lower()
        
        def pergunta(self, resultado=None):
            while True:
                num1 = resultado if resultado is not None else input("Digite o primeiro valor: ")
                num2 = input("Digite o segundo valor: ")

                try:
                    num1 = float(num1)
                    num2 = float(num2)
                    if resultado is not None:
                        resultado = float(resultado)
                    if num2 == 0:
                        raise ValueError("Divisão por zero não é permitida! Tente novamente.")
                except ValueError:
                    print("O valor digitado é incorreto! Tente novamente utilizando apenas números.")
                    continue

                operacao = input("Digite a palavra da operação que você deseja realizar:\nAdc é (+), Sub é (-), Mul é (*), Div é (/) >> ").lower()
                if operacao not in ['adc', 'sub', 'mul', 'div']:
                    print("Operação inválida! Digite o opção corretamente.")
                    continue
                else:
                    return num1, num2, operacao
class Main:
    #Instanciando as classes Calculadora e Exibir dentro de uma função para rodar tods os camandos.
    def executar_calculadora(self):
        exibir = Exibir()
        exibir.mostrar_boas_vindas()
        calculadora = Calculadora()
        
        resultado = None
        while True:
            num1, num2, operacao = exibir.pergunta(resultado)
            try:
                if operacao == 'adc':
                    resultado = calculadora.adc(num1, num2)
                elif operacao == 'sub':
                    resultado = calculadora.sub(num1, num2)
                elif operacao == 'mul':
                    resultado = calculadora.mul(num1, num2)
                elif operacao == 'div':
                    resultado = calculadora.div(num1, num2)
            except ValueError as e:
                print(f"Erro: {e}")
                continue
            
            exibir.mostrar_resultado(resultado)
            if 'n' in exibir.continuar_calculando():
                print("Calculadora encerrada!")
                break

Main().executar_calculadora()