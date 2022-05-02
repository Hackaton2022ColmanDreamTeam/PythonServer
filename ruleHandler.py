import imp
from queue import Queue
from InstancesFunction import InstancesFunctions
import Model_EC2
from rule import Rule
import service
from threading import Thread


class RuleHandler(Thread):

    def __init__(self, model_ec2, dict):
        Thread.__init__(self)
        self.numOfRules = 1
        self.idgenrators = 1
        self.rulesDict = { 'Rule id - 1': dict}
        self.rules = [Rule(dict['Type'], dict['Action'], dict['Data'], dict['Threshold']), self.idgenrators]
        self.model_EC2 = model_ec2
        self.insCre = InstancesFunctions()
        self.dict_parameters = dict

    def addRule(self, ruledict):

        self.numOfRules += 1
        self.idgenrators += 1
        rule = Rule(ruledict['Type'], ruledict['Action'], ruledict['Data'], ruledict['Threshold'], self.idgenrators)
        self.rules.append(rule)
        tmprule = 'Rule id'
        self.rulesDict[tmprule] = ruledict
        return '{ "value":"true" }'

    def removeRule(self, ruledict):
        for r in self.rulesDict.keys():
            if(self.getRuleById(ruledict) == self.rulesDict.get(r)['Rule id']):
                self.rulesDict.pop(r)
        for r in self.rules:
            if(self.getRuleById(ruledict) == r.getRuleId()):
                self.rules.remove(r)
                self.numOfRules -= 1

        return '{ "value":"true" }'

    def handleRules(self):
        while True:
            if(self.numOfRules >= 1):
                data = self.rulesString.get()

    def getRuleById(self, ruledict):
        for r in self.rulesDict.keys():
            if(ruledict['Type'] == self.rulesDict.get(r)['Type'] and ruledict['Action'] == self.rulesDict.get(r)['Action'] and ruledict['Data'] == self.rulesDict.get(r)['Data'] and ruledict['Threshold'] == self.rulesDict.get(r)['Threshold']):
                return self.rulesDict.get(r)['Rule id']
        return -1

    def createInstance(self,str):
        self.insCre.InstanceCreator(str) 

    def removeInstance(self, str):
        self.insCre.InstanceRemover(str) 

    def stopInstance(self,str):
        self.insCre.InstanceStoper(str) 

    def run(self):
        self.handleRules()