from rpi_rf import RFDevice

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

class light:
    def __init__(self):
        print("Creating a light")