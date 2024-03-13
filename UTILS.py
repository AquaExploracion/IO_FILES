
import os
import re
import sys
import traceback
import collections
import shutil

def get_file_list(path):
    """

    Args:
        path (_type_): _description_

    Returns:
        _type_: _description_
    """
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def filter_list(file_list,pattern):
    """_summary_

    Args:
        file_list (_type_): _description_
        pattern (_type_): _description_

    Returns:
        _type_: _description_
    """
    filtered_list = [i for i in file_list if re.search(pattern, i)]
    return filtered_list


def copy_files(filtered_list,dest_path):
    """_summary_

    Args:
        filtered_list (_type_): _description_
        dest_path (_type_): _description_
    """
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    for file in filtered_list:
        shutil.copy(file,dest_path)
        
def rename_files(file_list,extension):
    len_ext=len(extension)
    for i in range(len(file_list)):
        print("File {} has been renamed to {}".format(file_list[i],file_list[i][:-15]+file_list[i][-len_ext:]))
        #os.rename(file_list[i],file_list[i][:-15]+".sgy"+file_list[i][-4:])
        os.rename(file_list[i],file_list[i][:-15]+file_list[i][-len_ext:])
    return