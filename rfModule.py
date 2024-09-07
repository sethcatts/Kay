from rpi_rf import RFDevice
import schedule
import time

class lightController:
    def __init__(self):
        self.light1 = light("Light 1", 11097754, 11097746)
        self.light2 = light("Light 2", 11097756, 11097748)
        self.light3 = light("Light 3", 11097753, 11097745)
        self.light4 = light("Plant Light", 5592321, 5592323)
        print("Log: Created light controller")


class light:
    def __init__(self, name, onCode, offCode):
        self.name = name
        self.onCode = onCode 
        self.offCode = offCode
        self.on = False
        self.rfController = rfController()
        print("Log: Created a light")

    def toggle(self):
        if(self.isOn()):
            self.rfController.sendSignal(self.offCode)
            self.on = False
            print("Log: Toggled light off")
        else:
            self.rfController.sendSignal(self.onCode)
            self.on = True
            print("Log: Toggled light on")

    def isOn(self):
        return self.on

    def getName(self):
        return self.name
    
    def turnOn(self):
        self.rfController.sendSignal(self.onCode)
        self.on = True
        print("Log: Toggled light on")
    
    def turnOff(self) :
        self.rfController.sendSignal(self.offCode)
        self.on = False
        print("Log: Toggled light off")

class rfController:
    def __init__(self):
        print("Created RF controller object")

    def sendSignal(self, code):
        rfdevice = RFDevice(17)
        rfdevice.enable_tx()
        rfdevice.tx_repeat = 10
        rfdevice.tx_code(code, 1, 350, None)
        rfdevice.cleanup()
        s_string = "Sent signal: " + str(code)
        print(s_string)