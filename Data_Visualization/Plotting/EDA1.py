# Ploting of Exploretary Data Analysis 

'''
1. Understanding of Features And Target Variable
2. Scatter Plot --- Visualize in 2 Dimensions
3. Pair Plot --- If you have 4d,5d and 6d then visualize your data
4. Histogramme --- Analysis one Feature (How Many Datapoints we have in a interval)
5. PDF --- Probablity Distribution Function (Probablity of datapoint in a interval)
6. CDF --- Cummulative Distribution Function (Mostly for telling efficency )
'''


# Objective --- If Someone give a flower then tell that flower belongs to which Class.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 1. Understanding the Dataset (How Many Rows,Columns)

iris = pd.read_csv("iris.csv")
print(iris.shape)  # (150,5)
print(iris.columns)  # ['sepal_length', 'sepal_width', 'petal_length', 'petal_width','species']
print(iris['species'].value_counts())   # This is A Balanced Dataset

# 2. Scatter Plot

sns.set_style("whitegrid")
sns.FacetGrid(iris,hue='species',size=6).map(plt.scatter,'sepal_length','sepal_width').add_legend()
plt.show()

# Oberservation -- Using Sl And Sw we can distnguish between setosa and Another Flower.

# 3. Pair Plot

sns.set_style("whitegrid")
sns.pairplot(iris,hue="species",size=5)
plot.show() 
# Oberservation -- Most Important Feature is Petel Length And Petel Width.

# 4. Histogramme,pdf,cdf --- Analysis One Feature
all_species = iris['species']
all_versicolor = iris.loc[iris['species']=='versicolor']
all_setosa = iris.loc[iris['species']=='setosa']
all_virginica = iris.loc[iris['species']=='virginica']


sns.FacetGrid(iris,hue='species',size=6).map(sns.distplot,'sepal_length').add_legend()
plt.show()


sns.FacetGrid(iris,hue='species',size=6).map(sns.distplot,'sepal_width').add_legend()
plt.show()

sns.FacetGrid(iris,hue='species',size=6).map(sns.distplot,'petal_length').add_legend()
plt.show()

# Oberervation --- with the help of petal length i can distribute setosa and versicolor And Virginica

sns.FacetGrid(iris,hue='species',size=6).map(sns.distplot,'petal_width').add_legend()
plt.show()

count,n_bins = np.histogram(all_setosa['petal_length'],bins=10,density=True)

pdf = count/sum(count)

cdf = np.cumsum(pdf)

plt.plot(n_bins[1:],pdf)
plt.plot(n_bins[1:],cdf)
plt.show()

# if petal length is less then 1.6 then 82% Flowers is setosa






