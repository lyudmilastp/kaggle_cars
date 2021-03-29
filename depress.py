import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


pd.set_option('display.max_rows', 50)
pd.set_option('display.min_rows', 20)
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 150)
pd.set_option('display.precision', 4)
pd.set_option('expand_frame_repr', True)

#  Read all csv files. Control group / Condition group / Total scores


path1 = 'C://Users/cth/PycharmProjects/sources/data/scores.csv'
path2 = 'C://Users/cth/PycharmProjects/sources/data/condition/'
path3 = 'C://Users/cth/PycharmProjects/sources/data/control/'
cond_df = pd.DataFrame()
control_df = pd.DataFrame()
scores  = pd.read_csv(path1)


for i in os.listdir(path2):
    if cond_df.empty:
        cond_df = pd.read_csv(path2 + str(i))
        cond_df['file'] = i
    temp = pd.read_csv(path2 + str(i))
    temp['file'] = i
    cond_df = cond_df.append(temp)


for i in os.listdir(path3):
    if control_df.empty:
        control_df = pd.read_csv(path3 + str(i))
        control_df['file'] = i
    temp = pd.read_csv(path3 + str(i))
    temp['file'] = i
    control_df = control_df.append(temp)


#######################################################################################

scores['madrs_delta'] = scores.madrs2 - scores.madrs1


grouped = cond_df.groupby(['file', 'date'])
cond_list = list(zip(*cond_df.groupby('file')))
cond_list = cond_list[1]
for index, i in enumerate(cond_list):
    print(index)
    print(i['activity'].mean())