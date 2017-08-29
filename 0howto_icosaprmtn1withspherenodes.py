#form1 Icososphere

#(0, ±1, ±φ)
#(±1, ±φ, 0)
#(±φ, 0, ±1)

import bpy
import math

goldenratio = (1+2.23606797749979)/2
count = 0;
permutations = []

v_prmtn1 = [
	(0,1.0,goldenratio),
	(0,1.0,-goldenratio),
	(0,-1.0,-goldenratio),
	(0,-1.0,goldenratio)
	]

f_prmtn1 = [(0,1,2,3)]

#Define mesh and object variables
icosomesh = bpy.data.meshes.new("Icoso")
icosoobj = bpy.data.objects.new("Icoso", icosomesh)  

#Set location and scene of object
icosoobj.location = bpy.context.scene.cursor_location
bpy.context.scene.objects.link(icosoobj)

#Catalog prmtn1 by adding objects to the scene that describe it
icosomesh.from_pydata(v_prmtn1,[],f_prmtn1)
icosomesh.update(calc_edges=True)

bpy.ops.mesh.primitive_uv_sphere_add(
segments=12,
ring_count=6,
size=.1,enter_editmode=True,
location=(v_prmtn1[0][0], v_prmtn1[0][1], v_prmtn1[0][2]))

bpy.ops.mesh.primitive_uv_sphere_add(
segments=12,
ring_count=6,
size=.1,enter_editmode=True,
location=(v_prmtn1[1][0], v_prmtn1[1][1], v_prmtn1[1][2]))

bpy.ops.mesh.primitive_uv_sphere_add(
segments=12,
ring_count=6,
size=.1,enter_editmode=True,
location=(v_prmtn1[2][0], v_prmtn1[2][1], v_prmtn1[2][2]))

bpy.ops.mesh.primitive_uv_sphere_add(
segments=12,
ring_count=6,
size=.1,enter_editmode=True,
location=(v_prmtn1[3][0], v_prmtn1[3][1], v_prmtn1[3][2]))


#------DONE---------#
print("done...")
#~~~~~~~~~~~~~~~~~~~#

