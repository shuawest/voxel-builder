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
# The script removes the previous
# version before installation.
#
# For manual installation:
# https://github.com/nimadez/voxel-builder#desktop-installation
#

ELECTRON = 'https://github.com/electron/electron/releases/download/v23.1.3/electron-v23.1.3-win32-x64.zip'
VBUILDER = 'https://github.com/nimadez/voxel-builder/archive/refs/heads/main.zip'

run_bat = """@echo off
title Voxel Builder
start "" electron\electron .
pause
"""

import os
import shutil
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

cwd = os.getcwd()
DIR_SRC = cwd + '/voxel-builder/voxel-builder-main'
DIR_DST = cwd + '/voxel-builder'
DIR_ELC = cwd + '/voxel-builder/electron'

print('\n Voxel Builder Portable Installer')
print(' --------------------------------')
print(' Electron Package:', ELECTRON.split('/')[-1])
doEl = input(' Download Electron Package (Y/N)? ').upper()
print('')

if os.path.exists(DIR_DST):
    os.chdir(DIR_DST)
    for item in os.listdir(os.getcwd()):
        if item not in ["electron"]:
            if os.path.isfile(item):
                os.remove(item)
            elif os.path.isdir(item):
                shutil.rmtree(item, ignore_errors=True)

print('Downloading Voxel Builder Package...')
with urlopen(VBUILDER) as zip:
    with ZipFile(BytesIO(zip.read())) as zfile:
        zfile.extractall(DIR_DST)

print('Extracting...')
for f in os.listdir(DIR_SRC):
    shutil.move(os.path.join(DIR_SRC, f), DIR_DST)
os.rmdir(DIR_SRC)

with open(DIR_DST + "/run.bat", "w") as f:
    f.write(run_bat)

print('Done\n')

if doEl == 'Y':
    if os.path.exists(DIR_ELC):
        shutil.rmtree(DIR_ELC, ignore_errors=True)
    print('Downloading Electron Package...')
    with urlopen(ELECTRON) as zip:
        with ZipFile(BytesIO(zip.read())) as zfile:
            zfile.extractall(DIR_ELC)
    print('Done\n')

print('Running Voxel Builder')
os.chdir(DIR_DST)
if os.path.exists(DIR_ELC):
    os.system('electron\\electron .')
else:
    os.system('electron .')
