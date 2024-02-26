'''
ADStudio V 1.0

Test for Pattern / Digital IO / Power

Digital Output D10 and D09 set as output and
assgin D10=High, D09=Low

Pattern : 1kHz pulse clock with 50%duty through D15

Coded by Younsik Kim
2024. 02. 23

'''
import sys
sys.path.append("C:/vscode_ws/ws_python/adstudio")

from adstudio import Power
from adstudio import Pattern
from adstudio import DigitalIO
import time

pwr = Power()
dio = DigitalIO()
pttn=Pattern()


pttn.get_device_info()
pttn.print_device_info()
pttn.open_device()

pttn.DO_reset()

#default 100MHz clock
pttn.DO_check_internal_clock()  #internal clock check


pttn.DO_set_divider(15,500000)
pttn.DO_enable_disable(15,True)
pttn.DO_set_counter(15,1,1)
pttn.DO_set_form(15,'PP')

#2. Now let them go out
pttn.DO_start_stop(True) # make them output


dio.SetOutputPins(0x0600)
dio.SetOutputValues(0x0400)
dio.GetDigitalIOInputs()


pwr.set_channel_voltage('V+',5)
pwr.set_channel_current('V+',500e-3)
pwr.enable_channel('V+')
pwr.analogIO_ON()

time.sleep(1)
pwr.get_voltVP() #measure
pwr.analogIO_OFF()
print('Vmtr1=%.2f V\n'%(pwr.get_vmtr(0)))
print('Vmtr2=%.2f V\n'%(pwr.get_vmtr(1)))


pttn.CloseAll()

del pttn, pwr, dio
