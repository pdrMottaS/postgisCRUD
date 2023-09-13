import shapely.geometry
from geoalchemy2.shape import to_shape
from typing import List

def wkbToGeoJSON(wkb):
    return shapely.geometry.mapping(to_shape(wkb))

def arrayToWkt(l:List[List[float]]):
    coordinates = []
    for i in l:
        coordinates.append(str(i[0])+" "+str(i[1]))
    return "(("+",".join(coordinates)+"))"