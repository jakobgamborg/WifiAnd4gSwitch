import os
wifi_interface = 'WiFi'
lte_interface = '4G'



os.system("netsh mbn disconnect mobiltelefon")
os.system("netsh interface set interface '" + wifi_interface + "' enabled")