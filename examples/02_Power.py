'''
ADStudio V 1.0
Coded By Youngsik Kim @ CSEE . HGU

Test the Power supply and Voltage meter function

 Set V+ : 4.0V
     V- : -3.0V
'''
import sys
sys.path.append("C:/vscode_ws/ws_python/adstudio")

from adstudio import Power
import time

pwr=Power()
pwr.get_device_info()
pwr.print_device_info()

pwr.open_device()

pwr.reset_analogIO()

#get the number of channels for AnalogIO
pwr.get_number_of_channels()
Nch=5

# Print All Channels of Power object
for idx in range(Nch):
    pwr.get_nodes_of_channels(idx)

# print all nodes of channel=0 device
pwr.get_nodes_of_channels(0)
for idx in range(3):
    pwr.what_is_channel_node(0,idx)

pwr.get_nodes_of_channels(1)
for idx in range(3):
    pwr.what_is_channel_node(1,idx)

pwr.get_nodes_of_channels(2)
for idx in range(4):
    pwr.what_is_channel_node(2,idx)

pwr.get_nodes_of_channels(3)
for idx in range(2):
    pwr.what_is_channel_node(3,idx)

pwr.get_nodes_of_channels(4)
pwr.what_is_channel_node(4,0)



# Configure VP+=2.5V with 50mA current
pwr.set_channel_voltage('V+',4.0)
pwr.set_channel_voltage('V-',-3.0)


pwr.enable_channel('V+')
pwr.enable_channel('V-')

pwr.analogIO_configure()
pwr.set_power_limit('V+-',10e-3)
pwr.set_channel_current('V+',10e-3)
pwr.set_channel_current('V-',-10e-3)

# power on
pwr.analogIO_ON()
time.sleep(1)   # wait to settle down
pwr.get_voltVP() #measure
pwr.get_crntVP() # measure current
pwr.get_crntVN() # measure current
#power off
pwr.analogIO_OFF()


print('Vmtr1=%.2f V\n'%(pwr.get_vmtr(0)))
print('Vmtr2=%.2f V\n'%(pwr.get_vmtr(1)))
print('Current VP=%.2f A\n'%(pwr.crntVP.value))
print('Current VN=%.2f A\n'%(pwr.crntVN.value))


del pwr
