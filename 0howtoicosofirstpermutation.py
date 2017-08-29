#blender --python ~/Desktop/bcreate_icosohedron_objgp.py
#form1 of icoso
#(0, ±1, ±φ)
#(±1, ±φ, 0)
#(±φ, 0, ±1)
import bpy
import math

goldenratio = (1+2.23606797749979)/2

count = 0;

permutations = []

verts = [(0,1.0,goldenratio),
(0,1.0,-goldenratio),
(0,-1.0,-goldenratio),
(0,-1.0,goldenratio)]

faces = [(0,1,2,3)]

#Define mesh and object variables
mymesh = bpy.data.meshes.new("Icoso")
myobject = bpy.data.objects.new("Icoso", mymesh)  

#Set location and scene of object
myobject.location = bpy.context.scene.cursor_location
bpy.context.scene.objects.link(myobject)

#Create mesh
mymesh.from_pydata(verts,[],faces)
mymesh.update(calc_edges=True)

print("done...")
