# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias_alugado = int(input('Quantidade de dias alugado: '))
km_pecorrido = float(input('Km pecorrido: '))
preco_dia = dias_alugado * 60
preco_km_rodado = km_pecorrido * 0.15
total_a_pagar = preco_dia + preco_km_rodado
print('O total a pagar é de R${:.2f}'.format(total_a_pagar))