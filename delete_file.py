import os
from name_variables import Var

delete_check = 0
file_names = ['Bottom-Layer.png', 'Top-Layer.png', 'Green-Screen.png', Var.psd_name, Var.png_name, '1.png']
print(f'{len(file_names)} Number of files must be deleted')

for file_name in file_names:
    if os.path.exists(file_name):
        os.remove(file_name)
        delete_check += 1
        print(f"{file_name} : Has been deleted")
    else:
        print(f"{file_name} : Does not exist")

if delete_check > 0:
    print('All file has been deleted')
    print('Total Count : ', delete_check)
else:
    print('--------------------------')
    print('|', 'No files were deleted ', '|')
    print('--------------------------')
