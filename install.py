from os import environ
from winreg import *
from urllib.request import urlretrieve
from subprocess import run

python_install_key=R'SOFTWARE\Python\PythonCore\3.6\InstallPath'
python_url_64='https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe'
python_url_32='https://www.python.org/ftp/python/3.6.8/python-3.6.8.exe'
python_installer_args=' /passive Include_launcher=0 AssociateFiles=0 Shortcuts=0'
is64='64' in environ['PROCESSOR_ARCHITECTURE'] or '64' in environ['PROCESSOR_ARCHITEW6432']
global_ini_path=environ['appdata']+'/obs-studio/global.ini'
install_path=None

def ensureInstallPath()->str:
    print('Searching for conflicting python installs')
    try:
        install_path=QueryValue(HKEY_LOCAL_MACHINE, python_install_key)
        print('System python 3.6 found')
        return install_path
    except:
        print('System python 3.6 not found')
    try:
        install_path=QueryValue(HKEY_CURRENT_USER, python_install_key)
        print('User python 3.6 found')
        return install_path
    except:
        print('User python 3.6 not found')
    print('downloading python')
    python_installer=None
    if is64:
        python_installer=urlretrieve(python_url_64)[0]
    else:
        python_installer=urlretrieve(python_url_32)[0]
    print('Installing python')
    run(python_installer+python_installer_args)
    return QueryValue(HKEY_CURRENT_USER, python_install_key)

def main():
    input('Make sure OBS is closed, then press enter to continue.')
    install_path=ensureInstallPath()
    print('Using '+install_path)
    print('Updating OBS config')
    from configparser import ConfigParser
    config=ConfigParser(strict=False)
    global_ini=open(global_ini_path,'r+',encoding='utf-8')
    config.read_string(global_ini.read().replace('\ufeff',''))
    if is64:
        keyname='path64bit'
    else:
        keyname='path32bit'
    if config.has_section('Python'):
        config['Python'][keyname]=install_path
    else:
        config['Python']={keyname:install_path}
    global_ini.seek(0)
    global_ini.truncate()
    config.write(global_ini,space_around_delimiters=False)
    global_ini.close()
    input('\nOBS can now use python 3.6 scripts\nYou can close this window\nor press enter to exit')

if __name__ == '__main__':
    main()