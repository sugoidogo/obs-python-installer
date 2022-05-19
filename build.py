from winreg import *
from os.path import join,abspath,dirname
from subprocess import run
from sys import path

hives=[
    HKEY_LOCAL_MACHINE,
    HKEY_CURRENT_USER
]

roots=[
    R'SOFTWARE\WOW6432Node\Python',
    R'SOFTWARE\Python'
]

def getPythonPath()->str:
    print('Searching for Python installs')
    for hive in hives:
        for root in roots:
            try:
                rootKey=OpenKey(hive, root)
                companyCount=QueryInfoKey(rootKey)[0]
                for companyIndex in range(companyCount):
                    companyName=EnumKey(rootKey, companyIndex)
                    companyKey=OpenKey(rootKey, companyName)
                    tagCount=QueryInfoKey(companyKey)[0]
                    for tagIndex in range(tagCount):
                        tagName=EnumKey(companyKey, tagIndex)
                        tagKey=OpenKey(companyKey, tagName)
                        pythonPath=join(QueryValue(tagKey, 'InstallPath'),'python.exe')
                        print('Using '+pythonPath)
                        return pythonPath
            except:
                pass

def installPyInstaller(python:str):
    print('Installing/Updating PyInstaller')
    command=python+' -m pip install pyinstaller --user'
    run(command)
    
def build(python:str)->int:
    return run(python+' -m PyInstaller -F install.py').returncode

def main():
    python=getPythonPath()
    try:
        assert build(python)==0
    except:
        installPyInstaller(python)
        return build(python)
        
if __name__ == '__main__':
    exit(main())