#  Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco_produto = float(input('Qual é o preço do produto: R$'))
desconto = preco_produto * 0.05
novo_preco = preco_produto - desconto
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco_produto, novo_preco))