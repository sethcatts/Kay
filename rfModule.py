from rpi_rf import RFDevice

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
    def isOn(self):
        return self.on
    def getName(self):
        return self.name

class rfController:
    def __init__(self):
        print("Created RF Controller")
        light1Status = False
        light2Status = False
        light3Status = False


    def sendSignal(self, code):
        rfdevice = RFDevice(17)
        rfdevice.enable_tx()
        rfdevice.tx_repeat = 10
        rfdevice.tx_code(code, 1, 200, None)
        rfdevice.cleanup()