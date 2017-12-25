#!/usr/bin/env python3 
import escpos.printer

class bondrucker:
	def __init__(self, host="Printer-7B1BF9.visitor.congress.ccc.de"):
		self.printer = escpos.printer.Network(host = host)
		self.printer.set(smooth=True, flip=False)
		self.printer.charcode("MULTILINGUAL")

	def text(self, text, align="left"):
		self.printer.set(align=align)
		self.printer.text(text)
		self.printer.text("\n")

	def qr(self, data, size=12, align="center"):
		self.printer.set(align=align)
		self.printer.qr(data, size=size, native=True)

	def cut(self):
		self.printer.cut()
