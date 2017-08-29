#bpy.ops.mesh.primitive_uv_sphere_add()
#See ops documentation. We are going to use this command
#to insert a small sphere at each node of the icosohedrons permutations
# bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, size=1.0, calc_uvs=False, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, # 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
#Construct a UV sphere mesh

#Parameters:	
#segments (int in [3, 100000], (optional)) – Segments
#ring_count (int in [3, 100000], (optional)) – Rings
#size (float in [0, inf], (optional)) – Size
#calc_uvs (boolean, (optional)) – Generate UVs, Generate a default UV map
#view_align (boolean, (optional)) – Align to View, Align the new object to the view
#enter_editmode (boolean, (optional)) – Enter Editmode, Enter editmode when adding this object
#location (float array of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object
#rotation (float array of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object
#layers (boolean array of 20 items, (optional)) – Layer


#Operator reports
#Once an operator has been executed, it leaves a trail in the report window in Scripting screen 

#  bpy.ops.mesh.primitive_uv_sphere_add(segments=32, rings=16,
#  size=1, view_align=False, enter_editmode=False,
#  location=(0, 0, 0), rotation=(0, 0, 0), layer=(True, False, False,
#  False, False, False, False, False, False, False, False, False, False,
#  False, False, False, False, False, False, False))

#When we add an UV sphere from the menu, it always has 32 segments, 16 rings, etc. But it is straightforward to figure out wich call we need to make a sphere with other #data, e.g. 12 segments, 6 rings, radius 3, and centered at (1, 1, 1): 

#  bpy.ops.mesh.primitive_uv_sphere_add(
#  segments=12,
#  rings=6,
#  size=3,enter_editmode=True,
#  location=(1, 1, 1))


bpy.ops.mesh.primitive_uv_sphere_add(
segments=12,
ring_count=6,
size=3,enter_editmode=True,
location=(0, 0, 0))

print("done...")

