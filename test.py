folder_path = '/Users/apple/Downloads/bg/'
from tqdm.auto import tqdm
# get all file name in the folder
import os
import random
bg_files = os.listdir(folder_path)
# bg_files = [folder_path + file for file in bg_files]

for filename in tqdm(bg_files):
    name = filename.split('.')[0]
    extname = filename.split('.')[1]

    if os.path.exists(folder_path+name+'2.'+extname):
        os.remove(folder_path+filename)
        print(filename)