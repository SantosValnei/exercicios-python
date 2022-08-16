# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura: '))
area = largura * altura
tinta = area / 2
print('Sua parede tem a dimensao de {}x{} e sua área é de {:.3f}m².\n Para pintar essa parede, você precisará de {:.4f}l de tinta.'.format(largura, altura, area, tinta))