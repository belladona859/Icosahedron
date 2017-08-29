Blender 2.6 Python Grouping Objects

Do this experiment with nothing selected. A scene with 3 objects : Cube1, Cube2, Cube3
>>> bpy.ops.group.create(name="myGroup")
{'FINISHED'} # will not appear in outliner yet.

>>> bpy.context.scene.objects['Cube1'].select = True
{'FINISHED'}

>>> bpy.ops.object.group_link(group="myGroup")
{'FINISHED'}

The result of the above code should be that the object becomes part of "myGroup" Now un-group it again, and un-select everything. If you want all of them added you could do:
import bpy

# # or if you want to select all mesh objects.
# objects_to_add = [obj.name for obj in bpy.data.objects if obj.type == 'MESH']

# I will populate a list in advance, the square brackets are optional here.
objects_to_add = ["Cube1", "Cube2", "Cube3"]
for name in objects_to_add:
    bpy.context.scene.objects[name].select = True
    bpy.ops.object.group_link(group="myGroup")    
    bpy.context.scene.objects[name].select = False
if myGroup didn't exist yet you would do:
import bpy

# not visible in outliner until objects are linked.
bpy.ops.group.create(name="myGroup") 

objects_to_add = "Cube1", "Cube2", "Cube3"
for name in objects_to_add:
    bpy.context.scene.objects[name].select = True
    bpy.ops.object.group_link(group="myGroup")    
    bpy.context.scene.objects[name].select = False
This version is probably the cleanest I can come up with for now. It contains a little bit more code that checks if the group exists yet.
import bpy

# extra checking, if myGroup doesn't already exist, create it.
# if you know your group doesn't exist, this is not needed.
# if you are unsure at runtime, then this makes sure you don't 
# create a myGroup.001 etc..
if not 'myGroup' in bpy.data.groups:
    bpy.ops.group.create(name="myGroup") 

# if you want to select all mesh objects.
objects_to_add = [obj.name for obj in bpy.data.objects if obj.type == 'MESH']

# this would populate a list in advance, the square brackets are optional here.
# objects_to_add = ["Cube1", "Cube2", "Cube3"]

scn = bpy.context.scene
for name in objects_to_add:
    scn.objects.active = scn.objects[name]
    bpy.ops.object.group_link(group="myGroup")    
  
Without bpy.ops
This example shows a way to insert items into a group without the use of bpy.ops and should be faster than the previous methods when applied to large object lists. You can verify in the outliner goups mode that they have indeed been added. Blender might not outline these objects with the grouped colour you would normally expect, this is a bug and should be easy to fix (if it hasn't already)
import bpy

# to test this, 
# 1) delete all objects from the scene
# 2) add a cube, circle and plane
obs_to_add = [ob for ob in bpy.data.objects if ob.type == 'MESH']

ng = bpy.data.groups.new("new_group")
ng
>>> bpy.data.groups['new_group']

ng.objects
>>> (empty)

# seems this way you can't append a list of objects, but consecutive links work
# hence the for-loop over obs_to_add
for ob in obs_to_add:
  ng.objects.link(ob)

ng.objects[:]
>>> [bpy.data.objects['Circle'], bpy.data.objects['Cube'], bpy.data.objects['Plane']]
