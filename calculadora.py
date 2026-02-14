print('Hello world!')

# Float permite números decimais
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
operacao = input('Digite a operação (+, -, *, /): ')

if operacao == '+':
    res = num1 + num2
elif operacao == '-':
    res = num1 - num2
elif operacao == '*':
    res = num1 * num2
elif operacao == '/':
    if num2 != 0:
        res = num1 / num2
    else:
        res = 'Erro: divisão por zero!'
else:
    res = 'Operação inválida'

print('Resultado:', res)
