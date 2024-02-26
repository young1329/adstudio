'''
ADStudio V 1.0

Coded By Youngsik Kim @ CSEE.HGU
2024. 02.23

Testing Device is connected
print device SN when sucess
'''
import sys
sys.path.append("C:/vscode_ws/ws_python/adstudio")
from adstudio.device import Device

import time

dv=Device()
dv.open_device()
dv.get_device_info()
dv.print_device_info()
dv.CloseAll()
del dv
