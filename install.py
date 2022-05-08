from os import environ
from zipfile import ZipFile
from io import BytesIO
from urllib.request import urlopen
from os import makedirs,chdir
from subprocess import run
from json import load, dump
from os import listdir

python_url='https://www.python.org/ftp/python/3.6.8/python-3.6.8-embed-amd64.zip'
install_path=environ['appdata']+'/obs-studio/python/'
pth_path='python36._pth'
pth_string='python36.zip\n.\nimport site\n./Lib/site-packages/'
pip_url='https://bootstrap.pypa.io/pip/3.6/get-pip.py'
pip_path='get-pip.py'
pip_command='python.exe get-pip.py --no-warn-script-location'
global_ini_path=environ['appdata']+'/obs-studio/global.ini'

input('Make sure OBS is closed, then press Enter to continue')
print('downloading python...')
zip=ZipFile(BytesIO(urlopen(python_url).read()))
print('creating install folder...')
makedirs(install_path,exist_ok=True)
print('extracting python...')
chdir(install_path)
for filename in zip.namelist():
    ofile=open(filename,'wb')
    ifile=zip.open(filename)
    ofile.write(ifile.read())
    ofile.close()
    ifile.close()
print('enabling site-packages...')
pth=open(pth_path,'w')
pth.write(pth_string)
pth.close()
print('downloading pip installer...')
get_pip=open(pip_path,'wb')
get_pip.write(urlopen(pip_url).read())
get_pip.close()
print('running pip installer...')
run(install_path+pip_command)
print('setting python path in OBS...')
global_ini_file=open(global_ini_path,'a')
global_ini_file.writelines([
    '\n',
    '[Python]\n'
    'Path64bit='+install_path+'\n'
])
global_ini_file.close()
print('')
print('Python 3.6.8 embedded plus pip has been installed')
print('Your OBS Settings have been updated')
input('You may now close this window')