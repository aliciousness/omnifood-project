
  #this script unzips files from one bucket and sends all files to another bucket using lambda  

'''
import zipfile,boto3,os
from io import BytesIO




BUCKET='richnet-website'
key='myBuild.zip'

s3 = boto3.resource('s3')
my_bucket = s3.Bucket(BUCKET)

filebytes = BytesIO()

my_bucket.download_fileobj(key, filebytes)

file = zipfile.ZipFile(filebytes)

file.extractall('/tmp') # where everywhere you want it to go, /tmp is for aws lambda only IMPORTANT

path = '/tmp'

#on mac
for root,dirs,files in os.walk(path):
  for name in files:
    s3.meta.client.upload_file(os.path.join(root, name),'unzipped-richnet-website',name)
    
'''

# on windows IMPORTANT
# for root, dirs, files in os.walk(path):
# 	for name in files:
#     old = r'{}'.format(os.path.join(root, name)) 
#     newPath = old.replace(os.sep,'/')[29::]
#     s3.meta.client.upload_file(old,'unzipped-richnet-website',key)
  
  

  








