
import boto3
from credentials import AWS_ACCESS_KEY, AWS_SECRET_KEY

INSTANCE_ID = "i-075b0fe0809290316"

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name='us-east-1'
)

ec2 = session.resource("ec2")

for instance in ec2.instances.all():
    if instance.id == INSTANCE_ID:
        print(
            f"""ID: {instance.id}
            \nType: {instance.instance_type}
            \nPublic IPv4: {instance.public_ip_address}
            \nAMI: {instance.image.id}
            \nState: {instance.state}
            \n
            """
        )