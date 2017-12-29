#!/usr/bin/env python3 
import bondrucker
import sys

def main(text=None):
	printer = bondrucker.bondrucker()
	printer.default(align="left")
	printer.text("Offene Tickets:")
	printer.text("* Wifi/Ethernet for signal angels")
	printer.text("  in jedem Vortragssaal")
	printer.text(" ")
	printer.text("* Halle 2: No Wifi in nursing room")
	printer.cut()

if __name__ == "__main__":
	main()
