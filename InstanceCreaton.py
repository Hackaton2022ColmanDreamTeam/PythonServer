import boto3
import constant

class InstanceCreator:

    # connect to the client using the keys
    # insert your own keys below
    ec2 = boto3.client('ec2',
                        'us-east-1',
                        aws_access_key_id = constant.AWS_ACCESS_KEY,
                        aws_secret_access_key = constant.AWS_SECRET_KEY)



    #create a new ec2 instance
    # t2.micro/ami-0c02fb55956c7d316  - free tier  
    conn = ec2.run_instances(InstanceType="t2.micro",
                            MaxCount = 1,
                            MinCount = 1,
                            ImageId = "ami-0c02fb55956c7d316")

