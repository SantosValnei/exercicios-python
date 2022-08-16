# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Qual é o salário do funcionario: R$'))
reajuste_salarial = salario * 0.15
novo_salario = salario + reajuste_salarial
print('O produto que custava R${}, na promoção com desconto de 15% vai custar R${:.2f}'.format(salario, novo_salario))