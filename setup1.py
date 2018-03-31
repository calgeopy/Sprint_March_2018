from distutils.core import setup
from glob import glob
import py2exe
import sys
sys.path.append(r'c:\data\github\spring_march_2018')
data_files = [("Microsoft.VC90.CRT", glob(r'c:\data\github\spring_march_2018\*.*'))]
setup(
 data_files=data_files,
 windows=['proj1.py'] ,
 options={"py2exe": {"excludes":["Tkconstants", "Tkinter", "tcl"]}}