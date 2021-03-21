import pandas as pd
import numpy as np


df = pd.DataFrame( {"Column1" : [15, 14, 13],
                    "Column2" : 15, "Column3" : 15 }, index = ['First', 'First', 'Third'])



# function to lookup a list of all matches for __a__ in index from Column1
def look_up(name, column_name ):
    s = df.loc[df.index == name, column_name]
    #for no match
    if s.empty:
        return np.nan
    #for match only one value
    elif len(s) == 1:
        return s.item()
    else:
    #for return multiple values
        return s.tolist()

look_up('First', 'Column2')

df[df.index == 'First']