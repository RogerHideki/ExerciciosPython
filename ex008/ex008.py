distancia = float(input('Uma distância em metros: '))
print('A medida de {}m corresponde a\n{}km\n{}hm'.format(distancia, distancia / 1000, distancia / 100))
print('{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(distancia / 10, 10 * distancia, 100 * distancia, 1000 * distancia))
