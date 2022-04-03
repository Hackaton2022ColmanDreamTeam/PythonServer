import threading

import boto3
from credentials import AWS_ACCESS_KEY, AWS_SECRET_KEY
from datetime import datetime, timedelta
import time


class EC2Model:
    def __init__(self):
        self.Buffer = []
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
            MetricName="CPUUtilization",
            Dimensions=[{"Name": "InstanceId", "Value": self.INSTANCE_ID}],
            StartTime=datetime.utcnow() - timedelta(seconds=120),
            EndTime=datetime.utcnow(),
            Period=60,
            Statistics=[
                "Average",
            ],
            Unit="Percent",
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

    def printCPUuse(self):
        # for datapoint in self.response["Datapoints"]:
        #     if "Average" in datapoint:
        #         print(f"Time: {datapoint['Timestamp']}, Average: {datapoint['Average']}")

        # sort the datapoints by timestamp
        # while self.serverState.get("Name") == 'running':
        for x in range(5):
            datapoints_sorted = sorted(self.response["Datapoints"], key=lambda x: x["Timestamp"])
            for datapoint in datapoints_sorted:
                str = f"{datapoint['Timestamp']}, Average: {datapoint['Average']}"
                # newStr = str +"\n"
                self.Buffer.append(str)
                print(self.Buffer)

            self.Buffer.clear()
            time.sleep(60)
            self.responceInitialiez()

    def runServerandPrintData(self):
        t1 = threading.Thread(target=self.printCPUuse())
        t1.start()


object = EC2_Model()
object.printServerData()
object.runServerandPrintData()
