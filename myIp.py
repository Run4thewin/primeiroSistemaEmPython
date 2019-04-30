
import subprocess

currentIp = subprocess.Popen("ifconfig", shell=True)
print("You Ip: " + str(currentIp))
