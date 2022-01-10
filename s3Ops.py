# Simply python script to dump list of S3 buckets to a CSV file
# Boto3 documentation: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-creating-buckets.html
# To do:
# - Add Error handling with botocore if we want to get really fancy with it

import csv
import boto3

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


def main():
    listS3buckets()
    writeBuckets2csv()


if __name__ == "__main__":
    main()
