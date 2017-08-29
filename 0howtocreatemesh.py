import bpy
 
#Define vertices and faces
verts = [(0,0,0),(0,5,0),(5,5,0),(5,0,0)]
faces = [(0,1,2,3)]
 
# Define mesh and object variables
mymesh = bpy.data.meshes.new("Plane")
myobject = bpy.data.objects.new("Plane", mymesh)  
 
#Set location and scene of object
myobject.location = bpy.context.scene.cursor_location
bpy.context.scene.objects.link(myobject)
 
#Create mesh
mymesh.from_pydata(verts,[],faces)
mymesh.update(calc_edges=True)