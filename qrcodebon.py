#!/usr/bin/env python3 
import uuid
import bondrucker

def getuuid():
	return str(uuid.uuid4()).split("-")[-1]

def main():
	printer = bondrucker.bondrucker()
	uuid = getuuid()
	printer.text("Please enter the following code at", align="center")
	printer.text("** https://dns.colo.congress.ccc.de **", align="center")
	printer.text("to register your own colo.congress.ccc.de	subdomain\n\n", align="center")
	printer.text(uuid, align="center")
	printer.qr("https://dns.colo.congress.ccc.de/register/{}".format(uuid))
	printer.cut()

if __name__ == "__main__":
	main()
