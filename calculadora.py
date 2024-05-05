class Main:

    class Numeros:
        def __init__(self, num1, num2, operacao, resultado=None):
            self.num1 = num1
            self.num2 = num2
            self.operacao = operacao
            self.resultado = resultado

    class Calculando:        
        def adc(self, num1, num2, resultado=None):
            return num1 + num2
            
        def sub(self, num1, num2, resultado=None):
            return num1 - num2
            
        def mul(self, num1, num2, resultado=None):
            return num1 * num2
            
        def div(self, num1, num2, resultado=None):
            if num2 == 0:
                raise ValueError("Divisão por zero não é permitida! Tente novamente.")
            else:
                return num1 / num2

    class Interacao:
        def pergunta(self, resultado=None):
            num1 = resultado if resultado is not None else float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
            operacao = input("Digite a palavra da operação que você deseja realizar:\nAdc é (+), Sub é (-), Mul é (*), Div é (/) >> ").lower()
            return num1, num2, operacao
    
    class Exibir:
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

    def executar_calculadora(self):
        exibir = self.Exibir()
        exibir.mostrar_boas_vindas()
        interacao = self.Interacao()
        calculadora = self.Calculando()
        
        resultado = None
        while True:
            num1, num2, operacao = interacao.pergunta(resultado)
            try:
                if operacao == 'adc':
                    resultado = calculadora.adc(num1, num2)
                elif operacao == 'sub':
                    resultado = calculadora.sub(num1, num2)
                elif operacao == 'mul':
                    resultado = calculadora.mul(num1, num2)
                elif operacao == 'div':
                    resultado = calculadora.div(num1, num2)
                else:
                    exibir.mostrar_operacao_invalida()
                    continue
            except ValueError as e:
                print(f"Erro: {e}")
                continue
            
            exibir.mostrar_resultado(resultado)
            if not exibir.continuar_calculando():
                print("Calculadora encerrada!")
                break

Main().executar_calculadora()