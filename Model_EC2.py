# import threading
import threading
from threading import *
from multiprocessing import process, Process

import service
from threading import Thread

import boto3
from credentials import AWS_ACCESS_KEY, AWS_SECRET_KEY
from datetime import datetime, timedelta
import time
import json


# class StartThread(Thread):
#     def __init__(self, ser):
#         self.service = ser
#
#     def run(self):
#         #time.sleep(2)
#         self.service.Json()
#         #time.sleep(2)


class EC2_Model:

    def __init__(self):
        self.rules = []
        self.cpuSer = service.Service("CPUUtilization", "Percent")
        self.IoSer = service.Service("DiskReadOps", "Count")
        self.netPacOutSer = service.Service("NetPacketOut", "Count")
        self.serviceArray = [self.IoSer, self.cpuSer]

    def StartAll(self):
        # results = []
        # thread_list = []
        # for ser in self.serviceArray:
        #     t1 = threading.Thread(target=ser.Json(), args=(ser, results))
        #     thread_list.append(t1)
        # for t1 in thread_list:
        #     t1.start()
        # for t1 in thread_list:
        #     t1.join()

        processes = []
        for ser in self.serviceArray:
            p1 = Process(target=ser.Json())
            processes.append(p1)
        for p in processes:
            p.start()
        for p in processes:
            p.join()

            # # x = StartThread(ser)
            # # x.run()
            # # time.sleep(2)
            # class StartTheard(Thread):
            #     def run(self):
            #         print("start")
            #         ser.Json()
            #
            # x = StartTheard()
            # x.start()
            # time.sleep(1)
            # x.join()

    def StartOne(self, serviceName):
        for ser in self.serviceArray:
            if ser.parameter == serviceName:
                x = StartThread(ser)
                x.run()
