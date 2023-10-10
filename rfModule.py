from rpi_rf import RFDevice

#lightController.light1.toggle()

#TODO: Add on/off codes
class lightController:
    def __init__(self):
        light1 = light("Light 1", 0, 0)
        light2 = light("Light 2", 0, 0)
        light3 = light("Light 3", 0, 0)
        print("Created light controller")

class light:
    def __init__(self, name, onCode, offCode):
        self.name = name
        self.onCode = onCode 
        self.offCode = offCode
        self.on = false
        self.rfController = rfController()
        print("Created a light")

    def toggle(self):
        if(self.isOn()):
            self.rfController.sendSignal(self.offCode)
            self.on = false
        else:
            self.rfController.sendSignal(self.onCode)
            self.on = true

    def isOn(self):
        return self.on

    def getName(self):
        return self.name

class rfController:
    def __init__(self):
        print("Created RF controller object")

    def sendSignal(self, code):
        print("Sent signal: " + code)
        rfdevice = RFDevice(17)
        rfdevice.enable_tx()
        rfdevice.tx_repeat = 10
        rfdevice.tx_code(code, 1, 200, None)
        rfdevice.cleanup()