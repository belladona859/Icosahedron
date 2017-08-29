Use the vertex co attribute.

MeshVertex.co

You may want to take the objects transformation into account, in this case you have to multiply it with the objects matrix.

This test script adds an empty at the first vertex location

# Assume we are in object mode and have a mesh object

import bpy
from bpy import context

obj = context.active_object
v = obj.data.vertices[0]

co_final = obj.matrix_world * v.co

# now we can view the location by applying it to an object
obj_empty = bpy.data.objects.new("Test", None)
context.scene.objects.link(obj_empty)
obj_empty.location = co_final
Another common operation is to get all vertex locations with the objects transform applied, in this case you can use list comprehension to get a list of transformed vertex locations...

coords = [(obj.matrix_world * v.co) for v in obj.data.vertices]
