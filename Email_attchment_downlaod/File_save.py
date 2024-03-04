import pandas as pd
import os
import warnings

# Ignore warnings
warnings.filterwarnings("ignore")

# Specify the folder path where your Excel files are located
folder_path = '/home/muhammadshoaib/Desktop/Arcano_working/Email_attchment_downlaod/'

# Get a list of all Excel files in the folder
excel_files = [file for file in os.listdir(folder_path) if file.endswith('.xlsx')]

for file_name in excel_files:
    name = file_name.split("_")[0]
    
    # Check if the file matches the prefixes
    if name in ['AC', 'HS', 'CON', 'SIM', 'SC']:
        print(f"Processing {file_name}...")
        
        # Determine the destination folder based on the prefix
        destination_folder = f'/home/muhammadshoaib/Desktop/Arcano_working/Email_attchment_downlaod/JAZZ_{name}_PO'

        try:
            # Read the Excel file
            excel_data = pd.read_excel(os.path.join(folder_path, file_name))

            # Check if the destination folder exists, if not, create it
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            # Specify the destination file path for the current Excel file
            destination_file = os.path.join(destination_folder, file_name)

            # Save the Excel file to the specified destination
            excel_data.to_excel(destination_file, index=False)

            # Remove the Excel file from the source folder
            os.remove(os.path.join(folder_path, file_name))

            print(f"Saved {file_name} to {destination_folder}")
        except Exception as e:
            print(f"Error processing {file_name}: {e}")

    else:
        print(f"Ignoring {file_name}: Prefix not recognized.")





# import pandas as pd
# from excel_title import ExcelFileProcessor
# import os
# import warnings
# warnings.simplefilter("ignore")

# # # Specify the folder path where your Excel files are located
# folder_paths = '/home/muhammadshoaib/Desktop/Arcano_working/Email_attchment_downlaod/JAZZ_AC_PO'

# # # Get a list of all Excel files in the folder
# excel_files = [file for file in os.listdir(folder_paths) if file.endswith('.xlsx')]
# # print(excel_files)
# for file_name in excel_files:

#     name=file_name.split("_")[0]
#     # print(file_name.split("_")[0])
#     if name=='AC':
#         print("Found")
#         destination_folder = '/home/muhammadshoaib/Desktop/Arcano_working/Email_attchment_downlaod/JAZZ_AC_PO'

#         excel_data = pd.read_excel(os.path.join(folder_paths, file_name))
#         # print(excel_data)
#         # Specify the destination file path for the current Excel file
#         destination_file = os.path.join(destination_folder, file_name)
        
#         # Save the Excel file to the specified destination
#         excel_data.to_excel(destination_file, index=False)

#     elif name=='HS':

#         destination_folder = '/home/muhammadshoaib/Desktop/Arcano_working/Email_attchment_downlaod/JAZZ_HS_PO'
#         print("Found")

#         # Read the Excel file
#         excel_data = pd.read_excel(os.path.join(folder_paths, file_name))
#         # print(excel_data)
#         # Specify the destination file path for the current Excel file
#         destination_file = os.path.join(destination_folder, file_name)
        
#         # Save the Excel file to the specified destination
#         excel_data.to_excel(destination_file, index=False)

    # elif name=='CON':

    #     destination_folder = '/home/muhammadshoaib/Desktop/Arcano_working/Email_attchment_downlaod/JAZZ_CON_PO'


    #     for file_name in excel_files:
    #     # Read the Excel file
    #         excel_data = pd.read_excel(os.path.join(folder_path, file_name))
    #         print(excel_data)
    #         # Specify the destination file path for the current Excel file
    #         destination_file = os.path.join(destination_folder, file_name)
            
    #         # Save the Excel file to the specified destination
    #         excel_data.to_excel(destination_file, index=False)

    # elif name=='SC':

    #     destination_folder = '/home/muhammadshoaib/Desktop/Arcano_working/Email_attchment_downlaod/JAZZ_SC_PO'


    #     for file_name in excel_files:
    #     # Read the Excel file
    #         excel_data = pd.read_excel(os.path.join(folder_path, file_name))
    #         print(excel_data)
    #         # Specify the destination file path for the current Excel file
    #         destination_file = os.path.join(destination_folder, file_name)
            
    #         # Save the Excel file to the specified destination
    #         excel_data.to_excel(destination_file, index=False)

    # elif name=='SIM':

    #     destination_folder = '/home/muhammadshoaib/Desktop/Arcano_working/Email_attchment_downlaod/JAZZ_SIM_PO'


    #     for file_name in excel_files:
    #     # Read the Excel file
    #         excel_data = pd.read_excel(os.path.join(folder_path, file_name))
    #         # print(excel_data)
    #         # Specify the destination file path for the current Excel file
    #         destination_file = os.path.join(destination_folder, file_name)
            
    #         # Save the Excel file to the specified destination
    #         excel_data.to_excel(destination_file, index=False)


    # else:
    #     print("Attachment does not belong to the this directory")



# # Specify the destination folder where you want to save each Excel file

# # Iterate through each Excel file
# for file_name in excel_files:
#     # Read the Excel file
#     excel_data = pd.read_excel(os.path.join(folder_path, file_name))
#     print(excel_data)
#     # Specify the destination file path for the current Excel file
#     destination_file = os.path.join(destination_folder, file_name)
    
#     # Save the Excel file to the specified destination
#     excel_data.to_excel(destination_file, index=False)
