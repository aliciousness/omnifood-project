# import os

# path = 'c:/Python39/lib/os.py'
# #tpyeError: expected str, bytes or os.pathlike obj, not dict. This path does not work in powershell 

# for root, directories, files in os.walk(path, topdown=False):
# 	for name in files:
# 		print(os.path.join(root, name))
# 	for name in directories:
# 		print(os.path.join(root, name))
#----------------------------------------------------------------------------------------------------------------------------------------
import boto3 
zip = client.get_object(Bucket='richnet-website',Key='myBuild.zip') 
for f in zip:
      print(f)
      

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

# mem buffer
filebytes = BytesIO()

# download to the mem buffer
my_bucket.download_fileobj(key, filebytes)

# create zipfile obj
file = zipfile.ZipFile(filebytes)

# extact to local C: drive
file.extractall('/tmp/extract_test')

path = '/tmp/extract_test'

for root, direct, files in os.walk(path, topdown=False):
	for name in files:
		s3.meta.client.upload_file(f'{os.path.join(root, name)}','unzipped-richnet-website',f'{name}')
	for name in direct:
		s3.meta.client.upload_file(f'{os.path.join(root, name)}','unzipped-richnet-website',f'{name}')
