from rosreestr2coord import Area
import pandas as pd
import json
from geojson import Polygon
import geojson

cad_nums = ["42:07:0111003:1945","42:07:0111001:325","42:07:0111003:1944","70:17:0000009:466","70:17:0000009:468","70:17:0000009:444","70:17:0000009:467","70:17:0000009:461","70:17:0000009:1070","70:17:0000009:291","70:17:0000009:1025","70:17:0000009:1026","70:17:0000009:1028","70:17:0000009:1029","70:17:0000009:459","70:17:0000009:460","70:17:0000013:254","70:17:0000013:255","70:17:0000013:33","70:13:0100012:302","70:13:0101002:97","70:17:0000021:4","70:00:0000000:98", "70:17:0000009:1349", "70:17:0000009:1078", "70:02:0200046:1269","70:17:0000009:46","70:17:0000009:1071","70:17:0000000:259","70:17:0000015:157","70:17:0000009:0469" , "70:13:0100016:417", "70:13:0100016:418", "70:17:0000013:983", "70:17:0000013:989", "70:17:0000015:4060"]
cad_nums_rent = ["70:13:0101002:97","70:17:0000021:4","70:00:0000000:98", "70:17:0000009:1349", "70:17:0000009:1078", "70:02:0200046:1269","70:17:0000009:46","70:17:0000009:1071","70:17:0000000:259","70:17:0000015:157","70:17:0000009:0469" , "70:13:0100016:417", "70:13:0100016:418", "70:17:0000013:983", "70:17:0000013:989", "70:17:0000015:4060"]


areas = [Area(num) for num in cad_nums]
df = pd.DataFrame([area.get_attrs() for area in areas if area.get_coord() !=[]])
df['geometry'] = [area.get_coord() for area in areas if  area.get_coord() != []]
df['rights'] = np.where('property')

features_list = []

geo = {
    "type" : "FeatureCollection",
    "crs" : { "type" : "name",
              "properties" : {
                  "name" : "EPSG:4326"
                  }
              },
    "features" : None
    }

for x,y in df['geometry'].iteritems():
    if len(y) > 1:
        for i in y:
            feature = {
                    'type': 'Feature',
                    'id': x,
                    'geometry':
                    {'type': 'Polygon',
                    'coordinates': i},
                    'properties':
                    {"description": df['cn'].loc[x],
                    "fill": "#00f9ff",
                    "fill-opacity": 0.9,
                    "stroke": "#000000",
                    "stroke-width": "1",
                    "stroke-opacity": 0.5}}
            features_list.append(feature)
    if len(y) == 1:
        for i in y:
            feature = {
                    'type': 'Feature',
                    'id': x,
                    'geometry':
                    {'type': 'Polygon',
                    'coordinates': i},
                    'properties':
                    {"description": df['cn'].loc[x],
                    "fill": "#030056",
                    "fill-opacity": 0.9,
                    "stroke": "#000000",
                    "stroke-width": "1",
                    "stroke-opacity": 0.5}}
            features_list.append(feature)




geo['features'] = features_list
with open('result2.json', 'w') as fp:
    json.dump(geo, fp)
