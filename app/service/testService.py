from ..model.test import Test
from ..schema.testGeoSchema import TestGeoSchema
from ..schema.testSchema import PostTestSchema
from ..database import SessionLocal
from ..utils import arrayToWkt

def index_test():
    db = SessionLocal()
    result = db.query(Test).all()
    db.close()
    return TestGeoSchema(result).parse()

def get_test(id:int):
    db = SessionLocal()
    result = db.query(Test).where(Test.id==id).first()
    db.close()
    if result is None:
        raise Exception()
    return TestGeoSchema(result).parse()

def create_test(test:PostTestSchema):
    db_test = Test()
    db_test.name = test.name
    db_test.geom = "POLYGON"+arrayToWkt(test.coordinates)

    db = SessionLocal()
    db.add(db_test)
    db.commit()
    db.refresh(db_test)
    db.close()
    return TestGeoSchema(db_test).parse()