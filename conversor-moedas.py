# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

dinheiro_em_carteira = float(input('Quando em R$ reais você tem de na carteira? '))
dolar = dinheiro_em_carteira / 5.14
print('Com R${} você pode comprar U${:.2f}'.format(dinheiro_em_carteira, dolar))