#!/usr/bin/python

import unittest
from monges_canibais import gera_filhos

class test_monges(unittest.TestCase):
    def test_gera_filhos(self):
        v = []
        v.append([ [2, 2, 1] , [[0, 2, -1], [1, 1, -1]]])
        v.append([ [3, 2, 1] , [[3, 0, -1], [2, 2, -1], [3, 1, -1]] ])
        v.append([ [3, 3, 1] , [[3, 1, -1], [2, 2, -1], [3, 2, -1]] ])
        v.append([ [3, 1, 1] , [[1, 1, -1], [3, 0, -1]] ])
        v.append([ [0, 3, 1] , [[0, 1, -1], [0, 2, -1]] ])
        v.append([ [0, 2, 1] , [[0, 0, -1], [0, 1, -1]] ])
        for vtest in v:
            pai = vtest[0]
            filhos = vtest[1]
            gfilhos = gera_filhos(pai)
            for filho in gfilhos:
                self.assertTrue(filho in filhos)
            for filho in filhos:
                self.assertTrue(filho in gfilhos)
               
def vstr(v):
    return "%d %d %d"%(v[0],v[1],v[2])

def bfs(inicial,final):
    lista = [inicial]
    visitados = []
    hpais = dict()
    while(len(lista) > 0):
        pai = lista[0]
        del lista[0]
        if pai not in visitados:
            print "visitado"
            visitados.append(pai)
            filhos = gera_filhos(pai)
            for filho in filhos:
                chave_filho = vstr(filho)
                # print "chave_filho: "+chave_filho
                if chave_filho not in hpais:
                    hpais[chave_filho] = vstr(pai)
                    lista.append(filho)
                    print pai,filho
                    if filho == final:
                        break
    sestado = vstr(final)
    while sestado != vstr(inicial):
        print sestado
        sestado = hpais[sestado]
    print sestado



       

if __name__ == '__main__':
    unittest.main
    bfs([3,3,1],[0,0,-1])