"""
    # Blender 3.x.x
    # Run script inside Blender and select .vbx file
"""

import os
import bpy
from bpy_extras.io_utils import ImportHelper


class IMPORT_VBX(bpy.types.Operator, ImportHelper):
    bl_idname = 'voxelbuilder.import_vbx'
    bl_label = 'Import From Voxel Builder (.vbx)'
    bl_options = {'PRESET', 'UNDO'}
    filename_ext = '.vbx'
    filter_glob: bpy.props.StringProperty(default='*.vbx', options={'HIDDEN'})
    def execute(self, context):
        create(self.filepath)
        return {'FINISHED'}


def readFile(path):
    arr = []
    if os.path.isfile(path):
        with open(path, "r") as f:
            data = f.read().splitlines()
            for line in data:
                if line.startswith('voxels='):
                    line = line.split('=')[1]
                    arr = line.split(';')[:-1]
    return arr


def create(filePath):
    col = bpy.data.collections.new("Voxels") # create collection(group)
    bpy.context.scene.collection.children.link(col)

    bpy.ops.mesh.primitive_cube_add(size=1) # create original cube
    cube = bpy.context.active_object

    data = readFile(filePath)

    # find unique colors to create materials
    uniqueColors = []
    for voxel in data:
        hex = voxel.split(',')[3]
        if hex not in uniqueColors:
            uniqueColors.append(hex)

    materials = []
    for hex in uniqueColors:
        rgb = tuple(int(hex[i:i + 2], 16) / 255. for i in (1, 3, 5))
        mat = bpy.data.materials.new("voxel_%s" %(hex))
        mat.use_nodes = True
        principled = mat.node_tree.nodes['Principled BSDF']
        principled.inputs['Base Color'].default_value = (rgb[0],rgb[1],rgb[2],1)
        materials.append(mat)

    # recreation
    for voxel in data:
        x = float(voxel.split(',')[0])
        y = float(voxel.split(',')[1])
        z = float(voxel.split(',')[2])
        hex = voxel.split(',')[3]

        # instance original cube
        copy = cube.data.copy()
        obj = bpy.data.objects.new("voxel", copy)
        obj.location = (-x, z, y + 0.5)

        # apply related material
        for mat in materials:
            if mat.name.split('.')[0] == "voxel_%s"%(hex): # compare names
                obj.data.materials.append(mat)

        # add to collection
        bpy.data.collections["Voxels"].objects.link(obj)

    # delete original cube    
    bpy.ops.object.delete()


def register():
    bpy.utils.register_class(IMPORT_VBX)


def unregister():
    bpy.utils.unregister_class(IMPORT_VBX)


if __name__ == "__main__":
    register()
    bpy.ops.voxelbuilder.import_vbx('INVOKE_DEFAULT')
