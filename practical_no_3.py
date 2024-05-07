# -*- coding: utf-8 -*-
"""Practical no. 3

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p64EqAYBkgMPa0Uttc53naCTbQeEnaI7
"""

#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

#load data
df = pd.read_csv("/content/loan.csv")
print("First few rows of the loan dataset:")
print(df.head())

print("Shape of the dataset:", df.shape)

print("Information about the dataset:")
print(df.info())

print("Number of missing values in each column:")
print(df.isna().sum())

#Filling null values with mean
df["ApplicantIncome"].fillna(df["ApplicantIncome"].mean(), inplace=True)
df["CoapplicantIncome"].fillna(df["CoapplicantIncome"].mean(), inplace=True)
df["LoanAmount"].fillna(df["LoanAmount"].mean(), inplace=True)
df["Credit_History"].fillna(np.random.randint(0,2), inplace=True)

grouped_df = df[["ApplicantIncome", "CoapplicantIncome", "LoanAmount","Credit_History"]].groupby(df["Loan_Status"])

#Measures of Central Tendency
#mean
mean = grouped_df.mean()
print("Mean:")
print(mean)

#median
median = grouped_df.median()
print("\nMedian:")
print(median)

#mode
mode = df['LoanAmount'].mode()
print("\nMode:")
print(mode)

#Minimum
min = grouped_df.min()
print("\nMinimum:")
print(min)

#Maximum
max = grouped_df.max()
print("\nMaximum:")
print(max)

#Measures of Dispersion
#standard deviation
std = grouped_df.std()
print("\nStandard Deviation:")
print(std)

#variance
var = grouped_df.var()
print("\nVariance:")
print(var)

#Interquartile Range
from scipy.stats import iqr
iqr_value = iqr(df['LoanAmount'])
print("\nInterquartile Range:", iqr_value)

#Skewness
skewness = grouped_df.skew()
print("\nSkewness:")
print(skewness)

#Putting everything together
description = df.describe()
print("\nSummary Statistics:")
print(description)
description_all = df.describe(include='all')
print("\nSummary Statistics (including all columns):")
print(description_all)

# Import necessary libraries
import pandas as pd

# Load the Iris dataset
iris = pd.read_csv('/content/iris.csv')

# Display the first few rows of the dataset
print("\nFirst few rows of the Iris dataset:")
print(iris.head())

# 1. Display basic statistical details for 'Iris-setosa'
setosa_stats = iris[iris['species'] == 'setosa'].describe()

# Display the statistical details for 'Iris-setosa'
print("\nStatistical details for 'Iris-setosa':")
print(setosa_stats)

# 2. Display basic statistical details for 'Iris-versicolor'
versicolor_stats = iris[iris['species'] == 'versicolor'].describe()

# Display the statistical details for 'Iris-versicolor'
print("\nStatistical details for 'Iris-versicolor':")
print(versicolor_stats)

# 3. Display basic statistical details for 'Iris-virginica'
virginica_stats = iris[iris['species'] == 'virginica'].describe()

# Display the statistical details for 'Iris-virginica'
print("\nStatistical details for 'Iris-virginica':")
print(virginica_stats)