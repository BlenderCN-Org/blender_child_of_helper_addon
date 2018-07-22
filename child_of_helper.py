
bl_info = {
    'name': 'Child Of Helper',
    'author': 'Pavel_Blend',
    'version': (0, 0, 0),
    'blender': (2, 79, 0),
    'location': '3D View > Toolshelf > Pose Tools Panel',
    'category': 'Animation'
}


import bpy


def snap_to_frame(context, frame_offset):
    object = context.object
    bone_name = object.data.bones.active.name
    pose_bone = object.pose.bones[bone_name]

    frame_current = context.scene.frame_current
    context.scene.frame_set(frame_current + frame_offset)
    preview_matrix = pose_bone.matrix.copy()
    context.scene.frame_set(frame_current)
    pose_bone.matrix = preview_matrix


class SnapToPreviewFrameOperator(bpy.types.Operator):
    bl_idname = 'anim.snap_to_preview_frame'
    bl_label = 'Snap to Preview Frame'

    def execute(self, context):
        snap_to_frame(context, -1)
        return{'FINISHED'}


class SnapToNextFrameOperator(bpy.types.Operator):
    bl_idname = 'anim.snap_to_next_frame'
    bl_label = 'Snap to Next Frame'

    def execute(self, context):
        snap_to_frame(context, 1)
        return{'FINISHED'}


def draw_function(self, context):
    layout = self.layout
    layout.label('Child Of Helper:')
    layout.operator('anim.snap_to_preview_frame')
    layout.operator('anim.snap_to_next_frame')


def register():
    bpy.utils.register_class(SnapToPreviewFrameOperator)
    bpy.utils.register_class(SnapToNextFrameOperator)
    bpy.types.VIEW3D_PT_tools_posemode.append(draw_function)


def unregister():
    bpy.types.VIEW3D_PT_tools_posemode.remove(draw_function)
    bpy.utils.unregister_class(SnapToNextFrameOperator)
    bpy.utils.unregister_class(SnapToPreviewFrameOperator)
