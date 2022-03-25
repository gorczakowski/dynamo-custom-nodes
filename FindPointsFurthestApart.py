# Created by Krzysztof Gorczakowski, 2022
# https://github.com/gorczakowski

import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
import math

points = IN[0]

def dist(A, B):
	return math.sqrt((A.X - B.X)**2 + (A.Y - B.Y)**2)

max_dist = 0
point1, point2 = None, None

for i, pt in enumerate(points[:-1]):
	for pt2 in points[i+1:]:
		if dist(pt, pt2) > max_dist:
			max_dist = dist(pt, pt2)
			point1 = pt
			point2 = pt2

OUT = point1, point2