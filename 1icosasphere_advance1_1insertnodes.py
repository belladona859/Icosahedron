#TODO:
#After all that is displayed connect the nodes with cylinders and use a couple
#of cylinders and a cone to make arrows from the origin that will be used to denote
#changeable vectors that will move like a clock with each iteration of the subdivision
#process. The sudbivision process is described in glprogramming.com/red GL red book Chapter2
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

f_permutations = [(0,1,2,3),(4,5,6,7),(8,9,10,11),(12,13,14,15)]

for v in va_permutations[0:4]:
    bpy.ops.mesh.primitive_uv_sphere_add(
    segments=12,
    ring_count=6,
    size=.1,enter_editmode=False,
    location=(v[0], v[1], v[2]));

    setMaterial(bpy.context.object, mat_red);

for v in va_permutations[4:8]:
    bpy.ops.mesh.primitive_uv_sphere_add(
    segments=12,
    ring_count=6,
    size=.1,enter_editmode=False,
    location=(v[0], v[1], v[2]));

    setMaterial(bpy.context.object, mat_green);

for v in va_permutations[8:12]:
    bpy.ops.mesh.primitive_uv_sphere_add(
    segments=12,
    ring_count=6,
    size=.1,enter_editmode=False,
    location=(v[0], v[1], v[2]));

    setMaterial(bpy.context.object, mat_blue);

#------DONE---------#
print("done...")
#~~~~~~~~~~~~~~~~~~~#

