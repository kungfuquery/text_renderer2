# folder_path = '/Users/apple/Downloads/bg/'
# from tqdm.auto import tqdm
# # get all file name in the folder
# import os
# import random
# bg_files = os.listdir(folder_path)
# # bg_files = [folder_path + file for file in bg_files]

# for filename in tqdm(bg_files):
#     name = filename.split('.')[0]
#     extname = filename.split('.')[1]

#     if os.path.exists(folder_path+name+'2.'+extname):
#         os.remove(folder_path+filename)
#         print(filename)

import os
import glob

def count_files_in_folder(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return
    
    # Use glob to list all files in the folder
    files = glob.glob(os.path.join(folder_path, "*"))
    
    # Count the files
    file_count = len(files)
    
    print(f"Number of files in '{folder_path}': {file_count}")

# Example usage:
folder_path = "//Users/apple/text_renderer2/text_renderer/output/images/"
count_files_in_folder(folder_path)
