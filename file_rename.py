import os
def rename_files():
    print("called rename files function");
    file_directory=os.listdir(r"/Users/vivek/Data/Code/Python/python_scripts/fileRename") 
    print(file_directory)
    current_directory=os.getcwd()
    print(current_directory)
    os.chdir(r"/Users/vivek/Data/Code/Python/fileRename")
    print(os.getcwd())
    for file_name in file_directory:
        print(file_name)
        new_name=file_name.translate(None,"0123456789")
        os.rename(file_name,new_name)

    os.chdir(current_directory)  
rename_files()
