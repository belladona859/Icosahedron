import bpy

# Go to edit mode, face selection mode and select all faces
bpy.ops.object.mode_set( mode   = 'EDIT'   )
bpy.ops.mesh.select_mode( type  = 'FACE'   )
bpy.ops.mesh.select_all( action = 'SELECT' )

bpy.ops.mesh.extrude_region_move(
    TRANSFORM_OT_translate={"value":(0, 0, 3)}
)

bpy.ops.object.mode_set( mode = 'OBJECT' )
