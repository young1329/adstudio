'''
ADStudio V 1.0
Test for Digital IO

Digital Static IO Test
  Set the pin map : D15-D8 input / D7-D0 output
  Ouput 0x12=0001 0010   hex : 0x12 -> dex: 18
'''
import sys
sys.path.append("C:/vscode_ws/ws_python/adstudio")

from adstudio import DigitalIO
from adstudio import Power
import time
# Static Digial IO test Tutorial
pwr = Power()

#1.0 Digital IO Test : connect D4 to D8
dio = DigitalIO()
dio.get_device_info()
dio.open_device()

# reset
dio.Reset_DIO()

# D7-D0 as output D15-D8 as input
dio.SetOutputPins(0x00FF)

#D7:D0 = 0x12 measn D4=1, D1=1 and others are 0
dio.SetOutputValues(0x12) # hex 12 -> dec 18
dio.GetDigitalIOInputs()

#check the dio.InputValues.value = 274L=0x0112
# connect Vmtr3->DO4 and Vmtr4->DO2
time.sleep(1)

print(dio.InputValues.value)

dio.CloseAll()

del dio,pwr
