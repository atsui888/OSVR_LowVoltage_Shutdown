nLogOff=0 
nReboot=2 
nForceLogOff=4 
nForceReboot=6 
nPowerDown=8 
nForcePowerDown=12

import wmi
wmi.WMI(privileges=["Shutdown"]).Win32_OperatingSystem()[0].Win32Shutdown (Flags=nPowerDown)
