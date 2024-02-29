'''
ADStudio V 1.0
Coded By Youngsik Kim @ CSEE . HGU

Test the Power supply and Voltage meter function

 Set V+ : 4.0V
     V- : -3.0V

     V+--<R1=2k>--+Ch1--<R2=1k>--->GND
'''
import sys
sys.path.append("C:/vscode_ws/ws_python/adstudio")

from adstudio import Power
from adstudio import Scope
import time
import numpy as np

pwr=Power()
pwr.get_device_info()
pwr.print_device_info()

pwr.open_device()

pwr.reset_analogIO()

#get the number of channels for AnalogIO
pwr.get_number_of_channels()
Nch=5


# Print All Channels of Power object
print('Channels are V+(0), V-(1), USB(2), Aux(3), V+-(4)\n')
for idx in range(Nch):
    pwr.get_nodes_of_channels(idx)

# print all nodes of channel=0(V+) device
pwr.get_nodes_of_channels(0)
print('Nodes for V+ are Enable(0), Voltage(1), Current(2)\n')
for idx in range(3):
    pwr.what_is_channel_node(0,idx)

pwr.get_nodes_of_channels(1)
print('Nodes for V- are Enable(0), Voltage(1), Current(2)\n')
for idx in range(3):
    pwr.what_is_channel_node(1,idx)

pwr.get_nodes_of_channels(2)
print('Nodes for USB Monitor are Voltage(0), Current(1), Always(2)\n')
for idx in range(4):
    pwr.what_is_channel_node(2,idx)

pwr.get_nodes_of_channels(3)
print('Nodes for Aux Monitor are Voltage(0), Current(1)\n')
for idx in range(2):
    pwr.what_is_channel_node(3,idx)

pwr.get_nodes_of_channels(4)
print('Node for V+- is Limit(0)\n')
pwr.what_is_channel_node(4,0)

# Configure V+=4V, V-=-3V
pwr.set_channel_voltage('V+',4.0)
pwr.set_channel_voltage('V-',-3.0)

pwr.enable_channel('V+')
pwr.enable_channel('V-')

pwr.analogIO_configure()


#Configure the scope to measure signal
#
sp = Scope()
sp.SCOPE_init()
# define channel 1 condition
sp.SCOPE_enable('SCOPE1')
sp.SCOPE_offset('SCOPE1',0)
sp.SCOPE_range('SCOPE1',5.0)
sp.SCOPE_trigsrc('pc')
sp.SCOPE_configure() # Armed

print('Finished Configuration\n')
# power on
pwr.analogIO_ON()
time.sleep(1)   # wait to settle down
pwr.get_voltVP() #measure

sp.SCOPE_pctrig() # Triggering

sp.SCOPE_get_data()  # Wait to measure the scope data

Ch1V = np.array(sp.Ch1Voltages) # DC value


#power off
pwr.analogIO_OFF()

print('V+=%.2f V\n'%(pwr.get_vmtr(0)))
print('V-=%.2f V\n'%(pwr.get_vmtr(1)))
print('Ch1V={:.2f} V\n'.format(Ch1V.mean()))

del pwr, sp
