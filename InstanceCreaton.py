import boto3
<<<<<<< Updated upstream
import constant
from credentials import AWS_ACCESS_KEY, AWS_SECRET_KEY
=======
# import constant
from credentials import AWS_SECRET_KEY, AWS_ACCESS_KEY
>>>>>>> Stashed changes

class InstanceCreator:

    def __init__(self, region, accesskey, secretkey, ami):
        self.region = region
        self.accesskey =accesskey
        self.secretkey = secretkey
        self.ami = ami
    # connect to the client using the keys
    # insert your own keys below
<<<<<<< Updated upstream
    # ec2 = boto3.client('ec2',
    #                     'us-west-1',
    #                     aws_access_key_id = AWS_ACCESS_KEY,
    #                     aws_secret_access_key = AWS_SECRET_KEY)
=======
    ec2 = boto3.client('ec2',
                        'us-west-1',
                        aws_access_key_id = AWS_ACCESS_KEY,
                        aws_secret_access_key = AWS_SECRET_KEY)
>>>>>>> Stashed changes



    #create a new ec2 instance
    # t2.micro/ami-0c02fb55956c7d316  - free tier
    def createInstance(self):
        ec2 = boto3.client('ec2',
                           self.region,
                           aws_access_key_id=self.accesskey,
                           aws_secret_access_key=self.secretkey)

        conn = ec2.run_instances(InstanceType="t2.micro",
                            MaxCount = 1,
                            MinCount = 1,
<<<<<<< Updated upstream
                            ImageId = self.ami)
=======
                            ImageId = "ami-09625adacc474a7b4")
>>>>>>> Stashed changes

