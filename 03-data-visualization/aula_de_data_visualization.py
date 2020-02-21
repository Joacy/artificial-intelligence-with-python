# -*- coding: utf-8 -*-
"""Aula de Data Visualization

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NClSiZMcJi5nZSihcFdD4V9TOIaeh3-j
"""

import pandas as pd

uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.1/movies.csv"
filmes = pd.read_csv(uri) # data_frame
filmes.columns = ["filmeId", "titulo", "generos"]
filmes = filmes.set_index('filmeId')
filmes = filmes.join(filmes['generos'].str.get_dummies()).drop('generos', axis=1)
filmes['ano'] = filmes['titulo'].str.extract(r'.*\((\d+)\)')
filmes = filmes.dropna()
# filmes.head()

uri_notas = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv"
notas = pd.read_csv(uri_notas)
notas.columns = ["usuarioId", "filmeId", "nota", "instante"]
arredondadas = notas["nota"].round(1)
# notas.head()

medias = notas.groupby("filmeId")["nota"].mean()
filmes = filmes.join(medias).dropna().sort_values("nota", ascending=False).rename(columns = {'nota' : 'media'})

total = notas.groupby("filmeId")["instante"].count()
filmes = filmes.join(total)
filmes = filmes.rename(columns={"instante" : "total"})
filmes = filmes.query("total > 50")
filmes["media_categoria"] = (filmes["media"]).round(1).values

random_filmes = filmes.sample(10)
# random_filmes.head()

notas["nota"].hist()

arredondadas.value_counts().plot.pie()

arredondadas.value_counts().plot.bar()

import seaborn as sns

import matplotlib.pyplot as plt

sns.countplot(arredondadas)
plt.title("Distribuição das Notas");

palette = sns.color_palette("Blues", 10)
palette = sns.cubehelix_palette(10, start=2, rot=0, dark=0, light=.65)
sns.countplot(arredondadas, palette=palette)
plt.title("Distribuição das Notas");

sns.distplot(filmes["media"])

p = sns.barplot(data = random_filmes, x = "titulo", y = "media")
p.set_xticklabels(p.get_xticklabels(), rotation = 45, horizontalalignment = "right")
plt.title("Notas médias de 10 filmes")
plt.show()

sns.catplot(data = filmes, x = "Action", y = "media")

sns.distplot(filmes.query("Action == 1")["media"])
sns.distplot(filmes.query("Action == 0")["media"])

ids_aleatorios = ",".join(random_filmes.index.values.astype(str))
query = f"filmeId in (.{ids_aleatorios}.)"
sns.boxplot(data = notas.query(query), x = "filmeId", y = "nota")
plt.show()

total_de_categorias = len(filmes['media_categoria'].unique())
sns.catplot(data=filmes, x = "ano", y="media", palette = sns.color_palette("Blues", total_de_categorias), hue="media_categoria")

