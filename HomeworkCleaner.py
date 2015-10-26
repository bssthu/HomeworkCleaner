#! D:\Python33\python.exe
# -*- coding: utf-8 -*-
# Module        : HomeworkCleaner.py
# Author        : bss
# Project       : TA
# State         :
# Creation Date : 2014-12-26
# Description   : 
# 

import os
import zipfile

g_basicList = ['obj','tlog','pdb','ilk','idb','log','lastbuildstate',
        'manifest','res','rc','cache','cs','resources','baml','lref',
        'exe.config','filelistabsolute.txt','pch','cpp','h',
        'enc','dep','tlh','tli','sbr','bsc','dll.bi']

# 是否要删除此文件
def checkClearDir(path, filenames, choose):
    s = os.sep
    if (path.find('__MACOSX'+s) >= 0
            or path.endswith('.DS_Store')):
        return True
    path = path.lower() # windows
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
            path.endswith('.ncb') or
            path.endswith('thumbs.db') or
            path.endswith('.pdb') or
            path.endswith('unsuccessfulbuild') or
            path.startswith('~$ ')):
        return True
    if (path.endswith('.rar') or
            path.endswith('.zip') or
            path.endswith('.7z') or
            path.endswith('.tar') or
            path.endswith('.gz')):
        print('>archive ' + path.split(os.sep)[-1])
    if (path.find('debug'+s) >= 0 or
            path.find('release'+s) >= 0) :
        if 1 == choose:     # basic
            for ext in g_basicList:
                if path.endswith('.' + ext):
                    return True
            print('>keep ' + path.split(os.sep)[-1])
        else:   # aggressive, only keep dll and exe
            return True
    return False

def zipDir(cd, dirname, choose):
    zipName = os.path.join(cd, dirname + '.zip')
    f = zipfile.ZipFile(zipName, 'w', zipfile.ZIP_DEFLATED)
    searchDir = os.path.join(cd, dirname)
    for dirpath, dirnames, filenames in os.walk(searchDir):
        for filename in filenames:
            fileAbsPath = os.path.join(dirpath, filename)
            if not checkClearDir(fileAbsPath, filenames, choose):
                f.write(fileAbsPath, fileAbsPath[searchDir.__len__():])
    f.close()

def main():
    cd = os.path.abspath('.')
    print(cd)
    print('https://github.com/bssthu/HomeworkCleaner')
    choose = input('1. Basic; 2. Aggressive ')
    try:
        choose = int(choose)
    except:
        pass
    if (choose != 1 and choose != 2):
        print('bye~')
        return

    for dirname in os.listdir(cd):
        if os.path.isdir(os.path.join(cd, dirname)) and (dirname != '.git'):
            print(dirname + ':')
            zipDir(cd, dirname, choose)
    print('nice!')

if __name__ == '__main__':
    main()
    os.system('pause')
 
