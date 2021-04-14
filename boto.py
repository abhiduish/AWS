import boto3

s3 = boto3.client('s3')

response = s3.list_buckets()

buckets = [bucket['Name'] for bucket in response['Buckets']]

print("Bucket List: %s" % buckets)

def create_bucket(bucket_name,region):
        s3_client = boto3.client('s3', region_name=region)
        location = {'LocationConstraint': region}
        s3_client.create_bucket(Bucket=bucket_name,CreateBucketConfiguration=location)

#create_bucket('abhi9644','ap-south-1')

def Upload(name):
    s3=boto3.resource('s3')
    data = open("C:/Users/my/PycharmProjects/f_project/bacode.py", 'rb')
    s3.Bucket(name).put_object(Key='bacode.py', Body=data)
    print("File Upload on {} Bucket Successfully".format(name))

# Upload('abhi9644')

def Delete(bucketname,filename):
    s3 = boto3.resource('s3')
    s3.Object(bucketname, filename).delete()
    print("File {} delete from {} Bucket Successfully".format(filename,bucketname))

Delete('abhi9644','C:/Users/my/PycharmProjects/f_project/bacode.py')