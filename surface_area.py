Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=1
>>> type(a)
<class 'int'>
>>> import numpy as np
... from stl import mesh
... import pandas as pd
... from Ipython.display import display
... 
... stl_file = "C:\Users\abidhar\Downloads.stl" 
... test_mesh = mesh.Mesh.from_file(stl_file)
... 
... vertices = test_mesh.vectors.reshape(-1,3)
... 
... unique_vertices = np.unique(vertices,axis=0)
... 
... df_vertices = pd.DataFrame(unique_vertices , columns=["X","Y","Z"])
... 
... display(df_vertices)
SyntaxError: multiple statements found while compiling a single statement
>>> 
... 
... from stl import mesh
... import pandas as pd
... from Ipython.display import display
... 
... stl_file = "C:\Users\abidhar\Downloads.stl" 
... test_mesh = mesh.Mesh.from_file(stl_file)
... 
... vertices = test_mesh.vectors.reshape(-1,3)
... 
... unique_vertices = np.unique(vertices,axis=0)
... 
... df_vertices = pd.DataFrame(unique_vertices , columns=["X","Y","Z"])
... 
... display(df_vertices)
SyntaxError: multiple statements found while compiling a single statement
>>> pip install numpy-stl
SyntaxError: invalid syntax
>>> pip install numpy-stl
... from stl import mesh
... import pandas as pd
... from Ipython.display import display
... 
... stl_file = "C:\Users\abidhar\Downloads.stl" 
... test_mesh = mesh.Mesh.from_file(stl_file)

vertices = test_mesh.vectors.reshape(-1,3)

unique_vertices = np.unique(vertices,axis=0)

df_vertices = pd.DataFrame(unique_vertices , columns=["X","Y","Z"])

display(df_vertices)
SyntaxError: invalid syntax
from stl import mesh
import numpy as np

# Load STL file
your_mesh = mesh.Mesh.from_file(r"D:\new\myTet.stl")

# All vertices
vertices = your_mesh.vectors.reshape(-1, 3)

# Remove duplicates (optional)
unique_vertices = np.unique(vertices, axis=0)

print("All vertices:\n", vertices)
print("\nUnique vertices:\n", unique_vertices)
SyntaxError: multiple statements found while compiling a single statement

clear
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
Clear All
SyntaxError: invalid syntax
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))
SyntaxError: multiple statements found while compiling a single statement
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))
SyntaxError: multiple statements found while compiling a single statement
import numpy
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    import numpy
ModuleNotFoundError: No module named 'numpy'
immport numpy-config
SyntaxError: invalid syntax
import numpy-config
SyntaxError: invalid syntax
