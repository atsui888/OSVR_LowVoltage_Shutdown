
import os
#os.system("C:\Windows\System32\cmd.exe /c powershell.exe -NoProfile -ExecutionPolicy Bypass -FILE ShutDown.ps1")
#os.system('C:\Windows\System32\cmd.exe /c powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "Stop-Computer -ComputerName \"localhost\""')

print('start shutdown?')
input()
os.system('C:\Windows\System32\cmd.exe /c shutdown /s /t 1')
