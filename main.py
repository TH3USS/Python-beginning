print('Hello World!')

# variavel

nome = 'Programador Python'
idade = 27
peso = 70.3

print(nome)
print(idade)
print(peso)

nome = input('Digite seu nome:')
idade = int( input('Digite sua idade:'))
peso = float( input('Digite seu peso:'))

print(len(nome)) # len retorna o tamanho da string
print(type(idade)) #type retorna o tipo da variavel
print(peso)

# operadores

soma = 1 + 1
subtracao = 2 - 2
divisao = 30 / 3
multiplicacao = 4 * 4
potencia = 7 ** 2

print('soma', soma)
print('subtracao', subtracao)
print('divisao', divisao)
print('multiplicacao', multiplicacao)
print('divisao', divisao)
print('potencia', potencia)

# condicionais

idade = int(input('Informe a sua idade: '))

if idade >= 18:
    print('Permitido')
elif idade >= 60 and idade >= 18:
    print('Permitido, mas não aconselhado')
elif idade >= 6 or idade > 0:
    print('Muito jovem')
else:
    print('Não pode')

# LISTAS

lista_numeros = [1, 2, 3]

print(lista_numeros[0])
print(lista_numeros[1])
print(lista_numeros[2])

lista_numeros.append(4) # adiciona no fim

print(lista_numeros)
print(len(lista_numeros))
print(min(lista_numeros)) # acha o valor minimo
print(max(lista_numeros)) # acha o valor maximo

# lacos de repeticao
notas = []
for x in range(5):
    notas.append(x)

for n in notas:
    print(n[0])

notas2 = []
contador = 1
while contador <= 5:
    notas.append(contador)

    contador += 1

# dicionario
# uma lista fica dentro de chaves [], uma dicionario dentro de {}

pessoa = {
    'nome': 'Programador Pyhton',
    'idade': 27,
    'peso': 70.2
}

# lista de dicionarios
pessoas = [
    {'nome': 'Ana','idade': 27,'peso': 70.2},
    {'nome': 'Caio','idade': 24,'peso': 60.2}
]

print(pessoa['nome'])

# funcoes

def minha_funcao(valor1, valor2):
    return valor1 + valor2

while True:
    valor1 = int(input('valor1: '))
    valor2 = int(input('valor2: '))

    resposta = minha_funcao(valor1, valor2)
    print(valor1, '+', valor2, '=', resposta)