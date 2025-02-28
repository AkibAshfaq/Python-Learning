from pathlib import Path

p = Path('/')

for subdir in p.iterdir():
    if subdir.is_dir():
        print(subdir)


# Filtering the files 
pyfilter = p.rglob('*.py')

for f in pyfilter:
    print(f)

# Navigating in the directry
sp = p / 'OS_Module.py'
print(sp)

# Check if the path is absolute
print("Is absolute:", sp.is_absolute())

# Get the file name
print("File name:", sp.name)

# Get the extension
print("Extension:", sp.suffix)

# Get the parent directory
print("Parent directory:", sp.parent)



# Reading from a file
with (p / '/CODE Files/PY  files/Path Lib/example.txt').open('r') as file:
    content = file.read()
    print(content)

# Writing to a file
with (p / '/CODE Files/PY  files/Path Lib/output.txt').open('w') as file:
    file.write("Hello, GFG!")

# PurePath 
from pathlib import PurePath

obj = PurePath('foo/bar')
print(obj)


from pathlib import PurePosixPath

obj = PurePosixPath('foo/bar')
print(obj)

# PureWindowsPath
from pathlib import PureWindowsPath

obj = PureWindowsPath('foo/bar')
print(obj)

print(obj.is_absolute())
print(obj.name)


# Just path
from pathlib import Path

obj = Path('/usr/local/bin')
print(obj)

# PosixPath 
from pathlib import WindowsPath

obj = WindowsPath('/usr/local/bin')
print(obj)

# cwd in path 
print(obj.cwd())

# Exixtence
print(obj.exists())

# Directory information
print(obj.is_dir())