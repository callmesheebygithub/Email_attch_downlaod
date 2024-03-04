# import os
# import pandas as pd
# import warnings

# class ExcelFileProcessor:
#     def __init__(self, folder_path):
#         self.folder_path = folder_path
#         self.file_name_list = []

#     def process_excel_files(self):
#         # Suppress warnings from openpyxl
#         warnings.simplefilter("ignore")

#         # List all files in the folder
#         files = os.listdir(self.folder_path)

#         # Filter out only Excel files
#         excel_files = [file for file in files if file.endswith('.xlsx')]

#         # Iterate over each Excel file
#         for file in excel_files:
#             # Construct the full path to the Excel file
#             file_path = os.path.join(self.folder_path, file)
            
#             try:
#                 # Load the Excel file
#                 excel_data = pd.read_excel(file_path)
                
#                 # Extract file name (excluding extension)
#                 file_name = os.path.splitext(file)[0]
                
#                 # Print the file name
#                 self.file_name_list.append(file_name)
#             except Exception as e:
#                 print(f"Error processing file '{file}': {e}")

#     def extract_prefixes(self):
#         # Extracting prefixes from file names
#         prefix_title = []
#         for pre in self.file_name_list:
#             title = pre.split("_")
#             prefix_title.append(title[0])
        
#         return prefix_title

# if __name__ == "__main__":
#     # Path to the folder containing Excel files
#     folder_path = '/home/muhammadshoaib/Desktop/Arcano_working/Email_attchment_downlaod/JAZZ_CON_PO'

#     # Create an instance of ExcelFileProcessor
#     processor = ExcelFileProcessor(folder_path)

#     # Process Excel files
#     processor.process_excel_files()

#     # Get prefixes from file names
#     prefixes = processor.extract_prefixes()

#     # Print the list of prefixes
#     print(prefixes)

#     if prefixes[0]=="HS":
#         print("Found")
#     else:
#         print("not found")


import os
import pandas as pd
import warnings

class ExcelFileProcessor:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.file_name_list = []
        self.prefix_title = []

    def process_excel_files(self):
        # Suppress warnings from openpyxl
        warnings.simplefilter("ignore")

        # List all files in the folder
        files = os.listdir(self.folder_path)

        # Filter out only Excel files
        excel_files = [file for file in files if file.endswith('.xlsx')]

        # Iterate over each Excel file
        for file in excel_files:
            # Construct the full path to the Excel file
            file_path = os.path.join(self.folder_path, file)
            try:
                # Load the Excel file
                excel_data = pd.read_excel(file_path)
                
                # Extract file name (excluding extension)
                file_name = os.path.splitext(file)[0]
                
                # Append the file name to the list
                self.file_name_list.append(file_name)
            except Exception as e:
                print(f"Error processing file '{file}': {e}")

    def extract_prefixes(self):
        # Extracting prefixes from file names
        for pre in self.file_name_list:
            title = pre.split("_")
            self.prefix_title.append(title[0])
        
        return self.prefix_title

if __name__ == "__main__":
    # Path to the folder containing Excel files
    folder_path = '/home/muhammadshoaib/Desktop/Arcano_working/Email_attchment_downlaod/JAZZ_CON_PO'

    # Create an instance of ExcelFileProcessor
    processor = ExcelFileProcessor(folder_path)

    # Process Excel files
    processor.process_excel_files()

    # Get prefixes from file names
    processor.extract_prefixes()
    print(processor.prefix_title[0])
