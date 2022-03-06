#!/usr/bin/env python3
import os
import sys
import nmap


if os.geteuid() != 0:
    sys.exit("\nOnly root can run this script\n")


# sudo apt install nmap

scanner = nmap.PortScanner()
print("Welcome!")
print("")

ip_address = input("Please enter the IP address you want to scan: ")
print(f"Is this the correct ip? {ip_address}")

type(ip_address)

response = input(
    """\nPlease enter the type of scan you want to run
(1) SYN ACK Scan
(2) UDP Scan
(3) Comprehensive Scan\n"""
)

print("\nYou have selected option: ", response)
print("nmap version: ", scanner.nmap_version())


if response == "1":
    scanner.scan(ip_address, "1-1024", "-v -sS")

    print(scanner.scaninfo())
    print("ip status", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())

    print("Open ports: ", scanner[ip_address]["tcp"].keys())
elif response == "2":
    scanner.scan(ip_address, "1-1024", "-v -sU")

    print(scanner.scaninfo())
    print("ip status", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())

    print("Open ports: ", scanner[ip_address]["udp"].keys())
elif response == "3":
    scanner.scan(ip_address, "1-1024", "-v -sS -sV -sC -A -O")

    print(scanner.scaninfo())
    print("ip status", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())

    print("Open ports: ", scanner[ip_address]["tcp"].keys())
else:
    print("invalid input")
