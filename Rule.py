


from tokenize import Double
from InstancesFunction import InstancesFunctions
from Model_EC2 import EC2_Model


class Rule:
    

    def __init__(self,command,data,tresh,Model:EC2_Model):
        self.Command = command
        self.Data = data
        self.TH = tresh
        self.MODEL = Model


    
    def Execute(self):
        if self.Data == 'CPUUtilization':
            self.MODEL.StartOne('CPUUtilization')
            CPU_Result = self.MODEL.GetCPUData()
            if self.Command == 'remove':
                if Double(self.TH) > Double(CPU_Result):
                    InstancesFunctions.InstanceRemover()
                    print('Removed the instance')
                    return True
            elif self.Command == 'create':
                if Double(self.TH) < Double(CPU_Result):
                    InstancesFunctions.InstanceCreator()
                    print('Created new instance')
                    return True
            else: 
                return False
        elif self.Data == 'DiskReadOps':
            self.MODEL.StartOne('DiskReadOps') 
            #add io getter
        else:
            self.MODEL.StartAll()
            #add cpu and io getter



    