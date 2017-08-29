import bpy

def vecCircle(name, verts, obj_type='MESH'):
    bpy.ops.mesh.primitive_circle_add(vertices=verts)
    obj = bpy.context.active_object
    obj.name = name
    if obj_type == 'CURVE':
        bpy.ops.object.convert(target='CURVE', keep_original=False)
    return obj

tor0refCirc = vecCircle("tor0refCirc", 6, 'CURVE')

beziers = [o for o in bpy.data.objects if o.type == 'CURVE']

for circleObj in beziers:
    circleName = circleObj.name
    circleObj.data.bevel_object = tor0refCirc
