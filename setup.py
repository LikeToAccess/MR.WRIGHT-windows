##import sys, os
##from cx_Freeze import setup, Executable
##
##__version__ = "1.0.0"
##
##include_files = [os.listdir(os.getcwd())]
##excludes = ["tkinter"]
##packages = ["os","random","time","random","pygame","sys"]
##
##setup(
##    name = "MRWRIGHT",
##    description='The New Mr. Wright Game!',
##    version=__version__,
##    options = {"build_exe": {
##        'packages': packages,
##        'include_files': include_files,
##        'excludes': excludes,
##        'include_msvcr': True,
##        }
##    },
##    executables = [Executable(script="mrwright.py")]
##)

import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python36-32\tcl\tk8.6'

setup(name = "mrwright",
        version = "1.0.0",
        description = "Copyright 2019",
        author = "Rico Alexander",
        author_email = "thecodingnapkin@gmail.com",
        options = {"build_exe": {
            'packages': ["pygame"],
            'include_files': os.listdir(os.getcwd()),
            }
        },
        executables = [Executable("mrwright.py")])
