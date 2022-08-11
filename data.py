#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: William Keilsohn
"""

# Import Packages:
import numpy as np
import pandas as pd
import os

# Declare variables:
path = os.getcwd() + '/'
file = path + 'Data_Quality_Test_Case.xlsx'
unknowns = ['None', 'NONE', 'UNKNOWN', 'Unknown']

# Create a dataframe:
excel_file = pd.ExcelFile(file)
sheets = excel_file.sheet_names[1:3]
valid_df = pd.read_excel(file, sheet_name = sheets[0])
valid_bov = valid_df.iloc[:, 1:3]
valid_aux = valid_df.iloc[:, 3:]
permisable_df = pd.read_excel(file, sheet_name = sheets[1])
perm_bov = permisable_df.iloc[0:151, :]
perm_aux = permisable_df.iloc[151:, :]
del excel_file, valid_df, permisable_df

# Declare Functions:
def replace_unknowns(df):
    for i in unknowns:
        df = df.replace(i, np.nan)
    return df

def pers(v1, v2):
    total = v1 + v2
    p1 = (v1 / total) * 100
    p2 = (v2 / total) * 100
    return [total, p1, p2]


# Organize the data
df_ls = [valid_bov,valid_aux, perm_bov, perm_aux]
    
# Answer the Questions:
### Q1
for i in range(0, len(df_ls)):
    df_ls[i] = df_ls[i].dropna()

bov_rec = len(df_ls[0].index)
aux_rec = len(df_ls[1].index)
print(bov_rec, aux_rec)
print(pers(bov_rec, aux_rec))

### Q2
for i in range(0, len(df_ls)):
    df_ls[i] = replace_unknowns(df_ls[i])

for i in range(0, len(df_ls)):
    df_ls[i] = df_ls[i].dropna()
del perm_aux, perm_bov, valid_aux, valid_bov

bov_rec = len(df_ls[0].index)
aux_rec = len(df_ls[1].index)
print(bov_rec, aux_rec)
print(pers(bov_rec, aux_rec))

### Q3
bov_count = 0
aux_count = 0
for i in list(df_ls[0].iloc[:, 0]):
    if i in list(df_ls[2].iloc[:, 1]):
        bov_count = bov_count +  1

for j in list(df_ls[0].iloc[:, 0]):
    if j in list(df_ls[3].iloc[:, 1]):
        aux_count = aux_count + 1
del i, j 
print(str(bov_count), str(aux_count))
print(pers(bov_count, aux_count))

### Q4
bov_count = 0
bov_ls_1 = list(df_ls[0].iloc[:, 0])
bov_ls_2 = list(df_ls[0].iloc[:, 1])
length_bov = len(bov_ls_1)

for i in range(0, length_bov):
    if bov_ls_1[i] in list(df_ls[2].iloc[:, 1]) and bov_ls_2[i] in list(df_ls[2].iloc[:, 3]):
        bov_count = bov_count + 1
del i
print(str(bov_count))