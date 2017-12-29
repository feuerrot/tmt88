#!/usr/bin/env python3 
import escpos.printer

class bondrucker:
	def __init__(self, host="151.217.15.25"):
		self.printer = escpos.printer.Network(host = host)
		self.printer.set(smooth=True, flip=False)
		self.printer.charcode("MULTILINGUAL")
		self.defaults = {
			"align": "left",
		}

	def default(self, **options):
		for elem in options:
			self.defaults[elem] = options[elem]

	def text(self, text, align=None, newline=True):
		if align == None:
			align = self.defaults["align"]
		self.printer.set(align=align)
		self.printer.text(text)
		if newline:
			self.printer.text("\n")

	def qr(self, data, size=12, align=None):
		if align == None:
			align = self.defaults["align"]
		self.printer.set(align=align)
		self.printer.qr(data, size=size, native=True)

	def cut(self):
		self.printer.cut()
