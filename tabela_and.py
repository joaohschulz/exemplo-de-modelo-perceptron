## Esse aqui é um exemplo usando a tabela and inteira em "resultados_esperados"
## aqui o x1, x2 e o alvo já estão definidos ou seja, o codigo vai rodar as epocas na tabela and
## e assim buscando todos os resultados possíveis
## rodando as epocas a partir das linhas
## primeira linha --- x1 = 0,  x2 = 0,  alvo = 0
## segunda linha --- x1 = 1,  x2 = 0,  alvo = 0
## terceira linha --- x1 = 0,  x2 = 1,  alvo = 0
## quarta linha --- x1 = 1,  x2 = 1,  alvo = 1


from colorama import Fore, Style
import time
# Tabela verdade AND -- resultados esperados do codigo


resultados_esperados = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 1]

    # não usado diretamente no código, ta aqui apenas pra saber como é a tabela and na sequencia abaixo
    # x1 | x2 | alvo
]


# pesos
w1 = 0
w2 = 0

# learning rate
lr = 0.1

# quantidade de épocas

epocas = 5


# função de ativação
def ativacao(resultado):
    if resultado >= 2:
        return 1
    else:
        return 0


# treinamento do perceptron
for epoca in range(1, epocas + 1):
    print(f"\nÉPOCA {epoca}")
    print("-" * 35)



    for linha in resultados_esperados:
        x1 = linha[0]
        x2 = linha[1]
        alvo = linha[2]

        # soma ponderada
        resultado = x1 * w1 + x2 * w2


        # validação através da função de ativação
        saida = ativacao(resultado) # - > recebe o resultado e passa pela função atiavacao que passa pelo "if"


        # erro = alvo - saída
        erro = alvo - saida


        # atualização dos pesos
        # fórmula:
        # w(m + 1) = w + lr * entrada * erro
        w1 = w1 + lr * x1 * erro
        w2 = w2 + lr * x2 * erro


        print(f"x1: {x1}")
        print(f"x2: {x2}")
        print(f"alvo: {alvo}")
        print(f"resultado: {resultado}")
        print(f"saída: {saida}")
        print(f"erro: {erro}")
        print(Fore.GREEN + f"novo w1: {w1}" )
        print(f"novo w2: {w2}" + Style.RESET_ALL)
        print("-" * 40)
        time.sleep(1)



print("\nPESOS FINAIS")
print(Fore.CYAN +f"w1 = {w1}")
print(f"w2 = {w2}" + Style.RESET_ALL)

