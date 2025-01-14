# -*- coding: utf-8 -*-
"""Practical no. 9

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TAasnlxHFVKq_JNd2Tb8a65QL9Bml2TG
"""

import seaborn as sns
import matplotlib.pyplot as plt
# Load the Titanic dataset
titanic = sns.load_dataset('titanic')
# Plotting a box plot for distribution of age with respect to each gender and survival
plt.figure(figsize=(12, 6))
sns.boxplot(x='sex', y='age', hue='survived', data=titanic, palette='Set2')
plt.title('Distribution of Age by Gender and Survival')
plt.xlabel('Gender')
plt.ylabel('Age')
plt.show()