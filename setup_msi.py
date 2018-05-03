# coding=utf-8

import sys
import json
import os
from cx_Freeze import setup, Executable

# --- for resolving KeyError: 'TCL_LIBRARY' ---
import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
# ------


name = "s2aio"
version = "1.12"
description = 'A Scratch 2.0 (Offline) Hardware Extension for Arduino'
author = 'Alan Yorinks (msi installer: memakura)'
url ='https://github.com/MrYsLab/s2aio/wiki'

# 変更しない
upgrade_code = '{0B3D0CFF-BD3C-470D-9919-F5145E8823C6}'

# ----------------------------------------------------------------
# セットアップ
# ----------------------------------------------------------------
shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "s2aio",                    # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]s2aio.exe",# Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     "TARGETDIR",              # WkDir
     )
    ]

# Now create the table dictionary
msi_data = {"Shortcut": shortcut_table}

build_exe_options = {"packages": ['asyncio', 'serial.win32', 'idna'],
                    "excludes": [],
                    "includes": [],
                    "include_files": [
                        ('s2aio/configuration/', 'configuration'),
                        ('s2aio/miscellaneous/', 'miscellaneous'),
                        ('s2aio/ScratchFiles/', 'ScratchFiles'),
                        'icons/',
                        '00scratch/',
                        'license.txt'
                    ]
}
#                    "compressed": True


bdist_msi_options = {'upgrade_code': upgrade_code,
                    'add_to_path': False,
                    'data': msi_data
}

options = {
    'build_exe': build_exe_options,
    'bdist_msi': bdist_msi_options
}

# exeの情報
base = None #'Win32GUI' if sys.platform == 'win32' else None
icon = 'icons/icon_256x256.ico'

# exe にしたい python ファイルを指定
exe = Executable(script = 's2aio/__main__.py',
                 targetName = 's2aio.exe',
                 base = base,
                 icon = icon
                 )
#                 copyDependentFiles = True

# セットアップ
setup(name = name,
      version = version,
      author=author,
      url=url,
      description = description,
      options = options,
      executables = [exe]
      )
