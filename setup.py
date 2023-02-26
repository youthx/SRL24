# NO NEED TO USE THIS, THIS WAS FOR TESTING

from cx_Freeze import setup, Executable

base = None    

executables = [Executable("srl24.py", base=base)]

packages = [
    "idna", 
    "random", 
    "win32api",
    "win32gui", 
    "win32ui", 
    "win32file", 
    "win32con",
    "multiprocessing",
    "ctypes",
    "os",
    "sys",
    "math",
    "requests",
    "tkinter",
    "string",
]

options = {
    'build_exe': {    
        'packages': packages,
    },    
}

setup(
    name = "SRL24",
    options = options,
    version = "0.11",
    description = 'The SRl24 Experience',
    executables = executables
)
