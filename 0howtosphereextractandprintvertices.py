import bpy

obj = context.active_object

coords = [(obj.matrix_world * v.co) for v in obj.data.vertices]

print( str( coords ) )

