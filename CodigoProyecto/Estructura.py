from typing import List
from pydantic import BaseModel
#.
class XYData(BaseModel):
    x: List[float]
    y: List[float]
    z: List[float]
    xName: str
    yName: str
    zName: str
