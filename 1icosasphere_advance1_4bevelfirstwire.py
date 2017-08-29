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

def getvertices():
    goldenratio = (1+2.23606797749979)/2

    va_permutations = [
			#(0, ±1, ±φ) permutation1
			(0.0,  1.0,  goldenratio),
			(0.0,  1.0,  -goldenratio),
			(0.0,  -1.0,  -goldenratio),
			(0.0,  -1.0,  goldenratio),

			#(±1, ±φ, 0) permutation 2
			(1.0,goldenratio,0.0),
			(1.0,-goldenratio,0.0),
			(-1.0,-goldenratio,0.0),
			(-1.0,goldenratio,0.0),

			#(±φ, 0, ±1) permutation 3
			(goldenratio,0,1.0),
			(-goldenratio,0,1.0),
			(-goldenratio,0,-1.0),
			(goldenratio,0,-1.0)
    ]
    
    #return form1 Icososphere
    return va_permutations;

def insertnodes(vertices,mat1,mat2,mat3):
    for i, v in enumerate(vertices[0:4]):
        bpy.ops.mesh.primitive_uv_sphere_add(
        segments=12,
        ring_count=6,
        size=.1,enter_editmode=False,
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
        size=.1,enter_editmode=False,
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
        size=.1,enter_editmode=False,
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
    mesh.from_pydata(vertices,[],[(0,1,2,3)]);
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

mat_red = makeMaterial('Red', (1,0,0), (1,1,1), 1);
mat_green = makeMaterial('Green', (0,1,0), (1,1,1), 1);
mat_blue = makeMaterial('Blue', (0,0,1), (1,1,1), 1);
matsemi_red = makeMaterial('RedSemi', (1,0,0), (0.5,0.5,0), 0.5);
matsemi_green = makeMaterial('GreenSemi', (0,1,0), (0.5,0.5,0), 0.5);
matsemi_blue = makeMaterial('BlueSemi', (0,0,1), (0.5,0.5,0), 0.5);




#START:::
blankoutdrawing();

vertices = getvertices();

print("VERTICES: ",vertices);

insertnodes(vertices,mat_red,mat_green,mat_blue);

v_plane1 = vertices[0:4];
v_plane2 = vertices[4:8];
v_plane3 = vertices[8:12];
insertplane("plane01",matsemi_red,v_plane1);
insertplane("plane02",matsemi_green,v_plane2);
insertplane("plane03",matsemi_blue,v_plane3);

v_poly1 = [vertices[0],vertices[3],vertices[8],vertices[0]]
#v_poly2 = [vertices[0],vertices[3],vertices[9],vertices[0]]
#v_poly3 = [vertices[3],vertices[8],vertices[5],vertices[3]]
#v_poly4 = [vertices[0],vertices[8],vertices[4],vertices[0]]
#v_poly5 = [vertices[0],vertices[4],vertices[7],vertices[0]]
#v_poly6 = [vertices[9],vertices[0],vertices[7],vertices[0]]
#v_poly7 = [vertices[3],vertices[9],vertices[6],vertices[3]]
#v_poly8 = [vertices[5],vertices[3],vertices[6],vertices[5]]

insertpoly("poly01",v_poly1);
#insertpoly("poly2",v_poly2);
#insertpoly("poly3",v_poly3);
#insertpoly("poly4",v_poly4);
#insertpoly("poly5",v_poly5);
#insertpoly("poly6",v_poly6);
#insertpoly("poly7",v_poly7);
#insertpoly("poly8",v_poly8);

direction = mathutils.Vector( v_poly1[0] ) - mathutils.Vector( v_poly1[1] );

bpy.ops.mesh.primitive_circle_add(vertices=16, radius=.05,
location=(v_poly1[0][0],v_poly1[0][1],v_poly1[0][2]));

cobj = bpy.context.active_object;

cobj.name = "poly01circle";

bpy.ops.object.convert(target='CURVE', keep_original=False);

quat = direction.to_track_quat('-Z', 'Y');

cobj.rotation_euler = quat.to_euler();

bpy.data.objects["poly01"].data.bevel_object = cobj;

print("done...");


