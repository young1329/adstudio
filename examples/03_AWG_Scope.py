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
import numpy as np
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
sp.SCOPE_range('SCOPE1',10.0)
sp.SCOPE_trigsrc('detectoranalogin')
sp.SCOPE_trigtype('edge')
sp.SCOPE_configure() # Armed
print('Scope Configured\n')
awg.AWG_pctrig() # Triggering
# sp.SCOPE_pctrig()
time.sleep(1)
sp.SCOPE_get_data()  # Wait to measure the scope data

fs=sp.sampling_freq.value # sampling frequency
N=sp.num_of_samples.value # number of samples
Ch1V = np.array(sp.Ch1Voltages)
ts = np.arange(0,N/fs,1/fs)
print('Finised the measurement. Close device\n')

pwr.CloseAll()

del pwr,awg,sp

plt.plot(ts,Ch1V,label='Scope 1')
plt.xlabel('Time(sec)')
plt.ylabel('Volt(V)')
plt.grid('both')
plt.legend()
plt.show()


