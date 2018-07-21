
bl_info = {
    'name': 'Child Of Helper',
    'author': 'Pavel_Blend',
    'version': (0, 0, 0),
    'blender': (2, 79, 0),
    'location': '3D View > Toolshelf (in Pose Mode)',
    'category': 'Animation'
}


import bpy


class ChildOfHelperOperator(bpy.types.Operator):
    bl_idname = 'anim.child_of_helper'
    bl_label = 'Snap to Preview Frame'

    def execute(self, context):
        object = context.object
        bone_name = object.data.bones.active.name
        pose_bone = object.pose.bones[bone_name]

        frame_current = context.scene.frame_current
        bpy.context.scene.frame_set(frame_current - 1)
        preview_matrix = pose_bone.matrix.copy()
        bpy.context.scene.frame_set(frame_current)
        pose_bone.matrix = preview_matrix

        return{'FINISHED'}


def draw_function(self, context):
    layout = self.layout
    layout.label('Child Of Helper:')
    layout.operator('anim.child_of_helper')


def register():
    bpy.utils.register_class(ChildOfHelperOperator)
    bpy.types.VIEW3D_PT_tools_posemode.append(draw_function)


def unregister():
    bpy.types.VIEW3D_PT_tools_posemode.remove(draw_function)
    bpy.utils.unregister_class(ChildOfHelperOperator)
