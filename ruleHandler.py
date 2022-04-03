import string
import Model_EC2
import service
import Rule as r


class ruleHandler:

    def __init__(self, model_ec2:Model_EC2,rules:list):
        self.model_EC2 = model_ec2
        self.Rules = rules

    def addRule(self, rule):
        list:list =  rule.split('/')
        Command = list[0] #create 
        Data = list[1] #cpu
        TH = list[2] 
        CurrentRule = r.Rule(Command,Data,TH,self.model_EC2)
        self.Rules.append(CurrentRule)
        return CurrentRule.Execute()
