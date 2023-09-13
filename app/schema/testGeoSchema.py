from typing import Union,List
from ..model.test import Test
from ..utils import wkbToGeoJSON

class TestGeoSchema:
    def __init__(self,data:Union[Test,List[Test]]):
        self.data = data

    def parse(self):
        if not isinstance(self.data,list):
            return self.parseOne()
        else:
            return self.parseMany()

    def parseOne(self):
        return {
            "type": "Feature",
            "geometry": wkbToGeoJSON(self.data.geom),
            "properties": {
                "id": self.data.id,
                "name": self.data.name,
            }
        }

    def parseMany(self):
        print(len(self.data))
        objects = [{
            "type": "Feature",
            "geometry": wkbToGeoJSON(i.geom),
            "properties": {
                "id": i.id,
                "name": i.name,
            }
        } for i in self.data]
        return {
            "type": "FeatureCollection",
            "features": objects
        }