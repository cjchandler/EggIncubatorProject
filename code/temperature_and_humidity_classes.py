
from Phidget22.Phidget import *
from Phidget22.Devices.VoltageRatioInput import *
from Phidget22.Devices.TemperatureSensor import *
from Phidget22.Devices.HumiditySensor import *
from Phidget22.Devices.DigitalInput import *

import time
import csv
import collections
import datetime
import pandas as pd
import power
import numpy as np

class handler_temperature_and_humidity:
    def __init__(self):
        self.time_of_last_humidity_change = 0
        self.time_of_last_temperature_change = 0
        self.temperature = np.sqrt(-300)
        self.humidity = np.sqrt(-1)

    def onTemperatureChangeInsideAir(self,self2, temperature):
        # print("Temperature: " + str(temperature))
        self.temperature = temperature
        self.time_of_last_temperature_change = time.time()

    def onHumidityChangeInsideAir(self,self2, humidity):
        # print("Temperature: " + str(temperature))
        self.humidity = humidity
        self.time_of_last_humidity_change = time.time()

class temperature_humidity_phidget_channel: #I use this for PAR reading in, analog input
    def __init__(self, serial_number, port ):
        self.serial_number = serial_number
        # self.signal_temperature = 0.0
        # self.signal_humidity = 0.0
        # self.n_temperature = 0
        # self.n_humidity = 0
        self.handler = handler_temperature_and_humidity()
        self.port = port
        self.temperatureSensor = TemperatureSensor()
        self.humiditySensor = HumiditySensor()

    def startup(self ):
        self.temperatureSensor.setHubPort(self.port)
        self.temperatureSensor.setDeviceSerialNumber(self.serial_number)
        self.humiditySensor.setHubPort(self.port)
        self.humiditySensor.setDeviceSerialNumber(self.serial_number)
        self.temperatureSensor.setOnTemperatureChangeHandler(self.handler.onTemperatureChangeInsideAir)
        self.humiditySensor.setOnHumidityChangeHandler(self.handler.onHumidityChangeInsideAir)
        self.temperatureSensor.openWaitForAttachment(10000)
        self.humiditySensor.openWaitForAttachment(10000)


    def shutdown(self):
        self.temperatureSensor.close()
        self.humiditySensor.close()

    def getTemperature(self):
        temperature_c= self.handler.temperature
        return temperature_c

    def getHumidity(self):
        humidity_percent= self.handler.humidity
        return humidity_percent*0.01

#testing inside temperature and humidity sensor
def testTemperatureHumidity():
    insideTemperatureHumidity = temperature_humidity_phidget_channel(681710, 4)
    insideTemperatureHumidity.startup()
    while True:
        print( insideTemperatureHumidity.getTemperature() )
        print( insideTemperatureHumidity.getHumidity() )
        time.sleep(2)
        
#testTemperatureHumidity()
