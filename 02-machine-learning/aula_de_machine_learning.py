# -*- coding: utf-8 -*-
"""Aula de Machine Learning

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BRiiguVAMFnS7Xo8twIQNGkfdQ8uu1eD
"""

# pelo longo?
# perna curta?
# faz auau?
porco1 = [0, 1, 0]
porco2 = [0, 1, 1]
porco3 = [1, 1, 0]

cachorro1 = [0, 1, 1]
cachorro2 = [1, 0, 1]
cachorro3 = [1, 1, 1]

treino_x = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
treino_y = [1, 1, 1, 0, 0, 0] # 0 -> cachorro 1 -> porco

from sklearn.svm import LinearSVC

modelo = LinearSVC()
modelo.fit(treino_x, treino_y)

animal_misterioso = [1, 1, 1]
modelo.predict([animal_misterioso])

misterio1 = [1,1,1]
misterio2 = [1,1,0]
misterio3 = [0,1,1]

teste_x = [misterio1, misterio2, misterio3]
teste_y = [0,1,1]

previsoes = modelo.predict(teste_x)
previsoes

from sklearn.metrics import accuracy_score
accuracy_score(teste_y, previsoes)

