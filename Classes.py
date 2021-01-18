#Parent Class
class Vehicle:
    def __init__(self,make,model,year,weight,NeedsMaintainence=False):
        self.make=make
        self.year=year
        self.year=year
        self.weight=weight
    
    def setMake(self,make):
        self.make=make
        return self.make
    
    def setModel(self,model):
        self.model=model
        return self.model
    
    def setYear(self,year):
        self.year=year
    
    def setWeight(self,weight):
        self.weight=weight
        return self.weight

#Cars inheriet Vehicle
class Cars(Vehicle):
    def __init__(self,make,model,year,weight,NeedsMaintainence=False,TripsSinceMaintenance=0):
        Vehicle.__init__(self,make,model,year,weight)
    
    def Drive(self,isDriving,TripsSinceMaintenance):
        self.isDriving=True
        TripsSinceMaintenance+=1
        if TripsSinceMaintenance >=100:
            self.NeedsMaintainence=True
            return self.NeedsMaintainence
        return TripsSinceMaintenance
    
    def Stop(self,isDriving):
        self.isDriving=False
    
    def Repair(self,TripsSinceMaintenance,NeedsMaintainence):
        self.TripsSinceMaintenance=0
        self.NeedsMaintainence=False
    
   
newcar=Cars("Gen1","YMZ",1990,1000)

d=newcar.Drive(True,101)
newcar.Repair(101,True)
print(d)

class Planes(Vehicle):
    def __init__(self,make,model,year,weight,NeedsMaintainence=False):
        Vehicle.__init__(self,make,model,year,weight)
    
    def Flying(self,NeedsMaintainence):
        if NeedsMaintainence== False:
            return False
        else:
            return True
    
    def Landing(self,NeedsMaintainence):
        pass

    def Repair(self,NeedsMaintainence):
        self.NeedsMaintainence=False


p=Planes('Boeing',757,2010,1000)
print(p.Flying(False))



