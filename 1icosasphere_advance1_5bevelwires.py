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

def beveltri(name,v_poly,pathobj):
    direction = mathutils.Vector( v_poly[0] ) - mathutils.Vector( v_poly[1] );
    bpy.ops.mesh.primitive_circle_add(vertices=16, radius=.05,
    location=(v_poly[0][0],v_poly[0][1],v_poly[0][2]));
    cobj = bpy.context.active_object;
    cobj.name = name;
    bpy.ops.object.convert(target='CURVE', keep_original=False);
    quat = direction.to_track_quat('-Z', 'Y');
    cobj.rotation_euler = quat.to_euler();
    pathobj.data.bevel_object = cobj;

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

#planes of permutation
v_plane1 = vertices[0:4];
v_plane2 = vertices[4:8];
v_plane3 = vertices[8:12];
insertplane("plane01",matsemi_red,v_plane1);
insertplane("plane02",matsemi_green,v_plane2);
insertplane("plane03",matsemi_blue,v_plane3);

#bevling for each face one is missing I believe
v_poly01 = [vertices[0],vertices[3],vertices[8],vertices[0]]
insertpoly("poly01",v_poly01);
beveltri("poly01circle",v_poly01,bpy.data.objects["poly01"]);

v_poly02 = [vertices[0],vertices[3],vertices[9],vertices[0]]
insertpoly("poly02",v_poly02);
beveltri("poly02circle",v_poly02,bpy.data.objects["poly02"]);

v_poly03 = [vertices[3],vertices[8],vertices[5],vertices[3]]
insertpoly("poly03",v_poly03);
beveltri("poly03circle",v_poly03,bpy.data.objects["poly03"]);

v_poly04 = [vertices[0],vertices[8],vertices[4],vertices[0]]
insertpoly("poly04",v_poly04);
beveltri("poly04circle",v_poly04,bpy.data.objects["poly04"]);

v_poly05 = [vertices[0],vertices[4],vertices[7],vertices[0]]
insertpoly("poly05",v_poly05);
beveltri("poly05circle",v_poly05,bpy.data.objects["poly05"]);

v_poly06 = [vertices[9],vertices[0],vertices[7],vertices[9]]
insertpoly("poly06",v_poly06);
beveltri("poly06circle",v_poly06,bpy.data.objects["poly06"]);

v_poly07 = [vertices[3],vertices[9],vertices[6],vertices[3]]
insertpoly("poly07",v_poly07);
beveltri("poly07circle",v_poly07,bpy.data.objects["poly07"]);

v_poly08 = [vertices[5],vertices[3],vertices[6],vertices[5]]
insertpoly("poly08",v_poly08);
beveltri("poly08circle",v_poly08,bpy.data.objects["poly08"]);

v_poly09 = [vertices[8],vertices[5],vertices[11],vertices[8]]
insertpoly("poly09",v_poly09);
beveltri("poly09circle",v_poly09,bpy.data.objects["poly09"]);

v_poly10 = [vertices[8],vertices[4],vertices[11],vertices[8]]
insertpoly("poly10",v_poly10);
beveltri("poly10circle",v_poly10,bpy.data.objects["poly10"]);

v_poly11 = [vertices[7],vertices[4],vertices[1],vertices[7]]
insertpoly("poly11",v_poly11);
beveltri("poly11circle",v_poly11,bpy.data.objects["poly11"]);

v_poly12 = [vertices[9],vertices[7],vertices[10],vertices[9]]
insertpoly("poly12",v_poly12);
beveltri("poly12circle",v_poly12,bpy.data.objects["poly12"]);


v_poly13 = [vertices[6],vertices[9],vertices[10],vertices[6]]
insertpoly("poly13",v_poly13);
beveltri("poly13circle",v_poly13,bpy.data.objects["poly13"]);

v_poly14 = [vertices[5],vertices[6],vertices[2],vertices[5]]
insertpoly("poly14",v_poly14);
beveltri("poly14circle",v_poly14,bpy.data.objects["poly14"]);

v_poly15 = [vertices[11],vertices[5],vertices[2],vertices[11]]
insertpoly("poly15",v_poly15);
beveltri("poly15circle",v_poly15,bpy.data.objects["poly15"]);

v_poly16 = [vertices[11],vertices[4],vertices[1],vertices[11]]
insertpoly("poly16",v_poly16);
beveltri("poly16circle",v_poly16,bpy.data.objects["poly16"]);

v_poly17 = [vertices[11],vertices[2],vertices[1],vertices[11]]
insertpoly("poly17",v_poly17);
beveltri("poly17circle",v_poly17,bpy.data.objects["poly17"]);

v_poly18 = [vertices[7],vertices[10],vertices[1],vertices[7]]
insertpoly("poly18",v_poly18);
beveltri("poly18circle",v_poly18,bpy.data.objects["poly18"]);

v_poly19 = [vertices[10],vertices[1],vertices[2],vertices[10]]
insertpoly("poly19",v_poly19);
beveltri("poly19circle",v_poly19,bpy.data.objects["poly19"]);

print("done...");


