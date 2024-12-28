import os
import shutil

target_dir = r"E:\Backup\Pictures" 

image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

for root, dirs, files in os.walk("C:\\"):
    for file in files:
        if any(file.lower().endswith(ext) for ext in image_extensions):
            source_file = os.path.join(root, file)
            target_file = os.path.join(target_dir, os.path.relpath(source_file, "C:\\"))
            target_file_dir = os.path.dirname(target_file)
            
            if not os.path.exists(target_file_dir):
                os.makedirs(target_file_dir)
                
            shutil.copy2(source_file, target_file)
            print(f"Copied {source_file} to {target_file}")

print("All images have been copied.")
