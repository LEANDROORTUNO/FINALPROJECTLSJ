from pathlib import Path
import csv
from typing import List
from CodigoProyecto.Estructura import XYData
#.

def read(csv_path: Path) -> XYData:
    xs: List[float] = []
    ys: List[float] = []
    zs: List[float] = []
    xName = "X"
    yName = "Y"
    zName = "Z"

    with csv_path.open(newline="", encoding="utf-8") as f:
        r = csv.reader(f)  # default delimiter=','
        # header 
        header = next(r, None)
        if header and len(header) >= 2:
            xName = (header[0] or "X").strip() or "X"
            yName = (header[1] or "Y").strip() or "Y"
            zName = (header[2] or "Z").strip() or "Z"

        # data rows
        for row in r:
            if len(row) <= 2:
                continue
            sx = (row[0] or "").strip()
            sy = (row[1] or "").strip()
            sz = (row[2] or "").strip()
            if not sx or not sy or not sz:
                continue
            try:
                xs.append(float(sx))
                ys.append(float(sy))
                zs.append(float(sz))
            except ValueError:
                # skip malformed line
                continue

    return XYData(x=xs, y=ys, z=zs, xName=xName, yName=yName, zName=zName)
