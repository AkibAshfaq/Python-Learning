import os

def curr():
    # Current Working directry
    cwd = os.getcwd()
    print(cwd)

# Change location
curr()
os.chdir('../')
curr()
os.chdir('PY  files')


try :
    os.mkdir('WithPy')

    directory = "WithPy2\d"
    parent_dir = "E:\CODE Files\PY  files"
    path = os.path.join(parent_dir, directory)
    os.makedirs(path)
    print("Directory '% s' created" % directory)
    directory = "c\e"
    parent_dir = "E:\CODE Files\PY  files"
    mode = 0o666
    path = os.path.join(parent_dir, directory)
    os.makedirs(path, mode)
    print("Directory '% s' created" % directory)
except:
    print('Already Exists')


