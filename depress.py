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


path1 = 'C:/Users/cth/PycharmProjects/_to_do/depres/scores.csv'
path2 = 'C:/Users/cth/PycharmProjects/_to_do/depres/condition/'
path3 = 'C:/Users/cth/PycharmProjects/_to_do/depres/control/'
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
categories = ['gender' ,'afftype', 'melanch', 'inpatient', 'marriage', 'work', 'edu']
scores[categories] = scores[categories].astype('category')
scores['group'] = np.where(scores.number.str.contains('condition'),'condition','control' )

cond_df['timestamp'] = pd.to_datetime(cond_df['timestamp'], format = '%Y-%m-%d %H:%M:%S')
cond_df.set_index('timestamp', inplace = True)
grouped = cond_df.groupby(['file'])

for x,y in grouped:
    for i in range(1,9):
        plt.subplot(3,3, i)
        plt.plot(y['date'], y['activity'])


# grouped = cond_df.groupby(['file', 'timestamp'])['activity']
# plt.bar(pers_activ.index, pers_activ.values)
# pers_activ.droplevel('file')
# for index, (i,j), z in pers_activ:
#     plt.subplot(3,3,index + 1)
#     plt.bar(i, z)
