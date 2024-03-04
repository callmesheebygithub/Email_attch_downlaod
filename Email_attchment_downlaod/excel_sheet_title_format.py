class title_list:
    format_list=[]
    def __init__(self,name_list):

        self.name_list=name_list

    def title_format(self):

        for titles in self.name_list:

            title=titles.split("_")
            self.format_list.append(title[0].lower())
        
        return self.format_list
    
if __name__=="__main__":
    folder_names=['HS_Agreed_Templates.xlsx','SC_Agreed_Templates_PO.xlsx','CON_Agreed_Templates.xlsx','SIM_Agreed_Templates.xlsx','AC_Agreed_Templates.xlsx']
    obj=title_list(folder_names)
    final_list=obj.title_format()
    print(final_list)