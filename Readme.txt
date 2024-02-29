Library for Analog Discoverty Studio

Digilentinc - Waveforms must be installed first

change the sys.path.append( to the foloder )
Ex) First two lines
import sys
sys.path.append("C:/vscode_ws/ws_python/adstudio")

.
|-- Readme.txt   : this file
|-- adstudio
|   |-- __init__.py : package init file
|   |-- awg.py : AWG object
|   |-- device.py : Electronic Explorer board base class
|   |-- digitalio.py : digital static io object
|   |-- dwfconstants.py : constants provided from Digilentinc
|   |-- logic.py   : logic analyzer object
|   |-- pattern.py : digital pattern generation object
|   |-- power.py : Power supply and voltagemeter boject
|   `-- scope.py : analog scope object
`-- examples
    |-- 01_Device.py : check out the device connection.
    |-- 02_Power.py : Vref1, Vref2, VP+ and Voltage meters are tested
    |-- 03_AWG_Scope.py: AWG and Scope test
    |-- 04_DigitalIO.py : Static digital IO test
    |-- 05_Pattern_Logic03.py : 4bit counter and meausre with 8-bit 1000 samples with Single Acquisition Mode
    `-- 06_Pattern04.py D10 and D09 as output terminal, 1khz clock 50% duty output
