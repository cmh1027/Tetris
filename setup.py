import sys
from cx_Freeze import setup, Executable

build_exe_options = {"includes":["os", "pickle", "pygame", "math", "sys", "Block", "Board", "constants"], "include_files":['music', 'data.bin', 'record.bin']}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Tetris",
        version = "0.1",
        description = "Tetris",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main.py", base=base)])