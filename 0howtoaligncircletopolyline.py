import bpy, mathutils

def blankoutdrawing():
    scene = bpy.data.scenes['Scene'];
    
    for obj in bpy.data.objects:
        scene.objects.unlink(obj);
        obj.user_clear();
        bpy.data.objects.remove(obj);

def insertpoly(name,vertices):
    curveData = bpy.data.curves.new(name, type='CURVE')
    curveData.dimensions = '3D'
    curveData.resolution_u = 2

    polyline = curveData.splines.new('POLY')
    polyline.points.add(len(vertices)-1)
    for i, coord in enumerate(vertices):
        x,y,z = coord
        polyline.points[i].co = (x, y, z, 1)

    curveOB = bpy.data.objects.new(name, curveData)
    scn = bpy.context.scene
    scn.objects.link(curveOB)
    
blankoutdrawing();

#bpy.ops.mesh.primitive_circle_add(vertices=32, radius=1.0, 
#fill_type='NOTHING', calc_uvs=False, view_align=False, 
#enter_editmode=False, location=(0.0, 0.0, 0.0), 
#rotation=(0.0, 0.0, 0.0), 
#layers=(False, False, False, False, False, False, False, False, False,
# False, False, False, False, False, False, False, False, False, False, False))

#bpy.ops.mesh.primitive_circle_add(vertices=32, radius=1, enter_editmode=False,location=(0.0,0.0,0.0))
obj = bpy.ops.mesh.primitive_circle_add(vertices=32, radius=1, enter_editmode=False,location=(0.0,0.0,0.0))

direction = mathutils.Vector((0,0,0)) - mathutils.Vector((2,2,2));

quat = direction.to_track_quat('-Z', 'Y');

bpy.data.objects["Circle"].rotation_euler = quat.to_euler();

v = [(0,0,0),(2,2,2)];

insertpoly("poly1",v);