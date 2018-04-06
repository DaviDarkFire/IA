#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

def troca(estado,i1,j1,i2,j2): #troca duas posições da matriz dada
    aux = estado[i1,j1]
    estado[i1,j1] = estado[i2,j2]
    estado[i2,j2] = aux
    return estado

def gera_filhos(estado):
    lista_filhos = []

    i, j = np.where(estado == 0) #acho a posição onde está o 0

    if (i-1 >= 0): #Os if's abaixo movem o 0 de lugar e adicionam o novo estado na lista 
        lista_filhos.append(troca(estado.copy(),i,j,i-1,j)) 
    if (i+1 <= 2): 
        lista_filhos.append(troca(estado.copy(),i,j,i+1,j))
    if (j-1 >= 0): 
        lista_filhos.append(troca(estado.copy(),i,j,i,j-1))
    if (j+1 <= 2): 
        lista_filhos.append(troca(estado.copy(),i,j,i,j+1))

    return lista_filhos

def visitado(pai,visitados):
    resultado = False
    for val in visitados:
        if np.array_equal(pai,val):
            resultado = True
    return resultado

def printL(lista):
    for val in lista:
        print val
        print "\n"
    print "\n"
    print "\n"
    print "\n"
    print "\n"

def bfs(inicial,final):
    fila = [inicial]
    visitados = []
    while(True):
        pai = fila[0]
        del fila[0]
        if not visitado(pai,visitados):
            fila += gera_filhos(pai)
            printL(fila)
            if np.array_equal(pai,final):
                print "fim"
                break

        visitados.append(pai)

def calc_heuristica(estado):
    k = 1
    heuristica = 0
    for i in range(0,3):
        for j in range(0,3):
            if (k <= 8 ):
                m, n = np.where(estado == k)
                m = m[0]
                n = n[0]
                heuristica += abs(i-m)+abs(j-n)        
            k += 1;
    return heuristica        



def busca_heuristica():
    print "topper"

if __name__ == '__main__':
    inicial = np.matrix('1 2 3;8 0 4;7 6 5')
    final = np.matrix('1 2 3;4 5 6;7 8 0')
    # bfs(inicial,final)
    teste = np.matrix('0 1 2;7 8 3;6 5 4')
    print calc_heuristica(teste)