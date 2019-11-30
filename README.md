# WifiAnd4gSwitch

## Description
*These 2 applications can switch from using 4G to using Wifi on a computer*

*These applications is made for a specific computer, so that the name of the interface's fits the specific computer*

## To modify for your computer
**Write this command in your commandprompt:**

*netsh interface show interface*

**Find the name of your Wifi & 4G interface**

*Open the Enable4G.py & EnableWifi.py files and rename*

*The variables lte_interface & wifi_interface to the correct interface name*

**Recompile the python script to exe**

**Goto the directory in the commandprompt and write this command**

*pyinstaller Enable4G.py && pyinstaller EnableWiFi.py*


**If pyinstaller is not installed on your computer write line in commandpromt:** 

*pip install pyinstaller*

**For more information:**

https://stackoverflow.com/questions/5458048/how-to-make-a-python-script-standalone-executable-to-run-without-any-dependency








