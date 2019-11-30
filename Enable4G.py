import os
wifi_interface = 'WiFi'
lte_interface = '4G'



os.system("netsh interface set interface '" + wifi_interface + "' disabled")
os.system("netsh interface set interface '" + lte_interface + "' enabled")