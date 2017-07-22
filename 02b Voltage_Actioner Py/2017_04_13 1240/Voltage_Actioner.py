#!Python3
# Future: if low voltage detected 3 times within 5 minute, shutdown pc otherwise it is false alarm
#         due to voltage spike up and down.
import serial
import os
import datetime
import time

i =0
appPath='c:\\MonitorLowVolt_v02'
configFile=appPath+'\\MonitorLowVoltCfg.txt'
saveFile=appPath+'\\ShutDownLog.txt'    
sInput=""
batteryDCVoltage=0
#executeThis = 'C:\Windows\System32\cmd.exe /c powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "Stop-Computer"'
executeThis = 'C:\Windows\System32\cmd.exe /c shutdown /s /t 1'

print('loading...')
print('OneBerry Technolgies Low Voltage Monitor program')
rcFile=open(configFile,'r')
iComPort=rcFile.readline().strip()
lowVoltageTreshold=rcFile.readline().strip()
rcFile.close()

ser=serial.Serial()
ser.baudrate=9600
ser.port=iComPort
ser.open()
ser.reset_input_buffer()
#ser.reset_output_buffer()

#print('iComPort is :' + str(iComPort))
#print('lowVoltageTreshold is: ' + str(lowVoltageTreshold))
#print('Press enter to continue...')
#print('Serial Name is: '+ser.name)
#input()
#print(ser.name)

#while i<5000:
#    i+=1
time.sleep(2)

def checkVoltageLevels():
    if float(batteryDCVoltage)<float(lowVoltageTreshold):
        cDT = datetime.datetime.now()
        strSave=str(cDT.year)+'/'+str(cDT.month)+'/'+str(cDT.day)+'/ '+str(cDT.hour)+str(cDT.minute)+'hrs'+' '+'Shutdown due to voltage < '+str(lowVoltageTreshold)+';'
        rcFile=open(saveFile,'a')
        rcFile.write(strSave+'\n')
        rcFile.close()
        ser.close()

        print('Current Voltage is :'+str(batteryDCVoltage))
        print('shutting down system.....')
        os.system(executeThis)
    else:
        print('current battery voltage is: '+str(batteryDCVoltage))
        print('Low Voltage Treshold is: '+str(lowVoltageTreshold))
        print('')
            
while ser.isOpen():    
    sInput=ser.readline().strip()
    batteryDCVoltage=sInput.decode('utf-8')
    
    #if len(batteryDCVoltage)>5:
    #    batteryDCVoltage=batteryDCVoltage[0:5]

    try:
        checkVoltageLevels()
    except ValueError:
        print("Not a Float")
        print(' ')   
    
    

