session.journalOptions.setValues(replayGeometry=COORDINATE,recoverGeometry=COORDINATE)
from math import *
from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()

a = mdb.models['Model-1'].rootAssembly
n1,n2 = a.sets["Set-100"].nodes,a.sets["Set-200"].nodes
for i in n1:
    for j in n2:
        xd,yd,zd=i.coordinates[0]-j.coordinates[0],i.coordinates[1]-j.coordinates[1],i.coordinates[2]-j.coordinates[2]
        if pow((xd**2.0+yd**2.0+zd**2.0),0.5)==5:
            a.WirePolyLine(points=((i, j),), mergeType=IMPRINT, meshable=OFF)

ok