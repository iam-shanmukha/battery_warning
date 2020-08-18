from time import sleep
from playsound import playsound
import subprocess, platform

if platform.system() == 'Linux':
	while True:
		with open("/sys/class/power_supply/BAT0/status","r") as f:
			status = f.read()
		with open("/sys/class/power_supply/BAT0/capacity","r") as f:
			capacity = int(f.read())
		#print(capacity)
		if ("Discharging" in status) and (capacity <=50):	
				playsound('batt.mp3')
				subprocess.Popen(['notify-send', "Charge Me!!! Charge Me!!!. {}% rem.".format(capacity)])
				sleep(6)
		elif ("Charging" in status) or (capacity>50):
			print("GOOD")
			subprocess.Popen(['notify-send', "GOOD. {}% rem.".format(capacity)])
			break