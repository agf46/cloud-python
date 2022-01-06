# Simple python script to get all roles in a given AWS env
# To do:
# - List Groups a user belongs to
# - List Policies associated with user


import boto3
import csv

# Init IAM boto3 resource to list roles
# NOTE: The session is created by using creds available under ~/.aws/credentials
# For a specific profile add the 'profile_name' attribute
iam_roles = boto3.resource('iam')
iam = boto3.client('iam')
roles = iam_roles.roles.all()


def listAllUsers():
    # Using paginator here. Optional if a small env
    paginator = iam.get_paginator('list_users')
    for response in paginator.paginate():
        for user in response["Users"]:
            print(f"Username: {user['UserName']}, Arn: {user['Arn']}")


def listIAMRoles():
    for role in roles:
        roleslist = role.role_name
        print(roleslist)


def writeIAMRolestoCSV():
    # write to csv file
    with open('rolelist.csv', 'w', newline='') as f:
        for role in roles:
            roleslist = role.role_name
            f.write(roleslist + '\n')


def main():
    # List all IAM users in Username: Arn: format
    print("List all IAM users:\n")
    listAllUsers()
    print("Listing all account roles: \n")
    # call listIAMRoles func
    listIAMRoles()
    print("\nWriting to csv file rolelist.csv..")
    writeIAMRolestoCSV()


if __name__ == "__main__":
    main()
