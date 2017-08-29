import bpy
import math

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
    
def init_blank():
    scene = bpy.data.scenes['Scene'];
    
    for obj in bpy.data.objects:
        scene.objects.unlink(obj);
        obj.user_clear();
        bpy.data.objects.remove(obj);

init_blank();

#materials
mat_red = makeMaterial('Red', (1,0,0), (1,1,1), 1)
mat_green = makeMaterial('Green', (0,1,0), (1,1,1), 1)
mat_blue = makeMaterial('Blue', (0,0,1), (1,1,1), 1)
matsemi_red = makeMaterial('RedSemi', (1,0,0), (0.5,0.5,0), 0.5)
matsemi_green = makeMaterial('GreenSemi', (0,1,0), (0.5,0.5,0), 0.5)
matsemi_blue = makeMaterial('BlueSemi', (0,0,1), (0.5,0.5,0), 0.5)

goldenratio = (1+2.23606797749979)/2

va_permutations = [#form1 Icososphere
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
			(goldenratio,0,-1.0)]

va_nodenames = ['node01','node02','node03','node04','node05','node06',
'node07','node08','node09','node10','node11','node12']

nodecount = 0;

for v in va_permutations[0:4]:
    bpy.ops.mesh.primitive_uv_sphere_add(
    segments=12,
    ring_count=6,
    size=.1,enter_editmode=False,
    location=(0, 0, 0));

    bpy.ops.object.mode_set(mode='EDIT', toggle=False);
    bpy.ops.mesh.select_all(action='SELECT');
    bpy.ops.transform.translate(value=(v[0],v[1],v[2]));
    bpy.ops.object.mode_set(mode='OBJECT', toggle=False);

    setMaterial(bpy.context.object, mat_red);
    bpy.context.object.name = va_nodenames[nodecount]    
    nodecount=nodecount+1;

for v in va_permutations[4:8]:
    bpy.ops.mesh.primitive_uv_sphere_add(
    segments=12,
    ring_count=6,
    size=.1,enter_editmode=False,
    location=(0, 0, 0));

    bpy.ops.object.mode_set(mode='EDIT', toggle=False);
    bpy.ops.mesh.select_all(action='SELECT');
    bpy.ops.transform.translate(value=(v[0],v[1],v[2]));
    bpy.ops.object.mode_set(mode='OBJECT', toggle=False);

    setMaterial(bpy.context.object, mat_green);
    bpy.context.object.name = va_nodenames[nodecount]    
    nodecount=nodecount+1;

for v in va_permutations[8:12]:
    bpy.ops.mesh.primitive_uv_sphere_add(
    segments=12,
    ring_count=6,
    size=.1,enter_editmode=False,
    location=(0, 0, 0));

    bpy.ops.object.mode_set(mode='EDIT', toggle=False);
    bpy.ops.mesh.select_all(action='SELECT');
    bpy.ops.transform.translate(value=(v[0],v[1],v[2]));
    bpy.ops.object.mode_set(mode='OBJECT', toggle=False);

    setMaterial(bpy.context.object, mat_blue);
    bpy.context.object.name = va_nodenames[nodecount]    
    nodecount=nodecount+1;

va_plane1 = [#form1 Icososphere
			#(0, ±1, ±φ) permutation1
			(0.0,  1.0,  goldenratio),
			(0.0,  1.0,  -goldenratio),
			(0.0,  -1.0,  -goldenratio),
			(0.0,  -1.0,  goldenratio)]
va_plane2 = [			#(±1, ±φ, 0) permutation 2
			(1.0,goldenratio,0.0),
			(1.0,-goldenratio,0.0),
			(-1.0,-goldenratio,0.0),
			(-1.0,goldenratio,0.0)]
va_plane3 = 			[#(±φ, 0, ±1) permutation 3
			(goldenratio,0,1.0),
			(-goldenratio,0,1.0),
			(-goldenratio,0,-1.0),
			(goldenratio,0,-1.0)]
fa_plane = [(0,1,2,3)]
 

meshplane1 = bpy.data.meshes.new("Plane");
planeobject1 = bpy.data.objects.new("Plane1", meshplane1);  
bpy.context.scene.objects.link(planeobject1);
meshplane1.from_pydata(va_plane1,[],fa_plane);
meshplane1.update(calc_edges=True);
setMaterial(planeobject1, matsemi_red);

meshplane2 = bpy.data.meshes.new("Plane");
planeobject2 = bpy.data.objects.new("Plane2", meshplane2);  
bpy.context.scene.objects.link(planeobject2);
meshplane2.from_pydata(va_plane2,[],fa_plane);
meshplane2.update(calc_edges=True);
setMaterial(planeobject2, matsemi_red);

meshplane3 = bpy.data.meshes.new("Plane");
planeobject3 = bpy.data.objects.new("Plane3", meshplane3);  
bpy.context.scene.objects.link(planeobject3);
meshplane3.from_pydata(va_plane3,[],fa_plane);
meshplane3.update(calc_edges=True);
setMaterial(planeobject3, matsemi_blue);


#------DONE---------#
print("done...")
#~~~~~~~~~~~~~~~~~~~#

