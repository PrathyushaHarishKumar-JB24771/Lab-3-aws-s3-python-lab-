import boto3

s3 = boto3.client('s3')
bucket_name = 'my-boto3-s3-bucket-prathyusha12345'
file_name = 'myfile.txt'

# Create a sample file
with open(file_name, 'w') as f:
    f.write("Hello S3")

# Upload the file
s3.upload_file(file_name, bucket_name, file_name)
print(f'File {file_name} uploaded successfully!')
