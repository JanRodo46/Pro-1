import os
cwd = os.getcwd()
print(cwd)
folder = f"{cwd}/cewfolder"
# os.makedirs(folder)
print(os.path.exists(folder))
if not os.path.exists(folder):
    os.makedirs(folder)
    print("Folder został utworzony")
else:
    print("Folder istnieje")
