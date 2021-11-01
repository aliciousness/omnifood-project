BUCKET='richnet-website'
# key='myBuild.zip'

# s3 = boto3.resource('s3')
# my_bucket = s3.Bucket(BUCKET)

# filebytes = BytesIO()

# my_bucket.download_fileobj(key, filebytes)

# file = zipfile.ZipFile(filebytes)

# file.extractall('/tmp/extract_test')

# path = 'C:/Users/cradd/tmp'

# for root, direct, files in os.walk(path):
# 	for name in files:
# 		s3.meta.client.upload_file(f'{os.path.join(root, name)}','unzipped-richnet-website',f'{name}')
# 	for name in direct:
# 		s3.meta.client.upload_file(f'{os.path.join(root, name)}','unzipped-richnet-website',f'{name}')