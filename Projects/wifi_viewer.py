############# WELCOME TO WIFI VIEWER PRO #############
import subprocess
import time
import os
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_wifi_networks():
    try:
        subprocess.check_output("netsh wlan show networks mode=bssid", shell=True, stderr=subprocess.DEVNULL)
        
        result = subprocess.check_output(
            "netsh wlan show networks mode=bssid", 
            shell=True, 
            stderr=subprocess.DEVNULL
        ).decode('utf-8', errors='ignore')
        
        networks = []
        current_network = {}
        
        for line in result.split('\n'):
            line = line.strip()
            
            if "SSID" in line and "BSSID" not in line:
                if current_network:
                    networks.append(current_network)
                ssid = line.split(":")[1].strip()
                current_network = {
                    'ssid': ssid,
                    'bssid': 'N/A',
                    'signal': 'N/A',
                    'channel': 'N/A',
                    'encryption': 'N/A'
                }
            elif "BSSID" in line:
                bssid = line.split(":")[1].strip()
                current_network['bssid'] = bssid
            elif "Signal" in line:
                signal = line.split(":")[1].strip()
                current_network['signal'] = signal
            elif "Channel" in line:
                channel = line.split(":")[1].strip()
                current_network['channel'] = channel
            elif "Authentication" in line:
                encryption = line.split(":")[1].strip()
                current_network['encryption'] = encryption
        
        if current_network:
            networks.append(current_network)
            
        return networks
        
    except subprocess.CalledProcessError:
        return []

def display_networks(networks):
    if not networks:
        print("No Wi-Fi networks found!")
        return
    
    networks.sort(key=lambda x: int(x['signal'].replace('%', '')) if x['signal'] != 'N/A' else 0, reverse=True)
    
    print("=" * 90)
    print(f"Wi-Fi Networks - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 90)
    print(f"{'#':<4} {'SSID':<30} {'Signal':<12} {'Channel':<10} {'BSSID':<20} {'Security':<15}")
    print("-" * 90)
    
    for idx, net in enumerate(networks, 1):
        signal = net['signal']
        if signal == 'N/A':
            signal_display = 'N/A'
        else:
            signal_display = f"{signal}"
            
        print(f"{idx:<4} {net['ssid'][:29]:<30} {signal_display:<12} {net['channel']:<10} {net['bssid'][:19]:<20} {net['encryption'][:14]:<15}")
    
    print("=" * 90)

def get_password_for_network(ssid):
    try:
        result = subprocess.check_output(
            f"netsh wlan show profile \"{ssid}\" key=clear", 
            shell=True
        ).decode('utf-8', errors='ignore')
        
        for line in result.split('\n'):
            if "Key Content" in line:
                password = line.split(":")[1].strip()
                return password
        return "No password found or network is open"
    except:
        return "Unable to retrieve password"

def get_saved_profiles():
    try:
        profiles = subprocess.check_output(
            "netsh wlan show profiles", 
            shell=True
        ).decode('utf-8', errors='ignore')
        
        names = []
        for line in profiles.split("\n"):
            if "All User Profile" in line:
                name = line.split(":")[1].strip()
                names.append(name)
        return names
    except:
        return []

def show_profile_details(profile_name):
    try:
        result = subprocess.check_output(
            f"netsh wlan show profile \"{profile_name}\" key=clear", 
            shell=True
        ).decode('utf-8', errors='ignore')
        return result
    except:
        return "Error retrieving profile information!"

def show_network_password():
    clear_screen()
    print("=" * 60)
    print("        SHOW Wi-Fi PASSWORD")
    print("=" * 60)
    
    networks = get_wifi_networks()
    if not networks:
        print("No Wi-Fi networks found!")
        input("\nPress Enter to continue...")
        return
    
    display_networks(networks)
    
    try:
        choice = int(input("\nEnter the number of the network to show password: ")) - 1
        if 0 <= choice < len(networks):
            ssid = networks[choice]['ssid']
            clear_screen()
            print("=" * 60)
            print(f"Network: {ssid}")
            print("=" * 60)
            
            password = get_password_for_network(ssid)
            print(f"\nPassword: {password}")
            
            print("\n" + "=" * 60)
            print("Full network details:")
            print("=" * 60)
            print(show_profile_details(ssid))
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number!")
    
    input("\nPress Enter to continue...")

def main():
    clear_screen()
    print("=" * 60)
    print("          WIFI VIEWER PRO - Professional Edition")
    print("=" * 60)
    
    while True:
        print("\nMain Menu:")
        print("1. Scan available networks (real-time)")
        print("2. Auto-scan every 5 seconds")
        print("3. View saved profiles")
        print("4. Show password for a network")
        print("5. Exit")
        
        choice = input("\nEnter your choice: ").strip()
        
        if choice == "1":
            clear_screen()
            networks = get_wifi_networks()
            display_networks(networks)
            input("\nPress Enter to continue...")
            
        elif choice == "2":
            clear_screen()
            print("Auto-scan started... (Press Ctrl+C to stop)")
            try:
                while True:
                    clear_screen()
                    networks = get_wifi_networks()
                    display_networks(networks)
                    print("\nUpdating in 5 seconds...")
                    time.sleep(5)
            except KeyboardInterrupt:
                print("\n\nAuto-scan stopped!")
                input("Press Enter to continue...")
                
        elif choice == "3":
            clear_screen()
            profiles = get_saved_profiles()
            if not profiles:
                print("No saved profiles found!")
            else:
                print("Saved Profiles:")
                for idx, name in enumerate(profiles, 1):
                    print(f"{idx}. {name}")
                
                try:
                    profile_choice = int(input("\nEnter profile number: ")) - 1
                    if 0 <= profile_choice < len(profiles):
                        clear_screen()
                        print(f"Profile Details: {profiles[profile_choice]}")
                        print("=" * 60)
                        print(show_profile_details(profiles[profile_choice]))
                    else:
                        print("Invalid number!")
                except ValueError:
                    print("Please enter a valid number!")
            
            input("\nPress Enter to continue...")
            
        elif choice == "4":
            show_network_password()
            
        elif choice == "5":
            print("\nGoodbye!")
            print("=" * 60)
            break
            
        else:
            print("Invalid option! Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExited with Ctrl+C!")
    except Exception as e:
        print(f"\nError: {e}")
    finally:
        print("=" * 60)
        print("=================================")
        print("Have a nice day!")