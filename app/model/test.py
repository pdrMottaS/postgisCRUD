from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geometry

from ..database import Base

class Test(Base):
    __tablename__ = "my_test"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    geom = Column(Geometry(geometry_type="POLYGON", srid=4326))
