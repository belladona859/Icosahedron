from math import pi
import bpy

obj = bpy.data.objects['my_obj']
# go into edit mode
bpy.context.scene.objects.active = obj
bpy.ops.object.mode_set(mode='EDIT', toggle=False)
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.transform.rotate(value=pi/2, axis=(False, False, True))
bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

#bpy.ops.transform.translate(value=(0.0, 0.0, 0.0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), gpencil_strokes=False, texture_space=False, remove_on_cancel=False, release_confirm=False, use_accurate=False)

