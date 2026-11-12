"""
Windows IT Support Toolkit
A beginner-friendly command-line utility for basic Windows diagnostics.

This tool only displays information locally. It does not change system settings,
install software, or send diagnostic information over the network.
"""

import ctypes
import os
import platform
import shutil
import socket
import subprocess
from datetime import datetime


def get_system_information():
    """Display basic Windows and computer information."""
    print("\n=== SYSTEM INFORMATION ===")
    print(f"Computer name : {platform.node()}")
    print(f"Operating system: {platform.system()} {platform.release()}")
    print(f"OS version    : {platform.version()}")
    print(f"Architecture  : {platform.machine()}")
    print(f"Python version: {platform.python_version()}")


def get_memory_information():
    """Display total and currently available physical memory on Windows."""
    print("\n=== MEMORY INFORMATION ===")
    if platform.system() != "Windows":
        print("This memory check is currently implemented for Windows only.")
        return

    class MEMORYSTATUSEX(ctypes.Structure):
        _fields_ = [
            ("dwLength", ctypes.c_ulong),
            ("dwMemoryLoad", ctypes.c_ulong),
            ("ullTotalPhys", ctypes.c_ulonglong),
            ("ullAvailPhys", ctypes.c_ulonglong),
            ("ullTotalPageFile", ctypes.c_ulonglong),
            ("ullAvailPageFile", ctypes.c_ulonglong),
            ("ullTotalVirtual", ctypes.c_ulonglong),
            ("ullAvailVirtual", ctypes.c_ulonglong),
            ("ullAvailExtendedVirtual", ctypes.c_ulonglong),
        ]

    memory_status = MEMORYSTATUSEX()
    memory_status.dwLength = ctypes.sizeof(MEMORYSTATUSEX)

    if ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(memory_status)):
        total_gb = memory_status.ullTotalPhys / (1024 ** 3)
        available_gb = memory_status.ullAvailPhys / (1024 ** 3)
        print(f"Total RAM     : {total_gb:.2f} GB")
        print(f"Available RAM : {available_gb:.2f} GB")
        print(f"Memory in use : {memory_status.dwMemoryLoad}%")
    else:
        print("Could not retrieve memory information.")


def check_disk_space():
    """Display total, used, and free space on the Windows system drive."""
    print("\n=== DISK SPACE ===")
    drive = os.environ.get("SystemDrive", "C:") + "\\"
    try:
        usage = shutil.disk_usage(drive)
        to_gb = 1024 ** 3
        print(f"Drive         : {drive}")
        print(f"Total space   : {usage.total / to_gb:.2f} GB")
        print(f"Used space    : {usage.used / to_gb:.2f} GB")
        print(f"Free space    : {usage.free / to_gb:.2f} GB")
        print(f"Usage         : {usage.used / usage.total * 100:.1f}%")
    except OSError as error:
        print(f"Unable to check disk space: {error}")


def show_ip_configuration():
    """Run ipconfig to display the current network configuration."""
    print("\n=== IP CONFIGURATION ===")
    if platform.system() != "Windows":
        print("This command is intended for Windows.")
        return

    try:
        result = subprocess.run(
            ["ipconfig"],
            capture_output=True,
            text=True,
            check=False,
            timeout=10,
        )
        print(result.stdout or result.stderr)
    except (OSError, subprocess.TimeoutExpired) as error:
        print(f"Could not run ipconfig: {error}")


def test_network_connection():
    """Ping a hostname or IP address entered by the user."""
    print("\n=== NETWORK CONNECTIVITY TEST ===")
    host = input("Enter a hostname or IP address (e.g. google.com): ").strip()

    if not host:
        print("No hostname entered. Returning to menu.")
        return

    # Prevent command-line arguments from being passed as part of the host input.
    if any(character.isspace() for character in host):
        print("Please enter a single hostname or IP address.")
        return

    command = ["ping", "-n", "4", host] if platform.system() == "Windows" else ["ping", "-c", "4", host]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False,
            timeout=15,
        )
        print(result.stdout or result.stderr)
        if result.returncode == 0:
            print("Result: The host responded to ping.")
        else:
            print("Result: No successful ping response. Check the network or host.")
    except (OSError, subprocess.TimeoutExpired) as error:
        print(f"Could not complete the ping test: {error}")


def check_dns_resolution():
    """Resolve a hostname to an IP address using the system DNS resolver."""
    print("\n=== DNS LOOKUP ===")
    hostname = input("Enter a hostname (e.g. example.com): ").strip()

    if not hostname or any(character.isspace() for character in hostname):
        print("Please enter one valid hostname.")
        return

    try:
        ip_address = socket.gethostbyname(hostname)
        print(f"Hostname      : {hostname}")
        print(f"Resolved IP   : {ip_address}")
        print("Result: DNS resolution succeeded.")
    except socket.gaierror as error:
        print(f"DNS resolution failed: {error}")


def display_menu():
    """Display the available diagnostic options."""
    print("\n" + "=" * 42)
    print("       WINDOWS IT SUPPORT TOOLKIT")
    print("=" * 42)
    print("1. View system information")
    print("2. View memory information")
    print("3. Check disk space")
    print("4. View IP configuration")
    print("5. Test network connection (ping)")
    print("6. Check DNS resolution")
    print("0. Exit")
    print("-" * 42)


def main():
    """Run the interactive diagnostic menu."""
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    while True:
        display_menu()
        choice = input("Select an option: ").strip()

        actions = {
            "1": get_system_information,
            "2": get_memory_information,
            "3": check_disk_space,
            "4": show_ip_configuration,
            "5": test_network_connection,
            "6": check_dns_resolution,
        }

        if choice == "0":
            print("Thank you for using Windows IT Support Toolkit.")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid selection. Please choose a listed option.")


if __name__ == "__main__":
    main()
