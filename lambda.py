# import os

# path = 'c:/Python39/lib/os.py'
# #tpyeError: expected str, bytes or os.pathlike obj, not dict. This path does not work in powershell 

# for root, directories, files in os.walk(path, topdown=False):
# 	for name in files:
# 		print(os.path.join(root, name))
# 	for name in directories:
# 		print(os.path.join(root, name))
#----------------------------------------------------------------------------------------------------------------------------------------
# import boto3 
# zip = client.get_object(Bucket='richnet-website',Key='myBuild.zip') 
# for f in zip:
#     print(f)
      

'''
  import boto3
  
  client = boto3.client('s3')
  client.list_buckets()
  
  all s3 buckets come up, need to figure out the path for the dir for the s3 bbuckets on this client
  
  i think the path for the buckets maybe C:/Python39/lib/os.py, nvm not a dir
  
  ** import boto3 
  **zip = client.get_object(Bucket='richnet-websiite',Key='myBuild.zip') 
  **for f in zip:
  **    print(f)
  this script prints all the names of the files in this bucket. do i know if its zipped, no idea
'''
  
  
  # -----------------------------------------------------------------------------------------------------------------------------------------------
  
  
import zipfile,boto3,os
from io import BytesIO




BUCKET='richnet-website'
key='myBuild.zip'

s3 = boto3.resource('s3')
my_bucket = s3.Bucket(BUCKET)

filebytes = BytesIO()

my_bucket.download_fileobj(key, filebytes)

file = zipfile.ZipFile(filebytes)

file.extractall('/tmp')

path = '/tmp'

#on mac
for root,dirs,files in os.walk(path):
  for name in files:
    s3.meta.client.upload_file(os.path.join(root,name),'unzipped-richnet-website',name)

# on windows IMPORTANT
# for root, dirs, files in os.walk(path):
# 	for name in files:
#     old = r'{}'.format(os.path.join(root, name)) 
#     newPath = old.replace(os.sep,'/')[29::]
#     s3.meta.client.upload_file(old,'unzipped-richnet-website',key)
  
  
# for name in direct:               NOTE dont need all this, not sure why i put this in this if i walk through files, it will walk through all dirs and sub dirs to all files in the directory path i choose. 
#   old = r'{}'.format(os.path.join(root, name))  #didnt try this yet 
#   newPath = old.replace(os.sep,'/')
#   s3.meta.client.upload_file(f'{newPath}','unzipped-richnet-website',f'{name}')


# import os

# path = r"C:\temp\myFolder\example"

# newPath = path.replace(os.sep, '/')

# print(newPath)



import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
