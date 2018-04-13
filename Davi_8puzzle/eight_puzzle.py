#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import time
#Nome Davi Ferreira Santo 201519050046
#Para a execução insira o estado final e o inicial do jogo, altere a flag e execute o script
#na flag: 0 = bfs
#         1 = manhattan
#         2 = número de errados
#Nos resultados obtidos a partir da profundidade 16 o jogo demorou muito pra ser resolvido e então não terminei a execução deles.

final = np.matrix('1 2 3;4 5 6;7 8 0')
inicial = np.matrix('1 2 3;4 5 6;0 7 8')
flag = 0

def troca(estado,i1,j1,i2,j2): #troca duas posições da matriz dada
    aux = estado[i1,j1]
    estado[i1,j1] = estado[i2,j2]
    estado[i2,j2] = aux
    return estado

def gera_filhos(estado):
    lista_filhos = []

    i, j = np.where(estado == 0) #acho a posição onde está o 0
    i = i[0]
    j = j[0]

    if (i-1 >= 0): #Os if's abaixo movem o 0 de lugar e adicionam o novo estado na lista 
        lista_filhos.append(troca(estado.copy(),i,j,i-1,j)) 
    if (i+1 <= 2): 
        lista_filhos.append(troca(estado.copy(),i,j,i+1,j))
    if (j-1 >= 0): 
        lista_filhos.append(troca(estado.copy(),i,j,i,j-1))
    if (j+1 <= 2): 
        lista_filhos.append(troca(estado.copy(),i,j,i,j+1))

    return lista_filhos

def visitado(pai,visitados): #retorna dado um elemento e uma lista se o elemento está na lista
    resultado = False
    for val in visitados:
        if e_igual(pai,val):
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

def vstr(v):
    return "%d %d %d\n%d %d %d\n%d %d %d"%(v[0,0],v[0,1],v[0,2],v[1,0],v[1,1],v[1,2],v[2,0],v[2,1],v[2,2])

def e_igual(estado1,estado2): #compara dois estados
    resp = True
    for i in range(0,3):
        for j in range(0,3):
            if (estado1[i,j] != estado2[i,j]):
                resp = False
    return resp


def bfs(inicial,final,flag):
    sai = 1
    lista = [inicial]
    visitados = []
    hpais = dict()
    while(len(lista) > 0 and sai == 1):
        pai = lista[0]
        del lista[0]
        if not visitado(pai, visitados):
            visitados.append(pai)
            filhos = gera_filhos(pai)
            filhos = ordenacao_heuristica(filhos,flag)
            for filho in filhos:
                chave_filho = vstr(filho)
                if chave_filho not in hpais:
                    hpais[chave_filho] = vstr(pai)
                    lista.append(filho)
                    if e_igual(filho,final):
                        sai = 0
                        break
    # imprimir = []
    # sestado = vstr(final)
    # while sestado != vstr(inicial):
    #     imprimir.append(sestado)
    #     sestado = hpais[sestado]
    # imprimir.append(sestado)
    # for i in reversed(imprimir):
    #     print i
    #     print "\n"


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

def ordenacao_heuristica(lista,flag):
    list_output = []
    if flag != 0: #se flag = 0 não temos nenhum tipo de ordenação
        list_heuristicas = []
        for cel in lista:
            list_heuristicas.append(calc_heuristica(cel,flag))


        list_heuristicas = np.array(list_heuristicas)
        aux_list = np.argsort(list_heuristicas)

        for i in aux_list:
            list_output.append(lista[i])

        # printL(list_output)
        # print list_heuristicas
        # print aux_list

        # min_heuris = min(list_heuristicas)#pego a minha heuristica menor

        # for i, val in enumerate(list_heuristicas): #podo as heuristicas maiores que a minha mínima
        #     if val <= min_heuris:
        #         list_output.append(lista[i])

        lista = list_output        

    return lista
    

if __name__ == '__main__':
    start = time.time()
    bfs(inicial,final,flag)
    print time.time() - start 

    