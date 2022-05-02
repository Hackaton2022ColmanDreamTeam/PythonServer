
from threading import Thread
import Model_EC2
import serverThreadHandler
from ruleHandler import RuleHandler
from queue import Queue
from view import View
from Controller import Controller
from httpController import HttpController

def main():
    ec2Model = Model_EC2.EC2_Model("i-0770a3d5074a2ca34", "us-west-1")
    # qRules = Queue()
    # ruleHandler = RuleHandler(ec2Model,qRules)
    # s1 = serverThreadHandler.threadHandler(7000)
    # s1.start()


    
    # ruleHandler.start()
    ec2Model.StartOne("CPUUtilization")
    ec2Model.StartOne("DiskReadOps")
    # s1.start()

    # obj.StartAll()


if __name__ == "__main__":
<<<<<<< Updated upstream
    controller = Controller()
    view = View(controller)
    view.start()
=======
    conroller = Controller()
    view = View(conroller)
    view.start()
    # main()
>>>>>>> Stashed changes
