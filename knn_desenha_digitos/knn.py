#!/usr/bin/python
import csv
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import RandomizedSearchCV

def load_data(filename):
    d = csv.reader(open('alturapeso.csv'))
    x = []
    y = []
    for line in d:
        x.append([float(line[0]),float(line[1])])
        y.append(int(line[2]))
    return x,y

if __name__ == '__main__':
    x,y = load_data('alturapeso.csv')
    print len(x)
    x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.25)

    print len(x_train)
    print len(x_test)
    
    obj = KNeighborsClassifier()
    params = {'n_neighbors':range(1,50)} #cria parametros de 1 a 50, o famoso k (nesse caso)
    rsearch = RandomizedSearchCV(obj,params,scoring='accuracy')

    rsearch.fit(x_train,y_train) 
    print y_train
    print rsearch.best_score_
    print rsearch.best_params_

    obj = rsearch.best_estimator_ #pega o melhor estimador (no nosso caso, o melhor k ) e executa o knn com este estimador
    obj.fit(x_train,y_train)
    res = obj.predict(x_test)
    print accuracy_score(y_test,res)
   
    # obj.fit(x_train,y_train)
    # res = obj.predict(x_test)
    # print accuracy_score(y_test,res)
    # if res == 1:
    #   print "Mulher"
    # else:
    #   print "Macho"