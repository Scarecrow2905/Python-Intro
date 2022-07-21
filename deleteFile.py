import os
import shutil

path = "empty_folder"
try:
    #os.remove(path)
    #os.rmdir(path)
    #shutil.rmtree(path) # This one is a bit dangerous as it deletes the folder and everything it contains
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function (You need shutil)")
else:
    print(path+" was deleted")