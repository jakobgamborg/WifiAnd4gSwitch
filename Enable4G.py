import os
wifi_interface = 'Wi-Fi'
lte_interface = '4G'



os.system("netsh interface set interface '" + wifi_interface + "' disabled")
os.system("netsh mbn connect interface=Mobiltelefon connmode=name name=BCF33027-4005-492A-997A-582923C0BEDE")