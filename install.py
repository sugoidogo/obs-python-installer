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
scenes_path=environ['appdata']+'/obs-studio/basic/scenes/'

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
print('setting python path in all scene collections...')
for filename in listdir(scenes_path):
    if(filename.endswith('.json')):
        try:
            file=open(scenes_path+filename,'r+',encoding='utf-8')
            json=load(file)
            if(len(json['modules']['scripts-tool'])==0):
                json['modules']['scripts-tool'].append({
                    'path':install_path
                })
            else:
                json['modules']['scripts-tool'][0]['path']=install_path
            file.seek(0)
            file.truncate()
            dump(json, file)
            file.close
            print('updated '+filename)
        except:
            from traceback import print_exc
            print_exc()
            print('update failed on '+filename)
print('')
print('Python 3.6.8 embedded plus pip has been installed')
print('All existing scene collections have been updated')
print('To add python to new scenes, simply close obs and run this installer again')
input('You may now close this window')