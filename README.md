# Voxel Builder

![banner](media/banner.jpg?raw=true "banner")

### **Voxel-based 3D modeling application**

Version **4.0.1 RC 2023** *(Babylon.js 6.0.0)*

[ [Try now](https://nimadez.github.io/voxel-builder) ] [ [ Download ](https://github.com/nimadez/voxel-builder#desktop-installation) ] [ [Changelog](https://github.com/nimadez/voxel-builder/blob/main/CHANGELOG) ]

## Features

⚡ File I/O
- Save and load custom VBX format
- Load from MagicaVoxel
- Export to GLB, render to pixel perfect PNG
- Quick save and quick load, undo/redo
- 4 permanent local storages with image preview
- Load HDRI and import textures
- Import 3D models and 2D images for voxelization
- Support file drag-and-drop *(VBX, VOX, OBJ, GLB, HDR, PNG, JPG, SVG)*
- [Blender importer script](https://github.com/nimadez/voxel-builder/blob/main/scripts/blender-importer.py) for VBX files *(get exact copy in Blender)*

⚡ Model and Paint
- Terrain, cube, plane, sphere, ellipsoid, random, isometric generators
- OBJ and GLB voxelization
- Image voxelization *(JPG, PNG, SVG)*
- Interactive modeling toolsets
- Drawing and painting in freeform and box shape
- Symmetric drawing and painting, symmetrize and mirror
- Transformable workplane to draw anywhere in the space

⚡ Mesh Bakery
- Bake voxel particles to a clean mesh
- Clone, instance, merge, transform bakes and parts
- UVs, PBR material and texture setup
- PBR material data exported to GLB
- Ready for 3D printing *(watertight no holes)*

⚡ Rendering
- Basic PBR rendering, HDRI lighting, and post-process settings
- WASD controls on desktop, joystick controls on touchscreen

⚡ More
- Built-in documentation
- Clean handcrafted intelligent user-interface
- Single HTML file, minimum dependency
- Ad-free, no miners and trackers, no logging

## Supported Browsers
- Electron *(recommended)*
- Google Chrome for desktop
- Google Chrome for mobile devices
<br><sub>* *Tablet recommended for best experience*</sub>
<br><sub>* *PWA A2HS-ready (add to home screen)*</sub>

## Desktop Installation
✅ [Download and run](https://github.com/nimadez/voxel-builder/blob/main/scripts/voxel-builder.py) portable Python installer, even on USB!
```
curl -o voxel-builder.py https://raw.githubusercontent.com/nimadez/voxel-builder/main/scripts/voxel-builder.py
```
** Voxel Builder runs offline on desktop (except for the Extras and HDRI samples), remember to run Python script regularly to get the latest update.

[ Manual Installation ]<br>
1- [Download and install Electron](https://github.com/electron/electron/releases)<br>
2- Add Electron path to environment variables<br>
3- Clone repository to local storage *(or [Download ZIP](https://github.com/nimadez/voxel-builder/archive/refs/heads/main.zip))*<br>
4- Execute "run.bat" in Windows, or just enter the command:
```
> git clone https://github.com/nimadez/voxel-builder.git
> cd voxel-builder
> electron .
```
To switch from Offline to Online, edit "main.js" file:
```
loadFile('index.html') ==> loadURL('https://nimadez.github.io/voxel-builder')
```

## Known Issues
```
■ Max. 64K voxels (64000 or 40x40x40)
Each voxel is a particle, we used particles to build the world.
You may go up to 256K but you can't interact with voxels:
- Picking issue (GPU)
- SPS rebuild delay (CPU)
- Limited browser memory (unable to save/load/undo/redo)
Workaround: bake to mesh, 64K voxels per bake!

■ GLB failed to import multiple meshes for voxelization
Multiple meshes need to have the same properties,
or they won't merge, the only solution is to merge meshes
before exporting to GLB.

■ English is not my first language, sorry for the typos!
```

## FAQ
```
■ Will this project remain open-source?
Yes, remain open-source and ad-free

■ Can I use it to create 3D assets for commercial purposes?
Yes, you can use it however you want

■ Is it a small business or startup?
No, this is a fun project for learning purpose

■ How to merge vertices after export to GLB?
1- Open exported GLB file in Blender
2- Go to "Modeling" tab and choose vertex selection mode
3- Select all vertices (Ctrl + A)
4- Mesh > Clean Up > Merge by Distance
```

## History
```
4.0.0 -> release candidate
3.8.0 -> advancing to the next level (bakery)
3.6.0 -> major code rewrite
3.4.0 -> new features and ui/ux overhaul
3.0.0 -> SPS particles to build the world
0.0.0 -> I wrote a playground for learning Babylon.js
```

###### v3.0.0 *(BJS 4)* to v4.0.0 *(BJS 6)*<br>
![screenshot](media/devshots.jpg?raw=true "Screenshot")

## License
Code released under the [MIT license](https://github.com/nimadez/voxel-builder/blob/main/LICENSE).

## Credits
<a href="https://www.babylonjs.com/"><img width="200" src="https://raw.githubusercontent.com/BabylonJS/Brand-Toolkit/master/babylonjs_identity/fullColor/babylonjs_identity_color.svg"></img></a>

- [Babylon.js](https://www.babylonjs.com/)
- [Three.js](https://threejs.org/) *(vi²xel, asset-viewer, texture and hdri presets)*
- [MagicaVoxel](https://ephtracy.github.io/)
- [Electron](https://www.electronjs.org/)
- [Google Material Icons](https://github.com/google/material-design-icons)
- [Droid Sans Font](https://www.android.com/)
- [Blender](https://blender.org/)
- [KhronosGroup glTF-Sample-Models](https://github.com/KhronosGroup/glTF-Sample-Models)
- [KhronosGroup glTF-Sample-Environments](https://github.com/KhronosGroup/glTF-Sample-Environments)
- [Sketchfab](https://sketchfab.com/) *(MagicaVoxel free samples)*

###### Available in [Babylon.js community demos](https://www.babylonjs.com/community/)
