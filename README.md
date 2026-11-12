# Windows IT Support Toolkit

A beginner-friendly Python command-line project for practicing basic Windows IT support and troubleshooting tasks.

## Features

- Display computer name, Windows version, architecture, and Python version
- Display total and available RAM (Windows implementation)
- Check system-drive disk capacity and free space
- Display network configuration with `ipconfig`
- Test network reachability with `ping`
- Check hostname-to-IP resolution using DNS

## Technology

- Python 3
- Python standard library: `platform`, `ctypes`, `shutil`, `subprocess`, `socket`, `os`, and `datetime`
- Windows 10/11

## Requirements

- Windows 10 or Windows 11
- Python 3.10 or later recommended
- No third-party packages required

## Run the project

1. Download or clone this repository.
2. Open PowerShell in the project folder.
3. Run:

```powershell
python windows_it_support_toolkit.py
```

## Example workflow

1. Select option `1` to identify the computer and operating system.
2. Select option `3` to review free disk space.
3. Select option `4` to inspect the IP configuration.
4. Select option `5` and enter a hostname such as `google.com` to test connectivity.
5. Select option `6` and enter a hostname to test DNS resolution.

## Safety and privacy

- The program displays diagnostic information locally.
- It does not modify Windows settings, install software, or transmit diagnostic data.
- `ipconfig` output may contain private local network details. Do not publish screenshots or logs containing personal or network-sensitive information.
- A failed ping does not always mean a host is offline; some networks block ICMP traffic.

## Learning outcomes

This project provides practice with:
- Reading operating-system information
- Checking disk and memory usage
- Running built-in Windows diagnostic commands
- Basic network troubleshooting
- DNS resolution
- Handling user input and common exceptions

## Current limitations

- The memory check uses the Windows API and is intended for Windows.
- The network configuration view uses the Windows `ipconfig` command.
- The project is a learning tool, not a replacement for enterprise monitoring or helpdesk software.

## Future improvements

Possible next steps after implementing and testing them:
- Add a structured diagnostic report saved locally
- Add unit tests
- Add configurable disk-space warning thresholds
- Add a simple graphical interface
