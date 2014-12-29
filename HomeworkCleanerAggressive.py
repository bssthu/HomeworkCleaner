#! D:\Python33\python.exe
# -*- coding: utf-8 -*-
# Module        : HomeworkCleanerAggressive.py
# Author        : bss
# Project       : TA
# State         :
# Creation Date : 2014-12-26
#  Last modified: 2014-12-29 17:01:28
# Description   : 
# 

import os
import zipfile

# 是否要删除此文件
def checkClearDir(path, filenames):
    s = os.sep
    if (path.endswith('d.dll')):
        dllname = path.split(os.sep)[-1][:-5]
        for filename in filenames:
            if dllname == filename[:-4]:
                return True
    if (path.endswith('.dll') or path.endswith('.exe')):
        return False
    if (path.endswith('.sdf') or
            path.endswith('.opensdf') or
            path.endswith('.aps') or
            path.find(s+'ipch'+s) >= 0 or
            path.endswith('.pdb') or
            path.find('Debug'+s) >= 0 or
            path.find('Release'+s) >= 0 :
        return True
    return False

def zipDir(cd, dirname):
    zipName = os.path.join(cd, dirname + '.zip')
    f = zipfile.ZipFile(zipName, 'w', zipfile.ZIP_DEFLATED)
    searchDir = os.path.join(cd, dirname)
    for dirpath, dirnames, filenames in os.walk(searchDir):
        for filename in filenames:
            fileAbsPath = os.path.join(dirpath, filename)
            if not checkClearDir(fileAbsPath, filenames):
                f.write(fileAbsPath, fileAbsPath[searchDir.__len__():])
    f.close()

def main():
    cd = os.path.abspath('.')
    print(cd)
    for dirname in os.listdir(cd):
        if os.path.isdir(os.path.join(cd, dirname)) and (dirname != '.git'):
            print(dirname + ':')
            zipDir(cd, dirname)

if __name__ == '__main__':
    main()
    print('nice!')
    os.system('pause')
 
