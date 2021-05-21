import os
import pandas as pd
import docx
# path = 'C:/Users/svasiliev/Desktop/_archive/try.docx'
path = 'Z:/Сотрудники'
d = {}
main_list = [(root, folders, filename) for root, folders, files in os.walk(path) for filename in files]

df = pd.DataFrame(main_list)
df.to_csv('try.csv')