#!/usr/bin/python

MONGES   = 0
CANIBAIS = 1
BARCO    = 2

def estado_valido(estado):
    ret = True
    cestado = [3-estado[MONGES],3-estado[CANIBAIS]]
    if estado[MONGES] < 0    or estado[MONGES] > 3:    ret = False 
    if estado[CANIBAIS] < 0  or estado[CANIBAIS] > 3:  ret = False 
    if cestado[MONGES] < 0   or cestado[MONGES] > 3:   ret = False 
    if cestado[CANIBAIS] < 0 or cestado[CANIBAIS] > 3: ret = False 
    if estado[MONGES] !=0    and  estado[MONGES] < estado[CANIBAIS]:  ret = False
    if cestado[MONGES] !=0   and cestado[MONGES] < cestado[CANIBAIS]: ret = False
 
    return ret

def gera_filhos(estado):
    ret = []
    # 1 monge
    m1 = [estado[MONGES] - estado[BARCO],estado[CANIBAIS],estado[BARCO]*-1]
    if estado_valido(m1):
        ret.append(m1)

    # 2 monges
    m2 = [estado[MONGES] - 2*estado[BARCO],estado[CANIBAIS],estado[BARCO]*-1]
    if estado_valido(m2):
        ret.append(m2)

    # 1 canibal
    c1 = [estado[MONGES],estado[CANIBAIS] - estado[BARCO],estado[BARCO]*-1]
    if estado_valido(c1):
        ret.append(c1)

    # 2 canibais
    c2 = [estado[MONGES],estado[CANIBAIS] - 2*estado[BARCO],estado[BARCO]*-1]
    if estado_valido(c2):
        ret.append(c2)

    # 1 monge 1 canibal
    m1c1 = [estado[MONGES] - estado[BARCO],estado[CANIBAIS] - estado[BARCO],estado[BARCO]*-1]
    if estado_valido(m1c1):
        ret.append(m1c1)


    return ret

