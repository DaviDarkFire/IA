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
        # print "\n"
    print "\n"
    print "\n"
    print "\n"
    print "\n"

# def bfs(inicial,final,flag):
#     fila = [inicial]
#     visitados = []
#     while(True):
#         if (len(fila) == 0):
#             printL(visitados)
#             print "Solução não encontrada"
#             break
#         pai = fila[0]
#         del fila[0]
#         if not visitado(pai,visitados):
#             fila += gera_filhos(pai)
#             print len(fila)
#             poda_heuristica(fila,flag)
#             print len(fila)
#             if np.array_equal(pai,final):
#                 visitados.append(pai)
#                 print "fim"
#                 break

#         visitados.append(pai)
#     # printL(visitados)

# def vstr(v):
    # return "%d %d %d %d %d %d %d %d %d"%(v[0,0],v[0,1],v[0,2],v[1,0],v[1,1],v[1,2],v[2,0],v[2,1],v[2,2])

def vstr(v):
    return "%d %d %d\n%d %d %d\n%d %d %d"%(v[0,0],v[0,1],v[0,2],v[1,0],v[1,1],v[1,2],v[2,0],v[2,1],v[2,2])

def bfs(inicial,final,flag):
    gambs = 0
    lista = [inicial]
    visitados = []
    hpais = dict()
    while(len(lista) > 0):
        pai = lista[0]
        del lista[0]
        if not visitado(pai, visitados):
            visitados.append(pai)
            filhos = gera_filhos(pai)
            for filho in filhos:
                chave_filho = vstr(filho)
                if chave_filho not in hpais:
                    hpais[chave_filho] = vstr(pai)
                    lista.append(filho)

                    if np.array_equal(filho,final):
                        gambs = 1
                        break
            if gambs:
                break

    sestado = vstr(final)
    while sestado != vstr(inicial):
        print sestado
        print "\n"
        sestado = hpais[sestado]
    print sestado

def calc_heuristica(estado, flag):
    k = 1
    heuristica = 0
    for i in range(0,3):
        for j in range(0,3):
            if (k <= 8 ):
                m, n = np.where(estado == k)
                m = m[0]
                n = n[0]
                if flag == 1:#se flag = 1 faz-se heuristica com manhattan
                    heuristica += abs(i-m)+abs(j-n)        
                if flag == 2:#se flag = 2 faz-se heuristica com qtd de diferentes
                    if m != i or n != j:
                        heuristica += 1 
            k += 1;
    return heuristica        

def poda_heuristica(lista,flag):
    list_output = []
    if flag != 0: #se flag = 0 não temos nenhum tipo de poda
        list_heuristicas = []
        for cel in lista:
            list_heuristicas.append(calc_heuristica(cel,flag))

        min_heuris = min(list_heuristicas)#pego a minha heuristica menor

        for i, val in enumerate(list_heuristicas): #podo as heuristicas maiores que a minha mínima
            if val <= min_heuris:
                list_output.append(val)

        lista = list_output        

    return lista
    

if __name__ == '__main__':
    inicial = np.matrix('1 2 3;4 5 6;0 7 8')
    final = np.matrix('1 2 3;4 5 6;7 8 0')
    bfs(inicial,final,0)
    