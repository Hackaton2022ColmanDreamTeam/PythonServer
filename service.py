import boto3
from credentials import AWS_ACCESS_KEY, AWS_SECRET_KEY
from datetime import datetime, timedelta
import time
import json


class Service:
    def __init__(self, parameter, units):
        self.response = None
        self.parameter = parameter
        self.units = units
        self.Buffer = {"Date": [], "Average": []}
        self.INSTANCE_ID = "i-075b0fe0809290316"
        self.session = boto3.Session(
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY,
            region_name='us-east-1'
        )
        self.ec2 = self.session.resource("ec2")
        self.client = self.session.client("cloudwatch", region_name="us-east-1")
        for instance in self.ec2.instances.all():
            if instance.id == self.INSTANCE_ID:
                self.serverState = instance.state
        self.responceInitialiez()

    def responceInitialiez(self):
        self.response = self.client.get_metric_statistics(
            Namespace="AWS/EC2",
            MetricName=self.parameter,
            Dimensions=[{"Name": "InstanceId", "Value": self.INSTANCE_ID}],
            StartTime=datetime.utcnow() - timedelta(seconds=120),
            EndTime=datetime.utcnow(),
            Period=60,
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
        for x in range(5):
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

            time.sleep(60)
            self.responceInitialiez()
            print(self.parameter + json.dumps(self.Buffer))
