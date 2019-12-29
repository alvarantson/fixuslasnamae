from xml.etree import cElementTree as ElementTree
from tkinter import filedialog
from tkinter import *




# https://stackoverflow.com/questions/2148119/how-to-convert-an-xml-string-to-a-dictionary
class XmlListConfig(list):
	def __init__(self, aList):
		for element in aList:
			if element:
				# treat like dict
				if len(element) == 1 or element[0].tag != element[1].tag:
					self.append(XmlDictConfig(element))
				# treat like list
				elif element[0].tag == element[1].tag:
					self.append(XmlListConfig(element))
			elif element.text:
				text = element.text.strip()
				if text:
					self.append(text)


class XmlDictConfig(dict):
	'''
	Example usage:

	>>> tree = ElementTree.parse('your_file.xml')
	>>> root = tree.getroot()
	>>> xmldict = XmlDictConfig(root)

	Or, if you want to use an XML string:

	>>> root = ElementTree.XML(xml_string)
	>>> xmldict = XmlDictConfig(root)

	And then use xmldict for what it is... a dict.
	'''
	def __init__(self, parent_element):
		if parent_element.items():
			self.update(dict(parent_element.items()))
		for element in parent_element:
			if element:
				# treat like dict - we assume that if the first two tags
				# in a series are different, then they are all different.
				if len(element) == 1 or element[0].tag != element[1].tag:
					aDict = XmlDictConfig(element)
				# treat like list - we assume that if the first two tags
				# in a series are the same, then the rest are the same.
				else:
					# here, we put the list in dictionary; the key is the
					# tag name the list elements all share in common, and
					# the value is the list itself 
					aDict = {element[0].tag: XmlListConfig(element)}
				# if the tag has attributes, add those to the dict
				if element.items():
					aDict.update(dict(element.items()))
				self.update({element.tag: aDict})
			# this assumes that if you've got an attribute in a tag,
			# you won't be having any text. This may or may not be a 
			# good idea -- time will tell. It works for the way we are
			# currently doing XML configuration files...
			elif element.items():
				self.update({element.tag: dict(element.items())})
			# finally, if there are no child tags and no attributes, extract
			# the text
			else:
				self.update({element.tag: element.text})

def ImportXML(FileName):

	tree = ElementTree.parse(FileName)
	root = tree.getroot()
	xmldict = XmlDictConfig(root)

	items = []
	for i in xmldict.get("Invoice").get("InvoiceItem").get("InvoiceItemGroup"):
		item = {}
		item["InvoiceNumber"] = "" # not required
		item["ID"] = i["ItemEntry"]["SellerProductId"]
		if item["ID"] == None:
			continue
		item["Name"] = i["ItemEntry"]["Description"]
		item["ItemAmount"] = i["ItemEntry"]["ItemDetailInfo"]["ItemAmount"]
		item["ItemPrice"] = "" # difference in item price in import, calculated single item price - AddSum != SumBeforeVAT
#		item["AddRate"] = i["ItemEntry"]["Addition"]["AddRate"]
#		this didn't work for some reason, so solved it by getting the 'proper' key
		for j in i["ItemEntry"]:
			if j == "Addition":
				item["AddRate"] = i["ItemEntry"][j]["AddRate"]
		item["SumBeforeVAT"] = i["ItemEntry"]["VAT"]["SumBeforeVAT"]
		item["VATSum"] = i["ItemEntry"]["VAT"]["VATSum"]
#		print(i["ItemEntry"])
#		print()
#		print(item)
#		print()
		items.append(item)

#	print(xmldict.get("Invoice").get("InvoiceItem").get("InvoiceItemGroup"))
#	print(type(xmldict.get("Invoice").get("InvoiceItem").get("InvoiceItemGroup")))
	return items

def writeTXT(items, FileName):
	txt = ""
	for item in items:
		for key in item:
			txt += str(item[key]) + "\t"
		txt += "\n"
#	with filedialog.asksaveasfile(mode='w', defaultextension=".txt",filetypes = (("txt files","*.txt"),("all files","*.*"))) as fm:
#		fm.write(txt)
	return txt



#for i in ImportXML("sisend.xml"):
#	print(i, "\n")

#writeTXT(ImportXML("sisend.xml"), "sisend.xml")
# tell.nr tootekood nimi kogus asjaHind 0 kokku km

#writeTXT(ImportXML(root.filename), root.filename)
