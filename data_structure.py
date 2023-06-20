import os
print(os.getcwd())
import shutil
print(shutil.disk_usage("/"))

list_of_cloud = ["aws","azure","gcp","oracle"];
print(list_of_cloud[0])

for cloud in list_of_cloud:
   print(cloud);
   
   
dict_of_cloud = {
   "aws":"Amazon Web Service",
   "azure":"ms azure",
   "gcp":"google cloud plateform"
   }
print(dict_of_cloud["aws"])



