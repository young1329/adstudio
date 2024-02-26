'''
ADStudio V 1.0
Coded by Youngsik Kim @ CSEE . HGU

Connect AWG 1 to Scope 1

test AWG and scope functions
   Generate 1kHz sin wave and measure it with Scope1
   and plot the waveform

'''
import sys
sys.path.append("C:/vscode_ws/ws_python/adstudio")

from adstudio import Power
from adstudio import AWG
from adstudio import Scope

import time
import matplotlib.pyplot as plt

pwr=Power()
pwr.get_device_info()
pwr.print_device_info()
pwr.open_device()
pwr.reset_analogIO()


########
#AWG and Scope Test
#
# AWG armed and wait trigger
awg = AWG()
print("Created Object awg")
# configure the setup
awg.AWG_wform('AWG1','sin')
awg.AWG_freq('AWG1',1000)
awg.AWG_amp_offset('AWG1',1.5,0.0)  #Ready

awg.AWG_enable('AWG1') # Armed

awg.AWG_trig('AWG1','pc')
awg.AWG_configure('AWG1') #Wait

####
#awg.AWG_pctrig() # Trigger and Running


###
#Configure the scope to measure signal
#
sp = Scope()
sp.SCOPE_init()
# define channel 1 condition
sp.SCOPE_enable('SCOPE1')
sp.SCOPE_offset('SCOPE1',0)
sp.SCOPE_range('SCOPE1',5.0)


sp.SCOPE_pctrig() # Triggering
time.sleep(2)

sp.SCOPE_configure() # Armed

sp.SCOPE_get_data()  # Wait to measure the scope data


Ch1V = sp.Ch1Voltages
print('Finised the measurement. Close device\n')

pwr.CloseAll()

plt.plot(sp.Ch1Voltages)
plt.show()

del pwr,awg,sp
