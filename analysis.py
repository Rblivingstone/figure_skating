#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 23:01:16 2018

@author: ryan
"""

import pandas as pd
from normalization import *
import matplotlib.pyplot as plt

df = pd.read_csv('data/figure_skating.csv')
df.dropna(subset=['Rank'],inplace=True)
df.index = range(len(df))
df['Result'].hist()
plt.title("Distribution of Women's Figure Skating Scores"
          "\nSochi 2014 Raw Scores")
plt.ylabel('Number of Athletes')
plt.xlabel('Score')
plt.show()

df['pnorm'] = percentile_norm(df['Result'])
plt.hist(df['pnorm'])
plt.title("Distribution of Women's Figure Skating Scores"
          "\nSochi 2014 Percentile Normalized")
plt.xlabel('Normalized Score')
plt.ylabel('Number of Athletes')
plt.show()

plt.scatter(df['Result'],df['pnorm'])
plt.title('Monotonic Transformation for Percentile Normalization')
plt.show()

df['gqnorm'] = gaussian_quantile_norm(df['Result'],seed=19755213)
plt.hist(df['gqnorm'])
plt.title("Distribution of Women's Figure Skating Scores"
          "\nSochi 2014 Guassian Quantile Normalized")
plt.xlabel('Normalized Score')
plt.ylabel('Number of Athletes')
plt.show()

plt.scatter(df['Result'],df['gqnorm'])
plt.title('Monotonic Transformation for Gaussian Quantile Normalization')
plt.show()

df['bcnorm'] = boxcox_norm(df['Result'])[0]
plt.hist(df['bcnorm'])
plt.title("Distribution of Women's Figure Skating Scores"
          "\nSochi 2014 Box-Cox Normalized")
plt.xlabel('Normalized Score')
plt.ylabel('Number of Athletes')
plt.show()

plt.scatter(df['Result'],df['bcnorm'])
plt.title('Monotonic Transformation for Box-Cox Normalization')
plt.show()
