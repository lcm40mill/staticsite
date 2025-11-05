import shutil, os, sys
from copystatic import copy_files_recursive

static_dir_path = "./static"
public_dir_path = "./public"
default_path = "/"

def main():
    basepath = default_path
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    
    print("Deleting Public Directory")
    if os.path.exists(public_dir_path):
        shutil.rmtree(public_dir_path)

    print("Cloning static files to Public Directory")
    copy_files_recursive(static_dir_path, public_dir_path)


main()