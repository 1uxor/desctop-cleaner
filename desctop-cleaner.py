import os
import shutil
import sys


def create_subfolder_if_needed(folder_path, subfolder_name):
    subfolder_path = os.path.join(folder_path, subfolder_name)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    return subfolder_path

def clean_folder(folder_path):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_extension = filename.split('.')[-1].lower()
            if file_extension:
                subfolder_name = f"{file_extension.upper()}Files"
                subfolder_path = create_subfolder_if_needed(folder_path, subfolder_name)
                file_path = os.path.join(folder_path,filename)
                shutil.move(file_path, subfolder_path)
                print(f"the movement that done is :{filename}->{subfolder_name}/")




if __name__ == "__main__":
    print("!!!Desktop Cleaner!!!")
    
    while True:
        folder_path = input("Please enter the folder path  : ")

        if os.path.isdir(folder_path):
            clean_folder(folder_path)
            print("Cleaning Complete !")
            break
        else:
            print("Invalid folder path. Please enter a correct path!.")