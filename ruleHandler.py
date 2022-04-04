import imp
from InstancesFunction import InstancesFunctions
import Model_EC2
from rule import Rule
import service
from threading import Thread

class ruleHandler(Thread):

    def __init__(self, model_ec2):
        self.model_EC2 = model_ec2
        self.insCre = InstancesFunctions()
        self.rules = []

    def addRule(self, rule):
        parts = rule.split("/")

        rule = Rule()
        rule.serverType = parts[0]
        rule.Data = parts[1]
        rule.Command = parts[2]
        rule.TH = parts[3]
        self.rules.append(rule)
        return '{ "value":"true" }'

    def removeRule(self, rule):
        parts = rule.split("/")
        for r in self.rules:
            if(r.serverType == parts[0] and r.Data == parts[1] and r.Command == parts[2] and r.TH == parts[3]):
                self.rules.remove(rule)
                
        return '{ "value":"true" }'

    def handleRules(self):
        while True:
            for r in self.rules:
                r.Execute()



    def createInstance(self):
        self.insCre.InstanceCreator() 

    def removeInstance(self):
        self.insCre.InstanceRemover() 

    def stopInstance(self):
        self.insCre.InstanceStoper() 

    def run(self):
        self.handleRules()