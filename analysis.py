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

plt.hist(percentile_norm(df['Result']))
plt.show()

plt.hist(gaussian_quantile_norm(df['Result'],seed=19755213))
plt.show()

plt.hist(boxcox_norm(df['Result'])[0])
plt.show()