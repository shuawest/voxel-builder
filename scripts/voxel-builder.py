#
# Voxel Builder Portable Installer
#
# Edit "ELECTRON" variable to download
# newer Electron package based on your
# operating system
# Visit https://github.com/electron/electron/releases
#
# If you have Electron installed,
# there is no need to reinstall.
#
ELECTRON = 'https://github.com/electron/electron/releases/download/v23.1.3/electron-v23.1.3-win32-x64.zip'
VBUILDER = 'https://github.com/nimadez/voxel-builder/archive/refs/heads/main.zip'

import os
import shutil
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

cwd = os.getcwd()
DIR_SRC = cwd + '/voxel-builder/voxel-builder-main'
DIR_DST = cwd + '/voxel-builder'

print('\n Voxel Builder Portable Installer')
print(' --------------------------------')
print(' Electron Package:', ELECTRON.split('/')[-1])
doEl = input(' Download Electron Package (Y/N)? ').capitalize()
print('')

if os.path.exists(DIR_DST):
    shutil.rmtree(DIR_DST, ignore_errors=True)

print('Downloading Voxel Builder Package...')
with urlopen(VBUILDER) as zip:
    with ZipFile(BytesIO(zip.read())) as zfile:
        zfile.extractall(DIR_DST)

print('Extracting...')
for f in os.listdir(DIR_SRC):
    shutil.move(os.path.join(DIR_SRC, f), DIR_DST)
os.rmdir(DIR_SRC)
print('Done\n')

if doEl == 'Y':
    print('Downloading Electron Package...')
    with urlopen(ELECTRON) as zip:
        with ZipFile(BytesIO(zip.read())) as zfile:
            zfile.extractall(DIR_DST)
    print('Done\n')

print('Running Voxel Builder')
os.chdir(DIR_DST)
os.system('electron .')
