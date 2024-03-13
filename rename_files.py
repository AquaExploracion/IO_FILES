import os
import re
import sys
import traceback
import collections
import shutil
from UTILS import *


# Path: copy_files.py
print("\n")
print   (" Script executing ...")  
print   (" Script executing ...")  
print   (" Script executing ...") 
print   (" Script executing ...")  
print   (" Script executing ...")  
print   (" Script executing ...")  
print("\n")
print('########################################################################################################')
print('#                                                                                                      #')
print('#                  Indique el path donde estan los archivos que se quieren Renombrar:                      #')
print('#                       FORMAT:            D:\SEGY\EBCDICs                                             #')
#path_in=input("Enter the path of the folder where the files are located: e.g. /home/user/folder or D:\SEGY\SEGY_Files\sbp\yoti \n")
#path_in='D:\SEGY\SEGY_Files\sbp\yoti'
print('#                                                                                                      #')
print('########################################################################################################')
print("\n")
print("\n")
PATH_IN=input("Path (e.g. D:\SEGY\SEGY_Files\sbp\yoti):  \n \n")
print("\n")
print   (" Reading Files ...") 
print   (" Reading Files ...") 
print   (" Reading Files ...") 
print("\n")
##################################################################################################################
##################################################################################################################
file_list=get_file_list(PATH_IN)
#PATH_IN="D:\SEGY\EBCDICs"
print(" Do you want  to print all the files in the folder?  ")
print(" 1. Yes ")
print(" 2. No ")
print_files_raw=input("Enter 1 or 2:  \n \n")
if print_files_raw=="1":
    print("\n")
    print(file_list)
    print("\n")
    print("Number of files found: {} Files ".format(len(file_list)))
else:
    print("\n")
    print("Number of files found: {} Files ".format(len(file_list)))
    print("Ok, lets continue")
    print("\n")
print("\n")
##################################################################################################################
##################################################################################################################    
# rename files  

print("\n")
print("\n")
print("\n")
print('########################################################################################################')
print('#                                                                                                      #')
print('#                  Type the  string contained in the files that you want to move, can be \n            #')    
print('                either a string within the file or an extension (e.g.  .sgy)                           #')
#extension=input("#Enter the extension of the file in format e.g. .sgy:         \n                              ")
print('#                                                                                                      #')
print('########################################################################################################')
print("\n")
print("\n")
string_inside_file=input("String contained in the file (e.g. WGS84):  \n \n")
filtered_list=filter_list(file_list,string_inside_file)
print("\n")
print("\n")
print(" Do you want  to print all selected files?  ")
print(" 1. Yes ")
print(" 2. No ")
print_files_processed=input("Enter 1 or 2:  \n \n")
if print_files_processed=="1":
    print("\n")
    print(filtered_list)
    print("\n")
    print("Number of files found: {} Files ".format(len(filtered_list)))
else:
    print("\n")
    print("Number of files found: {} Files ".format(len(filtered_list)))
    print("Ok, lets continue")
    print("\n")
print("\n")
pause=input("Press Enter to continue ...")




        
def rename_files_2(file_list,extension):
    len_ext=len(extension)
    for i in range(len(file_list)):
        print("File {} has been renamed to {}".format(file_list[i],file_list[i][:-8]+file_list[i][-len_ext:]))
        #os.rename(file_list[i],file_list[i][:-15]+".sgy"+file_list[i][-4:])
        os.rename(file_list[i],file_list[i][:-8]+file_list[i][-len_ext:])
    return

rename_files_2(filtered_list,extension=".sgy")


print("Successfully File Renamed")
print("\n")
print("\n")
print('########################################################################################################')
print('#               ooooo  o    o    ooooo  o  o                  o     o  oooooo    o     o               #')
print('#               o      o    o    o      o o                   o   o   o    o    o     o                #')
print('#               oo     o    o    o      oo                     o o    o    o    o     o                #')
print('#               o      o    o    o      o o                    o     o    o    o     o                 #')
print('#               o      oooooo    ooooo  o  o                  o     oooooo    ooooooo                  #')
print('#               you have been fucked up by el YORCH                                                    #')
print('########################################################################################################')    

