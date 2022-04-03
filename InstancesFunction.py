import boto3
import constant #add another python file for the keys

#Should get the Instance ID for those functions except the creation.
class InstancesFunctions:


    # def __init__(self,AWSAccess_Key,AWSSecret_Key):
    #     self.AWSAccessKey = AWSAccess_Key
    #     self.AWSSecretKey = AWSSecret_Key
    #     self.Instance = ""


    # def SetIntanceID(self,ID):
    #     self.Instance = ID


    def InstanceRemover():
        # connect to the client using the keys
        # insert your own keys below
        ec2 = boto3.client('ec2',
                            'us-east-1',
                            aws_access_key_id = constant.AWS_ACCESS_KEY,
                            aws_secret_access_key = constant.AWS_SECRET_KEY)


        InstanceID2Remove = ["i-0251898ab21ce07ba"] # ec2 instance ID for example


        # Terminate ec2 instance
        ec2.terminate_instances(InstanceIds = InstanceID2Remove)
        print("Removed the Instance")


    def InstanceStoper():
            # connect to the client using the keys
        # insert your own keys below
        ec2 = boto3.client('ec2',
                            'us-east-1',
                            aws_access_key_id = constant.AWS_ACCESS_KEY,
                            aws_secret_access_key = constant.AWS_SECRET_KEY)


        InstanceID2Remove = ["i-0251898ab21ce07ba"] # ec2 instance ID for example


        # Terminate ec2 instance
        ec2.stop_instances(InstanceIds = InstanceID2Remove)
        print("Stopped the Instance")


    def InstaceStarter():
            # connect to the client using the keys
        # insert your own keys below
        ec2 = boto3.client('ec2',
                            'us-east-1',
                            aws_access_key_id = constant.AWS_ACCESS_KEY,
                            aws_secret_access_key = constant.AWS_SECRET_KEY)


        InstanceID2Remove = ["i-0251898ab21ce07ba"] # ec2 instance ID for example


        # Terminate ec2 instance
        ec2.start_instances(InstanceIds = InstanceID2Remove)
        print("Started the Instance")


    def InstanceCreator():
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

        print("Instance created")



    # InstanceCreator()
    # InstanceStoper()
    # InstaceStarter()
    # InstanceRemover()