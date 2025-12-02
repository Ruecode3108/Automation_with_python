import os
import shutil

source_folder="unorganised"
destination_folder="organised_files"
# Make sure the destination folder exists
os.makedirs(destination_folder, exist_ok=True)

# Loop through all files and directories in the source folder
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)
    
    # Check if the current item is a file
    if os.path.isfile(file_path):
        # 1. Split the filename into name and extension
        name, extension = os.path.splitext(filename)
        
        # 2. Clean the extension (remove '.', lowercase, or use "no_ext")
        # extension[1:] removes the dot (e.g., '.txt' becomes 'txt')
        clean_ext = extension[1:].lower() or "no_ext" 

        # 3. Define the new filename format
        # Example: 'txt_document.renamed.txt'
        new_name = f"{clean_ext}_{name}.renamed{extension}"

        # 4. Define the extension-specific subfolder and make sure it exists
        ext_folder = os.path.join(destination_folder, clean_ext)
        os.makedirs(ext_folder, exist_ok=True) # <-- Added this line

        # 5. Define the full new path
        new_path = os.path.join(ext_folder, new_name)

        # 6. Move and rename the file
        shutil.move(file_path, new_path)

print("Files renamed and sorted into folders")