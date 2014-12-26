#! D:\Python33\python.exe
# -*- coding: utf-8 -*-
# Module        : HomeworkCleaner.py
# Author        : bss
# Project       : TA
# State         :
# Creation Date : 2014-12-26
#  Last modified: 2014-12-26 16:00:21
# Description   : 
# 

import os
import zipfile

def cleanDir(dirname):
    pass

def zipDir(cd, dirname):
    zipName = os.path.join(cd, dirname + '.zip')
    f = zipfile.ZipFile(zipName, 'w', zipfile.ZIP_DEFLATED)
    searchDir = os.path.join(cd, dirname)
    for dirpath, dirnames, filenames in os.walk(searchDir):
        for filename in filenames:
            f.write(os.path.join(dirpath, filename),
                    os.path.join(dirpath, filename)[searchDir.__len__():])
    f.close()

def main():
    cd = os.path.abspath('.')
    print(cd)
    for dirname in os.listdir(cd):
        if os.path.isdir(os.path.join(cd, dirname)) and (dirname != '.git'):
            print(dirname + ':')
            zipDir(cd, dirname)

if __name__ == '__main__':
    try:
        main()
    except:
        pass
    os.system('pause')
 
