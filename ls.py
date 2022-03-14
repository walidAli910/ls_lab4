# Import Module
import os
import json
import re
# Folder Path
path = r"C:\Users\Walid\PycharmProjects\ls_lab\Lab01_FCR_instances"

os.chdir(path)
def read_text_file(file_path):
   str =""
   with open(file_path, 'r') as f:
      str =f.read().replace("\n","")
   var = str.split(";")
   i = 0
   while( var[i].find("=") == -1):
      i += 1
   instance_name =  var[i].split("=")[1].strip()
   i += 1
   d = int(var[i].split("=")[1].strip())
   i += 1
   r = int(var[i].split("=")[1].strip())
   i += 1
   scj = var[i].split("=")[1].strip()
   scj = re.sub("\s+",",",scj)
   SCj = json.loads(scj)
   i += 1
   Dk = var[i].split("=")[1].strip()
   Dk = re.sub("\s+",",",Dk)
   Dk = json.loads(Dk)
   i += 1
   Cjk = var[i].split("=")[1].strip()
   Cjk = re.sub("\s+",",",Cjk)
   Cjk = json.loads(Cjk)



if __name__ == '__main__':
   instance_name = ""
   d = 0
   r = 0
   SCj = []
   Dk = []
   Cjk= []
   # iterate through all file
   for file in os.listdir():
      # Check whether file is in text format or not
      if file.endswith(".dat"):

         file_path = f"{path}\{file}"
         read_text_file(file_path)
