import os

class create_folder_at_your_location:
    # Join the path and folder name to create the full directory path
    def __init__(self,path,folder_name):
        self.path=path
        self.folder_name=folder_name
    
    def create_folders(self):
        full_path = os.path.join(self.path, self.folder_name)
        
        try:

            # Create the directory
            os.makedirs(full_path)
            print(f"Folder '{self.folder_name}' created successfully at '{self.path}'")
        except FileExistsError:
            print(f"Folder '{self.folder_name}' already exists at '{self.path}'")
        except Exception as e:
            print(f"An error occurred: {e}")

# Specify the path where you want to create the folder

if __name__=="__main__":
    target_directory = r"""/home/muhammadshoaib/Desktop/"""
    new_folder_names=['JAZZ_HS_PO','JAZZ_SC_PO','JAZZ_CON_PO','JAZZ_SIM_PO','JAZZ_AC_PO']
# Specify the name of the folder you want to create
    # for folder in new_folder_names:
    #     obj=create_folder(folder)
    #     obj.folder_creation()


#==================================================================================================
import os

class create_folder:
    
    def __init__(self,Folder_name):
        self.folder_name=Folder_name

    def folder_creation(self):
        try:
            # Create the directory in the current working directory
            os.makedirs(self.folder_name)
            print(f"Folder '{self.folder_name}' created successfully in the current working directory")
        except FileExistsError:
            print(f"Folder '{self.folder_name}' already exists in the current working directory")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__=="__main__":
    new_folder_names=['JAZZ_HS_PO','JAZZ_SC_PO','JAZZ_CON_PO','JAZZ_SIM_PO','JAZZ_AC_PO']
# Specify the name of the folder you want to create
    for folder in new_folder_names:
        obj=create_folder(folder)
        obj.folder_creation()
