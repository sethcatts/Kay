from rpi_rf import RFDevice
import schedule
import time
import rfModule

con = rfModule.lightController()

def light1On():
    con.light1.turnOn()

def light1Off():
    con.light1.turnOff()

def light2On():
    con.light2.turnOn()

def light2Off():
    con.light2.turnOff()

# Turn bedside lamp on at 6:30pm
schedule.every().day.at("17:30").do(light1On)
# Turn bedside lamp off at 12:00pm
schedule.every().day.at("00:00").do(light1Off)

# Turn desk lamp on at at 06:30pm
schedule.every().day.at("17:30:01").do(light2On)
# Turn desk lamp off at 09:00pm
schedule.every().day.at("21:00").do(light2Off)

# schedule.every().day.at("19:20").do(light1On)
# schedule.every().day.at("19:20:05").do(light2On)



while True:
    schedule.run_pending()
    time.sleep(1)