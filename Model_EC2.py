import threading
import service

import boto3
from credentials import AWS_ACCESS_KEY, AWS_SECRET_KEY
from datetime import datetime, timedelta
import time
import json


class EC2_Model:

    def __init__(self):
        self.cpuSer = service.Service("CPUUtilization", "Percent")
        self.IoSer = service.Service("DiskReadOps", "Count")
        self.serviceArray = [self.IoSer, self.cpuSer]

    def StartAll(self):
        for ser in self.serviceArray:
            t1 = threading.Thread(target=ser.Json())
            t1.start()

    def StartOne(self, serviceName):
        for ser in self.serviceArray:
            if ser.parameter == serviceName:
                t1 = threading.Thread(target=ser.Json())
                t1.start()



