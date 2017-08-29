import bpy, mathutils

def blankoutdrawing():
    scene = bpy.data.scenes['Scene'];
    
    for obj in bpy.data.objects:
        scene.objects.unlink(obj);
        obj.user_clear();
        bpy.data.objects.remove(obj);

def makeMaterial(name, diffuse, specular, alpha):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = diffuse
    mat.diffuse_shader = 'LAMBERT' 
    mat.diffuse_intensity = 1.0 
    mat.specular_color = specular
    mat.specular_shader = 'COOKTORR'
    mat.specular_intensity = 0.5
    mat.alpha = alpha
    mat.ambient = 1
    return mat
 
def setMaterial(ob, mat):
    me = ob.data
    me.materials.append(mat)

#per opengl red book
def getvertices():

    X = .525731112119133606;
    Z = .850650808352039932;

    va_permutations = [
    (-X, 0.0, Z), (X, 0.0, Z), (-X, 0.0, -Z), (X, 0.0, -Z),    
    (0.0, Z, X), (0.0, Z, -X), (0.0, -Z, X), (0.0, -Z, -X),    
    (Z, X, 0.0), (-Z, X, 0.0), (Z, -X, 0.0), (-Z, -X, 0.0) 
    ]
    
    #return form1 Icososphere
    return va_permutations;

#per opengl redbook
def getindices():
    indices = [
    (0,4,1), (0,9,4), (9,5,4), (4,5,8), (4,8,1),    
    (8,10,1), (8,3,10), (5,3,8), (5,2,3), (2,7,3),    
    (7,10,3), (7,6,10), (7,11,6), (11,0,6), (0,1,6), 
    (6,1,10), (9,0,11), (9,11,2), (9,2,5), (7,2,11)
    ]
   
    return indices;    

def insertnodes(vertices,mat1,mat2,mat3):
    for i, v in enumerate(vertices[0:4]):
        bpy.ops.mesh.primitive_uv_sphere_add(
        segments=12,
        ring_count=6,
        size=noderadius,enter_editmode=False,
        location=(0, 0, 0));

        bpy.ops.object.mode_set(mode='EDIT', toggle=False);
        bpy.ops.mesh.select_all(action='SELECT');
        bpy.ops.transform.translate(value=(v[0],v[1],v[2]));
        bpy.ops.object.mode_set(mode='OBJECT', toggle=False);

        setMaterial(bpy.context.object, mat1);
        bpy.context.object.name = "node"+str(i+1).zfill(2);   

    for i,v in enumerate(vertices[4:8]):
        bpy.ops.mesh.primitive_uv_sphere_add(
        segments=12,
        ring_count=6,
        size=noderadius,enter_editmode=False,
        location=(0, 0, 0));

        bpy.ops.object.mode_set(mode='EDIT', toggle=False);
        bpy.ops.mesh.select_all(action='SELECT');
        bpy.ops.transform.translate(value=(v[0],v[1],v[2]));
        bpy.ops.object.mode_set(mode='OBJECT', toggle=False);

        setMaterial(bpy.context.object, mat2);
        bpy.context.object.name = "node"+str(i+5).zfill(2);   

    for i,v in enumerate(vertices[8:12]):
        bpy.ops.mesh.primitive_uv_sphere_add(
        segments=12,
        ring_count=6,
        size=noderadius,enter_editmode=False,
        location=(0, 0, 0));

        bpy.ops.object.mode_set(mode='EDIT', toggle=False);
        bpy.ops.mesh.select_all(action='SELECT');
        bpy.ops.transform.translate(value=(v[0],v[1],v[2]));
        bpy.ops.object.mode_set(mode='OBJECT', toggle=False);

        setMaterial(bpy.context.object, mat3);
        bpy.context.object.name = "node"+str(i+9).zfill(2);    

def insertplane(name,mat,vertices):
    mesh = bpy.data.meshes.new(name);
    object = bpy.data.objects.new(name, mesh);  
    bpy.context.scene.objects.link(object);
    mesh.from_pydata(vertices,[],[(0,1,3,2)]);
    mesh.update(calc_edges=True);
    setMaterial(object, mat);

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

def beveltri(name,v_poly,pathobj,rad):
    direction = mathutils.Vector( v_poly[0] ) - mathutils.Vector( v_poly[1] );
    bpy.ops.mesh.primitive_circle_add(vertices=16, radius=rad,
    location=(v_poly[0][0],v_poly[0][1],v_poly[0][2]));
    cobj = bpy.context.active_object;
    cobj.name = name;
    bpy.ops.object.convert(target='CURVE', keep_original=False);
    quat = direction.to_track_quat('-Z', 'Y');
    cobj.rotation_euler = quat.to_euler();
    pathobj.data.bevel_object = cobj;

def look_at(obj_camera, point):
    loc_camera = obj_camera.matrix_world.to_translation()

    direction = point - loc_camera
    # point the cameras '-Z' and use its 'Y' as up
    rot_quat = direction.to_track_quat('-Z', 'Y')

    # assume we're using euler rotation
    obj_camera.rotation_euler = rot_quat.to_euler()
    
mat_red = makeMaterial('Red', (1,0,0), (1,1,1), 1);
mat_green = makeMaterial('Green', (0,1,0), (1,1,1), 1);
mat_blue = makeMaterial('Blue', (0,0,1), (1,1,1), 1);
matsemi_red = makeMaterial('RedSemi', (1,0,0), (0.5,0.5,0), 0.5);
matsemi_green = makeMaterial('GreenSemi', (0,1,0), (0.5,0.5,0), 0.5);
matsemi_blue = makeMaterial('BlueSemi', (0,0,1), (0.5,0.5,0), 0.5);

noderadius=0.03;
tuberadius=0.01;


#START:::
blankoutdrawing();

bpy.ops.mesh.primitive_cube_add(radius=0.1,location=(0,0,0));

vertices = getvertices();
indices = getindices();

insertnodes(vertices,mat_red,mat_green,mat_blue);

#planes of permutation
v_plane1 = vertices[0:4];
v_plane2 = vertices[4:8];
v_plane3 = vertices[8:12];
insertplane("plane01",matsemi_red,v_plane1);
insertplane("plane02",matsemi_green,v_plane2);
insertplane("plane03",matsemi_blue,v_plane3);

for i,indice in enumerate(indices):
    name = "poly" +str(i+1).zfill(2);
    v_poly = [ vertices[indice[0] ], vertices[ indice[1] ], vertices[ indice[2] ], vertices[ indice[0] ]   ]
    insertpoly(name,v_poly);
    beveltri(str("circle")+str(i+1).zfill(2),v_poly,bpy.data.objects[name],tuberadius);


for i,indice in enumerate(indices): 
    mymesh = bpy.data.meshes.new("Face"+str(i+1).zfill(2))
    myobject = bpy.data.objects.new("Face"+str(i+1).zfill(2), mymesh)  
    setMaterial(myobject,matsemi_red);
    bpy.context.scene.objects.link(myobject)
    mymesh.from_pydata(vertices,[],indices)
    mymesh.update(calc_edges=True)

for object in bpy.data.objects:
    object.hide=True;

print("done...");


