Thanks guys, DirectionVector.to_track_quat('X', 'Z') did the trick very nicely!

#define direction
Vector=(1,1,1)
DirectionVector = mathutils.Vector(Vector) 
#apply rotation
bpy.context.object.rotation_mode = 'QUATERNION'
bpy.context.object.rotation_quaternion = DirectionVector.to_track_quat('Z','Y')
