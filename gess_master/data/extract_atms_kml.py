# Download kml from https://export.hotosm.org/en/v3/
from pykml import parser
from os import path
with open('/Users/Robin/Downloads/yorkshire_planet_osm_point_points.kml') as f:
    folder = parser.parse(f).getroot().Document.Folder

for p in folder.Placemark:
    coord=p.Point.coordinates
    try:
        atm_name=p.ExtendedData.SchemaData.SimpleData[2]
    except:
        atm_name='ATM : %s' % p.ExtendedData.SchemaData.SimpleData[0]

    print('%s,"%s"' % (coord, atm_name))
