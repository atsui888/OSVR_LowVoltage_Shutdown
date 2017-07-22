import serial.tools.list_ports

print('')
print('List of Com Ports available: ')
ports = list(serial.tools.list_ports.comports())
for p in ports:
    print('... '+str(p))

print(' ')
print('Key in the correct Com Port e.g. COM5 ')
print('into MonitorLowVoltCfg.txt')
print('')
print('Press "Enter" to exit this program.')
input()
