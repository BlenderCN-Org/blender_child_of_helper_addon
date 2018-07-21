
import bpy


object = bpy.context.object
bone_name = object.data.bones.active.name
pose_bone = object.pose.bones[bone_name]

frame_current = bpy.context.scene.frame_current
bpy.context.scene.frame_set(frame_current - 1)
preview_matrix = pose_bone.matrix.copy()
bpy.context.scene.frame_set(frame_current)
pose_bone.matrix = preview_matrix
