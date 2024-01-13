"""Crie um programa que mostre quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar

Considere US$1,00 = R$3,27"""

valor = float(input('Digite quanto dinheiro você tem: '));
valorDolarAtual = float(input('Digite o valor do dolar atual: '))
print('O valor {} convertido em dolar é {:.2f}'.format(valor, valor / valorDolarAtual))