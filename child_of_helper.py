
import bpy


object = bpy.context.object
bone_name = object.data.bones.active.name
pose_bone = object.pose.bones[bone_name]
active_child_of_constraints = []

for constraint in pose_bone.constraints:
    if constraint.type != 'CHILD_OF':
        continue
    if constraint.influence != 1.0:
        continue
    active_child_of_constraints.append(constraint)

child_of_count = len(active_child_of_constraints)

if child_of_count == 1:
    child_of_constarint = active_child_of_constraints[0]
    transposed_matrix = child_of_constarint.inverse_matrix.transposed()
    translation_vector = child_of_constarint.inverse_matrix.to_translation()
    translation_matrix = child_of_constarint.inverse_matrix.Translation(translation_vector)
    pose_bone.matrix = transposed_matrix * translation_matrix.inverted()
