###############  WELCOME TO WIFI VIEWER ###############
import subprocess

profiles = subprocess.check_output(
    ['netsh', 'wlan', 'show', 'profiles'],
    shell=True
).decode('utf-8').split('\n')

names = []

for line in profiles:
    if "All User Profile" in line:
        names.append(line.split(":")[1].strip())

for i, name in enumerate(names, 1):
    print(f"{i}. {name}")

choice = int(input("Enter the number of the Wi-Fi profile to view its password: "))

result = subprocess.check_output(
    ['netsh', 'wlan', 'show', 'profile', names[choice - 1], 'key=clear'],
    shell=True
).decode('utf-8').split('\n')

print("\n" + "="*50)
for line in result:
    if "Key Content" in line or "SSID" in line:
        print(line.strip())
print("="*50)

print("============================")
print("Have a nice day! :)")