# Simply python script to dump list of S3 buckets to a CSV file
# Boto3 documentation: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-creating-buckets.html
# To do:
# Make this a CLI operation

import csv
import boto3
from botocore.exceptions import ClientError

# Init boto3 resource for S3
# NOTE: The session is created by using creds available under ~/.aws/credentials
# For a specific profile add the 'profile_name' attribute
# For specific region add region_name param
s3 = boto3.client('s3')
# store response
response = s3.list_buckets()


def listS3buckets():
    # List all bucket names and print to terminal
    print('Active buckets:')
    for bucket in response['Buckets']:
        print(f' {bucket["Name"]}')


def writeBuckets2csv():
    with open('bucketlist.csv', 'w', newline='') as f:
        for bucket in response['Buckets']:
            s3listing = bucket["Name"]
            f.write(s3listing + '\n')


def listBucketsWithEncryption():
    for bucket in response['Buckets']:
        try:
            is_enc = s3.get_bucket_encryption(Bucket=bucket['Name'])
            rules = is_enc['ServerSideEncryptionConfiguration']['Rules']
            print('Bucket: %s, Encryption: %s' % (bucket['Name']))
        except ClientError as e:
            if e.response['Error']['Code'] == 'ServerSideEncryptionConfigurationNotFoundError':
                print('Bucket: %s, no server-side encryption' %
                      (bucket['Name']))
            else:
                print("Bucket: %s, error encountered: %s" %
                      (bucket['Name'], e))


def main():
    listS3buckets()
    writeBuckets2csv()
    listBucketsWithEncryption()


if __name__ == "__main__":
    main()
