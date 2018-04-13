#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import numpy as np
import eight_puzzle as ep

# inicial = np.matrix('1 2 3;4 5 6;0 7 8')
final = np.matrix('1 2 3;4 5 6;7 8 0')
# inicial = np.matrix('5 7 2;8 1 6;3 4 0')

lista = []
lista.append(np.matrix('1 2 3;4 5 6;0 7 8'))
lista.append(np.matrix('1 2 3;4 5 6;7 0 8'))
lista.append(np.matrix('1 0 2;4 5 3; 7 8 6'))
lista.append(np.matrix('1 5 2;4 0 3; 7 8 6'))
lista.append(np.matrix('1 5 2;0 4 3; 7 8 6'))
lista.append(np.matrix('1 5 2;7 4 3; 0 8 6'))
lista.append(np.matrix('1 5 2;7 4 3; 8 0 6'))
lista.append(np.matrix('1 5 2;7 0 3; 8 4 6'))
lista.append(np.matrix('1 5 2;7 3 0; 8 4 6'))
lista.append(np.matrix('1 5 2;7 3 6; 8 4 0'))
lista.append(np.matrix('1 5 2;7 3 6; 8 0 4'))
lista.append(np.matrix('1 5 2;7 0 6; 8 3 4'))
lista.append(np.matrix('1 5 2;0 7 6; 8 3 4'))
lista.append(np.matrix('0 5 2;1 7 6; 8 3 4'))
lista.append(np.matrix('5 0 2;1 7 6; 8 3 4'))
lista.append(np.matrix('5 7 2;1 0 6; 8 3 4'))
lista.append(np.matrix('5 7 2;0 1 6; 8 3 4'))
lista.append(np.matrix('5 7 2;8 1 6; 0 3 4'))
lista.append(np.matrix('5 7 2;8 1 6; 3 0 4'))
lista.append(np.matrix('5 7 2;8 1 6; 3 4 0'))

with open('saida.csv', 'w') as csvfile:
        fieldnames = ['Movimentos','BFS','BFS MANHATTAN','BFS NÚMERO ERRADOS']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

f = open('saida.csv','a')
for i in range(1,21):
    s = []
    for j in range(0,3):
        s.append(ep.main(lista[i-1],final,j))

    f.write(str(i)+','+str(s[0])+','+str(s[1])+','+str(s[2])+'\n')