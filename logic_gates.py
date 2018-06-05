class LogicGate:  # All gates implement the LogicGate Class
    def __init__(self,name): #Contains NAME,OUTPUT
        self.name = name
        self.output = None

    def getOutput(self):
        self.output = self.performLogic()
        return self.output

class BinaryGate(LogicGate): # All Binary gates implement this class
    def __init__(self,name): # Contains 2 pins, pin1 and pin2
        LogicGate.__init__(self,name)
        self.pin1 = None
        self.pin2 = None

    def getPin1(self):
        if self.pin1 ==None:
            return int(input("Enter pin1 value for " + self.name + " : "))
        elif self.pin1 ==1 or self.pin1 ==0:
            return self.pin1
        else:
            return self.pin1.getOutput()
    def getPin2(self):
        if self.pin2 ==None:
            return int(input("Enter pin2 value for " + self.name + " : "))
        elif self.pin2 ==1 or self.pin2 ==0:
            return self.pin2
        else:
            return self.pin2.getOutput()
    def setInput(self,fromGate):
        if self.pin1 == None:
            self.pin1 = fromGate
        else:
            if self.pin2 == None:
                self.pin2 = fromGate
            else:
                raise RuntimeError("No empty pins")

class UnaryGate(LogicGate): # All Binary gates implement this class
    def __init__(self,name):# Contains 1 pin, pin1 
        LogicGate.__init__(self,name)
        self.pin1 = None
    def getPin1(self):
        if self.pin1 ==None:
            return int(input("Enter pin1 value for " + self.name + " : "))
        elif self.pin1 ==1 or self.pin1 ==0:
            return self.pin1
        else:
            return self.pin1.getOutput()

    def setInput(self,fromGate):
        if self.pin1 == None:
            self.pin1 = fromGate
        else:
            raise RuntimeError("No empty pins")

class NOTGate(UnaryGate):
    def __init__(self,name):
        UnaryGate.__init__(self,name)
    def performLogic(self):
        self.pin1 = self.getPin1()
        if self.pin1 == 1:
            return 0
        else:
            return 1

class ANDGate(BinaryGate):
    def __init__(self,name):
        BinaryGate.__init__(self,name)
    def performLogic(self):
        self.pin1 = self.getPin1()
        self.pin2 = self.getPin2()
        return self.pin1 * self.pin2

class ORGate(BinaryGate):
    def __init__(self,name):
        BinaryGate.__init__(self,name)
    def performLogic(self):
        self.pin1 = self.getPin1()
        self.pin2 = self.getPin2()
        if self.pin1 == 1 or self.pin2 ==1:
            return 1
        else:
            return 0

class NORGate(BinaryGate): # Contains inbuilt OR and NOT gate
    def __init__(self,name):
        BinaryGate.__init__(self,name)
        self.orgate = ORGate("orgate in NORGate")
        self.notgate = NOTGate("notgate in NORGate")
        self.norgatewire = Wire(self.orgate, self.notgate)
    def performLogic(self):
        self.orgate.pin1 = self.pin1
        self.orgate.pin2 = self.pin2
        self.orgate.pin1 = self.getPin1()
        self.orgate.pin2 = self.getPin2()
        self.pin2 = self.pin2.getPin2()
        return self.notgate.getOutput()

class NANDGate(BinaryGate): # Contains inbuilt AND and NOT gate
    def __init__(self,name):
        BinaryGate.__init__(self,name)
        self.andgate = ANDGate("andgate in NANDGate")
        self.notgate = NOTGate("notgate in NANDGate")
        self.nandgatewire = Wire(self.andgate, self.notgate)
    def performLogic(self):
        self.andgate.pin1 = self.pin1
        self.andgate.pin2 = self.pin2
        self.andgate.pin1 = self.getPin1()
        self.andgate.pin2 = self.getPin2()
        self.pin2 = self.pin2.getPin2()
        return self.notgate.getOutput()



class Wire: # This class is a helper class to set one output to another gate's input
    def __init__(self,gate1,gate2):
        self.fromGate = gate1
        self.toGate = gate2

        self.toGate.setInput(self.fromGate) 

and1 = ANDGate("and1")
or1 = ORGate("or1")
or2 = ORGate("or2")
nand1 = NANDGate("nand1")
nor1 = NORGate("nor1")
not1 = NOTGate("not1")

wire1 = Wire(and1, nor1)
wire2 = Wire(and1, nand1)
wire3 = Wire(or1, nor1)
wire4 = Wire(or1, nand1)
wire5 = Wire(nor1, or2)
wire6 = Wire(nand1, or2)
wire7 = Wire(or2, not1)

finalOutput = not1.getOutput()

print("Final Output = ", finalOutput)