from Phidget22.Phidget import *
from Phidget22.Devices.DigitalOutput import *
import time


class fan:
    def __init__(self):
        self.fan_on = 0
        self.digitalOutput1 = DigitalOutput()
        
    def startup(self,hubserial, hubport , channel):
    

        self.digitalOutput1.setHubPort(hubport)
        self.digitalOutput1.setDeviceSerialNumber(hubserial)
        self.digitalOutput1.setChannel(channel)
        

        self.digitalOutput1.openWaitForAttachment(5000)
        

        self.digitalOutput1.setDutyCycle(0)
        
    def command_fan(self, state_wanted):
        self.fan_on = state_wanted
        self.digitalOutput1.setDutyCycle(self.fan_on)
    

class humidifyer:
    def __init__(self):
        self.fog_on = 0
        self.digitalOutput1 = DigitalOutput()
        
    def startup(self,hubserial, hubport , channel):
    

        self.digitalOutput1.setHubPort(hubport)
        self.digitalOutput1.setDeviceSerialNumber(hubserial)
        self.digitalOutput1.setChannel(channel)
        

        self.digitalOutput1.openWaitForAttachment(5000)
        

        self.digitalOutput1.setDutyCycle(0)
        
    def command_humidifyer(self, state_wanted):
        self.fog_on = state_wanted
        self.digitalOutput1.setDutyCycle(self.fog_on)


# ~ f = fan()
# ~ for n in range(10000):
	# ~ f.command_fan(1)
	# ~ f.command_fan(0)
	# ~ f.command_fan(0)
	# ~ f.command_fan(0)
	# ~ f.command_fan(0)
	# ~ f.command_fan(0)
	# ~ f.command_fan(0)
	# ~ f.command_fan(0)

# ~ h = humidifyer()
# ~ f.command_fan(0)
# ~ h.command_humidifyer(0)

# ~ time.sleep(10)

# ~ quit()

# ~ def main():
    # ~ digitalOutput1 = DigitalOutput()
    

    # ~ digitalOutput1.setHubPort(2)
    # ~ digitalOutput1.setDeviceSerialNumber(672487)
    # ~ digitalOutput1.setChannel(1)
    

    # ~ digitalOutput1.openWaitForAttachment(5000)
    

    # ~ digitalOutput1.setDutyCycle(1)


    # ~ digitalOutput2 = DigitalOutput()
    

    # ~ digitalOutput2.setHubPort(2)
    # ~ digitalOutput2.setDeviceSerialNumber(672487)
    # ~ digitalOutput2.setChannel(2)
    

    # ~ digitalOutput2.openWaitForAttachment(5000)
    

    # ~ digitalOutput2.setDutyCycle(1)

    # ~ try:
        # ~ input("Press Enter to Stop\n")
    # ~ except (Exception, KeyboardInterrupt):
        # ~ pass

    # ~ digitalOutput1.close()
    # ~ digitalOutput2.close()


# ~ main()
