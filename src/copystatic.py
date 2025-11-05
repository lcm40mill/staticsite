import os, shutil

def copy_files_recursive(source_path, dest_path):
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)
    
    for file in os.listdir(source_path):
        out_path = os.path.join(source_path, file)
        in_path = os.path.join(dest_path, file)
        print(f"Moving from {out_path} to {in_path}")
        if os.path.isfile(out_path):
            shutil.copy(out_path, in_path)
        else:
            copy_files_recursive(out_path, in_path)