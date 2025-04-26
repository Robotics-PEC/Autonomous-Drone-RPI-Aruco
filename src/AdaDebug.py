class AdaDebug:

    def __init__(self,ModuleName):
        self.ModuleName = ModuleName
        self.Log("Initializing Module")

    def Log(self,msg):
        print(f"{self.ModuleName} : {msg}")