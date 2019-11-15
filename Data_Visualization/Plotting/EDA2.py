'''
Mean,Variation,Standard Deviation
Median, Deviation , Median Absolute Deviation,percentile,Quartile
Box Plot -- Combination of meidan,Percentile and interQuantile Range
Vilin Plot -- Box Plot With Histogram

****( Box Plot we use Genreally)
**** Never Forgot your objective and Conclusion.
'''

import pandas as pd
import numpy as np
#read the file
iris = pd.read_csv("iris.csv")

# How Many Lables in my target variable
print(iris['species'].value_counts())

a_versicolor = iris.loc[iris['species']=='versicolor']
a_virginica = iris.loc[iris['species']=='virginica']
a_setosa = iris.loc[iris['species']=='setosa']


# Part -A . Mean and Standard Deviation

print(np.mean(a_versicolor['petal_length']))  #4.26
print(np.mean(a_virginica['petal_length']))  # 5.552
print(np.mean(a_setosa['petal_length']))     # 1.464

print(np.mean(np.append(a_setosa['petal_length'],50)))   # 2.41

# not Robust of Outliers

print(np.std(a_versicolor['petal_length']))  #0.46
print(np.std(a_virginica['petal_length']))  # 0.54
print(np.std(a_setosa['petal_length']))     # 0.17


# Part -B Median, Deviation , Median Absolute Deviation,percentile,Quartile

# Steps involve in median --- sorting then chosse middle term

print(np.median(a_versicolor['petal_length']))  #4.35
print(np.median(a_virginica['petal_length']))  # 5.55
print(np.median(a_setosa['petal_length']))     # 1.5

from statsmodels import robust
print(robust.mad(a_versicolor['petal_length']))  # 0.51
print(robust.mad(a_virginica['petal_length']))  # 0.66
print(robust.mad(a_setosa['petal_length']))     # 0.14

# Percentile
print(np.percentile(a_versicolor['petal_length'],90))  #4.8
print(np.percentile(a_virginica['petal_length'],90))  # 6.31
print(np.percentile(a_setosa['petal_length'],90))     # 1.7

# Quartle
print(np.percentile(a_versicolor['petal_length'],np.arange(0,100,25)))  #[3.   4.   4.35 4.6 ]
print(np.percentile(a_virginica['petal_length'],np.arange(0,100,25)))  # [4.5   5.1   5.55  5.875]
print(np.percentile(a_setosa['petal_length'],np.arange(0,100,25)))     #[1.    1.4   1.5   1.575]


# Step -3 Boxplot we use for analysis 1D Array

import seaborn as sns
sns.boxplot(x = "species",y = "petal_length",data=iris)

# Vilion Plot
sns.violinplot(x = "species",y = "petal_length",data=iris)





















