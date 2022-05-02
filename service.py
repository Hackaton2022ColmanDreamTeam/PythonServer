from threading import Thread
import boto3
# from credentials import AWS_SECRET_KEY, AWS_ACCESS_KEY
from datetime import datetime, timedelta
import time
import json


class Service(Thread):
<<<<<<< Updated upstream
    def __init__(self, parameter, units, aws_accesskey, aws_secretkey, instanceid, region):
=======
    def __init__(self, data, units, aws_accesskey, aws_secretkey, instance_id, region):
>>>>>>> Stashed changes
        Thread.__init__(self)
        self.response = None
        self.data = data
        self.units = units
        self.region = region
        self.AWS_ACCESS_KEY = aws_accesskey
        self.AWS_SECRET_KEY = aws_secretkey
        self.Buffer = {"Date": [], "Average": []}
<<<<<<< Updated upstream
        self.INSTANCE_ID = instanceid
        self.region = region
        self.session = boto3.Session(
            aws_access_key_id=aws_accesskey,
            aws_secret_access_key=aws_secretkey,
=======
        self.INSTANCE_ID = instance_id
        self.session = boto3.Session(
            aws_access_key_id=self.AWS_ACCESS_KEY,
            aws_secret_access_key=self.AWS_SECRET_KEY,
>>>>>>> Stashed changes
            region_name=self.region
        )
        self.ec2 = self.session.resource("ec2")
        self.client = self.session.client("cloudwatch", region_name=self.region)
        for instance in self.ec2.instances.all():
            if instance.id == self.INSTANCE_ID:
                self.serverState = instance.state
        self.responceInitialiez()

    def responceInitialiez(self):
        self.response = self.client.get_metric_statistics(
            Namespace="AWS/EC2",
            MetricName=self.data,
            Dimensions=[{"Name": "InstanceId", "Value": self.INSTANCE_ID}],
            StartTime=datetime.utcnow() - timedelta(seconds=3600),
            EndTime=datetime.utcnow(),
            Period=300,
            Statistics=[
                "Average",
            ],
            Unit=self.units,
        )

    def printServerData(self):
        for instance in self.ec2.instances.all():
            if instance.id == self.INSTANCE_ID:
                print(
                    f"""ID: {instance.id}
                           \nType: {instance.instance_type}
                           \nPublic IPv4: {instance.public_ip_address}
                           \nAMI: {instance.image.id}
                           \nState: {instance.state}
                           \n
                           """
                )

    def Json(self):

       # while self.serverState.get("Name") == 'running':
        # for x in range(3):
        #     time.sleep(1)
        while True:
            datapoints_sorted = sorted(self.response["Datapoints"], key=lambda x: x["Timestamp"])
            for datapoint in datapoints_sorted:
                str = f"{datapoint['Timestamp']}, Average: {datapoint['Average']}"
                # newStr = str +"\n"
                tmp = str.split(",")
                self.Buffer["Date"].append(tmp[0])
                tmp2 = tmp[1].strip()
                tmp3 = tmp2.split(":")
                self.Buffer["Average"].append(tmp3[1])
                # print(self.Buffer)

            # print(self.parameter)
            time.sleep(5)
            print(self.data + json.dumps(self.Buffer))
            print("here")
            # self.responceInitialiez()


    def run(self):
        self.Json()