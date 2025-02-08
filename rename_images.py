import os

def rename_images(folder_path, prefix="image"):
    files = os.listdir(folder_path)
    files.sort()
    
    for index, filename in enumerate(files, start=1):
        ext = os.path.splitext(filename)[1]
        new_name = f"{prefix}_{index}{ext}"
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))
        print(f"Renamed: {filename} -> {new_name}")

# Example usage
rename_images("dataset/healthy")
rename_images("dataset/diseased")
