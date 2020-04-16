from xml.dom import minidom, Node

def get_text(item, tagName):
	try:
		return item.getElementsByTagName(tagName)[0].firstChild.nodeValue
	except:
		return ""

def get_items(doc):
	tooted = doc.getElementsByTagName("ItemEntry")
	items = []
	for toode in tooted:
		item = {}
		try:
			item["SellerProductId"] = toode.getElementsByTagName("SellerProductId")[0].firstChild.nodeValue
		except:
			continue
		item["RowNo"] = get_text(toode, "RowNo")
		item["Description"] = get_text(toode, "Description")
		item["EAN"] = get_text(toode, "EAN")

		item["ItemUnit"] = get_text(toode.getElementsByTagName("ItemDetailInfo")[0], "ItemUnit")
		item["ItemAmount"] = get_text(toode.getElementsByTagName("ItemDetailInfo")[0], "ItemAmount")
		item["ItemPrice"] = get_text(toode.getElementsByTagName("ItemDetailInfo")[0], "ItemPrice")

		item["ItemSum"] = get_text(toode, "ItemSum")

		item["AddContent"] = get_text(toode.getElementsByTagName("Addition")[0], "AddContent")
		item["AddRate"] = get_text(toode.getElementsByTagName("Addition")[0], "AddRate")
		item["AddSum"] = get_text(toode.getElementsByTagName("Addition")[0], "AddSum")

		item["SumBeforeVAT"] = get_text(toode.getElementsByTagName("VAT")[0], "SumBeforeVAT")
		item["VATRate"] = get_text(toode.getElementsByTagName("VAT")[0], "VATRate")
		item["VATSum"] = get_text(toode.getElementsByTagName("VAT")[0], "VATSum")
		item["Currency"] = get_text(toode.getElementsByTagName("VAT")[0], "Currency")

		item["ItemTotal"] = get_text(toode, "ItemTotal")

		items.append(item)
	return items

def get_data(doc):
	meta = {}

	div = doc.getElementsByTagName("Header")[0]
	meta["Date"] = get_text(div, "Date")
	meta["FileId"] = get_text(div, "FileId")
	meta["Version"] = get_text(div, "Version")

	seller = {}

	div = doc.getElementsByTagName("SellerParty")[0]
	seller["Name"] = get_text(div, "Name")
	seller["RegNumber"] = get_text(div, "RegNumber")

	invoice = {}

	div = doc.getElementsByTagName("InvoiceInformation")[0]
	invoice["DocumentName"] = get_text(div, "DocumentName")
	invoice["InvoiceNumber"] = get_text(div, "InvoiceNumber")
	invoice["PaymentReferenceNumber"] = get_text(div, "PaymentReferenceNumber")
	invoice["InvoiceDate"] = get_text(div, "InvoiceDate")
	invoice["DueDate"] = get_text(div, "DueDate")
	invoice["PaymentTerm"] = get_text(div, "PaymentTerm")

	div = doc.getElementsByTagName("InvoiceSumGroup")[0]
	invoice["InvoiceSum"] = get_text(div, "InvoiceSum")
	invoice["Rounding"] = get_text(div, "Rounding")
	invoice["TotalVATSum"] = get_text(div, "TotalVATSum")
	invoice["TotalSum"] = get_text(div, "TotalSum")

	return {"seller": seller, "invoice": invoice, "meta":meta}

def import_motoral(file):
	doc = minidom.parse(file)
	invoice = get_data(doc)
	invoice["items"] = get_items(doc)
	return invoice

def export_baltiautoosad(INVOICE):

	doc = minidom.Document()

	arve_hankijalt = doc.createElement('arve_hankijalt')
	doc.appendChild(arve_hankijalt)

	# SAATJA
	saatja = doc.createElement('saatja')
	arve_hankijalt.appendChild(saatja)

	kuupaev = doc.createElement('kuupaev')
	ENTRY = "" # DEFAULT
	try:
		ENTRY = INVOICE["meta"]["Date"].replace("-","")
	except:
		pass
	if ENTRY != "":
		kuupaev.appendChild(doc.createTextNode(ENTRY))
	saatja.appendChild(kuupaev)

	nimi = doc.createElement('nimi')
	ENTRY = "" # DEFAULT
	try:
		ENTRY = INVOICE["seller"]["Name"]
	except:
		pass
	if ENTRY != "":
		nimi.appendChild(doc.createTextNode(ENTRY))
	saatja.appendChild(nimi)

	aadr1 = doc.createElement('aadr1')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		aadr1.appendChild(doc.createTextNode(ENTRY))
	saatja.appendChild(aadr1)

	aadr = doc.createElement('aadr')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		aadr.appendChild(doc.createTextNode(ENTRY))
	saatja.appendChild(aadr)

	pindeks = doc.createElement('pindeks')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		pindeks.appendChild(doc.createTextNode(ENTRY))
	saatja.appendChild(pindeks)

	regnr = doc.createElement('regnr')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		regnr.appendChild(doc.createTextNode(ENTRY))
	saatja.appendChild(regnr)

	kmregnr = doc.createElement('kmregnr')
	ENTRY = "" # DEFAULT
	try:
		if "EE" not in INVOICE["seller"]["RegNumber"]:
			INVOICE["seller"]["RegNumber"] = "EE"+INVOICE["seller"]["RegNumber"]
		ENTRY = INVOICE["seller"]["RegNumber"]
	except:
		pass
	if ENTRY != "":
		kmregnr.appendChild(doc.createTextNode(ENTRY))
	saatja.appendChild(kmregnr)

	# ARVE
	arve = doc.createElement('arve')
	arve_hankijalt.appendChild(arve)

	nr = doc.createElement('nr')
	ENTRY = "" # DEFAULT
	try:
		ENTRY = INVOICE["invoice"]["InvoiceNumber"]
	except:
		pass
	if ENTRY != "":
		nr.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(nr)

	seletus = doc.createElement('seletus')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		seletus.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(seletus)

	markus = doc.createElement('markus')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		markus.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(markus)

	firma = doc.createElement('firma')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		firma.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(firma)

	pank = doc.createElement('pank')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		pank.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(pank)

	kuup = doc.createElement('kuup')
	ENTRY = "" # DEFAULT
	try:
		ENTRY = INVOICE["meta"]["Date"].replace("-",".")
	except:
		pass
	if ENTRY != "":
		kuup.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(kuup)

	makseting = doc.createElement('makseting')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		makseting.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(makseting)

	vkuup = doc.createElement('vkuup')
	ENTRY = "" # DEFAULT
	try: # TODO
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		vkuup.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(vkuup)

	rkonto = doc.createElement('rkonto')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		rkonto.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(rkonto)

	akonto = doc.createElement('akonto')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		akonto.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(akonto)

	kkonto = doc.createElement('kkonto')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		kkonto.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(kkonto)

	osakond = doc.createElement('osakond')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		osakond.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(osakond)

	summa = doc.createElement('summa')
	ENTRY = "" # DEFAULT
	try:
		ENTRY = INVOICE["invoice"]["TotalSum"]
	except:
		pass
	if ENTRY != "":
		summa.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(summa)

	kaib = doc.createElement('kaib')
	ENTRY = "" # DEFAULT
	try:
		ENTRY = INVOICE["invoice"]["TotalVATSum"]
	except:
		pass
	if ENTRY != "":
		kaib.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(kaib)

	ymardus = doc.createElement('ymardus')
	ENTRY = "0.00" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		ymardus.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(ymardus)

	kmaks = doc.createElement('kmaks')
	ENTRY = "20.00" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		kmaks.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(kmaks)

	makstud = doc.createElement('makstud')
	ENTRY = "0.0" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		makstud.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(makstud)

	liik = doc.createElement('liik')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		liik.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(liik)

	omah = doc.createElement('omah')
	ENTRY = "0.00" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		omah.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(omah)

	laodok = doc.createElement('laodok')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		laodok.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(laodok)

	ettemaks = doc.createElement('ettemaks')
	ENTRY = "0.00" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		ettemaks.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(ettemaks)

	viivis = doc.createElement('viivis')
	ENTRY = ".  ." # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		viivis.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(viivis)

	kkaart = doc.createElement('kkaart')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		kkaart.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(kkaart)

	viitenr = doc.createElement('viitenr')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		viitenr.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(viitenr)

	enr = doc.createElement('enr')
	ENTRY = "0" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		enr.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(enr)

	kmregnr = doc.createElement('kmregnr')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		kmregnr.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(kmregnr)

	kmviide = doc.createElement('kmviide')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		kmviide.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(kmviide)

	tehliik = doc.createElement('tehliik')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		tehliik.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(tehliik)

	trvliik = doc.createElement('trvliik')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		trvliik.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(trvliik)

	tarnekl = doc.createElement('tarnekl')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		tarnekl.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(tarnekl)

	vsumma = doc.createElement('vsumma')
	ENTRY = "0.00" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		vsumma.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(vsumma)

	vkaib = doc.createElement('vkaib')
	ENTRY = "0.00" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		vkaib.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(vkaib)

	vmakstud = doc.createElement('vmakstud')
	ENTRY = "0.00" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		vmakstud.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(vmakstud)

	valkood = doc.createElement('valkood')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		valkood.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(valkood)

	vettemaks = doc.createElement('vettemaks')
	ENTRY = "0.00" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		vettemaks.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(vettemaks)

	tabnr = doc.createElement('tabnr')
	ENTRY = "0" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		tabnr.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(tabnr)

	kmdkuu = doc.createElement('kmdkuu')
	ENTRY = "" # DEFAULT
	ENTRY = "/".join("".split("-")[0:2])
	if ENTRY != "":
		kmdkuu.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(kmdkuu)

	sisestas = doc.createElement('sisestas')
	ENTRY = "Super" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		sisestas.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(sisestas)

	sisaeg = doc.createElement('sisaeg')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = "".replace("-",".")+" 00:00"
	except:
		pass
	if ENTRY != "":
		sisaeg.appendChild(doc.createTextNode(ENTRY))
	arve.appendChild(sisaeg)

	# TELLIMUS

	tellimus = doc.createElement('tellimus')
	arve.appendChild(tellimus)

	nr = doc.createElement('nr')
	ENTRY = "" # DEFAULT
	try:
		ENTRY = INVOICE["invoice"]["InvoiceNumber"]
	except:
		pass
	if ENTRY != "":
		nr.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(nr)

	nimi = doc.createElement('nimi')
	ENTRY = "" # DEFAULT
	try:
		ENTRY = "*MOTORAL*"+INVOICE["invoice"]["InvoiceNumber"]
	except:
		pass
	if ENTRY != "":
		nimi.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(nimi)

	firma = doc.createElement('firma')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		firma.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(firma)

	saaja = doc.createElement('saaja')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		saaja.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(saaja)

	osakond = doc.createElement('osakond')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		osakond.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(osakond)

	viit = doc.createElement('viit')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		viit.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(viit)

	makseting = doc.createElement('makseting')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		makseting.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(makseting)

	trans = doc.createElement('trans')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		trans.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(trans)

	regaeg = doc.createElement('regaeg')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = "".replace("-",".")
	except:
		pass
	if ENTRY != "":
		regaeg.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(regaeg)

	taeg = doc.createElement('taeg')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = "".replace("-",".")
	except:
		pass
	if ENTRY != "":
		taeg.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(taeg)

	saataeg = doc.createElement('saataeg')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = "".replace("-",".")
	except:
		pass
	if ENTRY != "":
		saataeg.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(saataeg)

	summa = doc.createElement('summa')
	ENTRY = "" # DEFAULT
	try:
		ENTRY = INVOICE["invoice"]["TotalSum"]
	except:
		pass
	if ENTRY != "":
		summa.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(summa)

	kmaks = doc.createElement('kmaks')
	ENTRY = "20.00" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		kmaks.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(kmaks)

	kmhind = doc.createElement('kmhind')
	ENTRY = "N" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		kmhind.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(kmhind)

	leping = doc.createElement('leping')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		leping.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(leping)

	olek = doc.createElement('olek')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		olek.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(olek)

	liik = doc.createElement('liik')
	ENTRY = "I" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		liik.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(liik)

	osmy = doc.createElement('osmy')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		osmy.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(osmy)

	tukukoht = doc.createElement('tukukoht')
	ENTRY = "0" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		tukukoht.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(tukukoht)

	ymardus = doc.createElement('ymardus')
	ENTRY = "0.00" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		ymardus.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(ymardus)

	arvenr = doc.createElement('arvenr')
	ENTRY = "" # DEFAULT
	try:
		ENTRY = INVOICE["invoice"]["InvoiceNumber"]
	except:
		pass
	if ENTRY != "":
		arvenr.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(arvenr)

	laodok = doc.createElement('laodok')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		laodok.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(laodok)

	viitenr = doc.createElement('viitenr')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		viitenr.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(viitenr)

	kkaart = doc.createElement('kkaart')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		kkaart.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(kkaart)

	teenr = doc.createElement('teenr')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		teenr.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(teenr)

	omaja = doc.createElement('omaja')
	ENTRY = "0" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		omaja.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(omaja)

	algdok = doc.createElement('algdok')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		algdok.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(algdok)

	recadv = doc.createElement('recadv')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		recadv.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(recadv)

	tkell = doc.createElement('tkell')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		tkell.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(tkell)

	ryhm = doc.createElement('ryhm')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		ryhm.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(ryhm)

	ettemaks = doc.createElement('ettemaks')
	ENTRY = "0.00" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		ettemaks.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(ettemaks)

	kontakt = doc.createElement('kontakt')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		kontakt.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(kontakt)

	vedaja = doc.createElement('vedaja')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		vedaja.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(vedaja)

	komple = doc.createElement('komple')
	ENTRY = "0" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		komple.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(komple)

	andvot = doc.createElement('andvot')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		andvot.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(andvot)

	trfirma = doc.createElement('trfirma')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		trfirma.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(trfirma)

	vsumma = doc.createElement('vsumma')
	ENTRY = "0.00" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		vsumma.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(vsumma)

	kurss = doc.createElement('kurss')
	ENTRY = "0.00000000" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		kurss.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(kurss)

	valkood = doc.createElement('valkood')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		valkood.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(valkood)

	tabnr = doc.createElement('tabnr')
	ENTRY = "0" # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		tabnr.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(tabnr)

	sisaeg = doc.createElement('sisaeg')
	ENTRY = "" # DEFAULT
	try:
		raise Exception
		ENTRY = "".replace("-",".")+" 00:00"
	except:
		pass
	if ENTRY != "":
		sisaeg.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(sisaeg)

	kinaeg = doc.createElement('kinaeg')
	ENTRY = ".  ." # DEFAULT
	try:
		raise Exception
		ENTRY = ""
	except:
		pass
	if ENTRY != "":
		kinaeg.appendChild(doc.createTextNode(ENTRY))
	tellimus.appendChild(kinaeg)

	# TOOTED

	tooteread = doc.createElement('tooteread')
	tellimus.appendChild(tooteread)

	# TOODE
	for toode in INVOICE["items"]:
		tooterida = doc.createElement('tooterida')
		tooteread.appendChild(tooterida)

		recnr = doc.createElement('recnr')
		ENTRY = "" # DEFAULT
		try:
			ENTRY = toode["SellerProductId"]
		except:
			pass
		if ENTRY != "":
			recnr.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(recnr)

		siffer = doc.createElement('siffer')
		ENTRY = "" # DEFAULT
		try:
			ENTRY = toode["SellerProductId"]
		except:
			pass
		if ENTRY != "":
			siffer.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(siffer)

		nimi = doc.createElement('nimi')
		ENTRY = "" # DEFAULT
		try:
			ENTRY = toode["Description"]
		except:
			pass
		if ENTRY != "":
			nimi.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(nimi)

		kogus = doc.createElement('kogus')
		ENTRY = "" # DEFAULT
		try:
			ENTRY = toode["ItemAmount"]
		except:
			pass
		if ENTRY != "":
			kogus.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(kogus)

		kogus2 = doc.createElement('kogus2')
		ENTRY = "" # DEFAULT
		try:
			ENTRY = toode["ItemAmount"]
		except:
			pass
		if ENTRY != "":
			kogus2.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(kogus2)

		mhind = doc.createElement('mhind')
		ENTRY = "" # DEFAULT
		try: # TODO
	#		ENTRY = toode["ItemPrice"]
			raise Exception
		except:
			pass
		if ENTRY != "":
			mhind.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(mhind)

		hind = doc.createElement('hind')
		ENTRY = "" # DEFAULT
		try: # TODO
	#		ENTRY = toode["ItemPrice"]
			raise Exception
		except:
			pass
		if ENTRY != "":
			hind.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(hind)

		allahp = doc.createElement('allahp')
		ENTRY = "" # DEFAULT
		try:
			ENTRY = toode["AddRate"]
		except:
			pass
		if ENTRY != "":
			allahp.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(allahp)

		reasum = doc.createElement('reasum')
		ENTRY = "" # DEFAULT
		try:
			ENTRY = toode["SumBeforeVAT"]
		except:
			pass
		if ENTRY != "":
			reasum.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(reasum)

		kmsum = doc.createElement('kmsum')
		ENTRY = "" # DEFAULT
		try:
			ENTRY = toode["VATSum"]
		except:
			pass
		if ENTRY != "":
			kmsum.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(kmsum)

		tyyp = doc.createElement('tyyp')
		ENTRY = "" # DEFAULT
		try:
			raise Exception
			ENTRY = ""
		except:
			pass
		if ENTRY != "":
			tyyp.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(tyyp)

		ahind = doc.createElement('ahind')
		ENTRY = "" # DEFAULT
		try:
			raise Exception
			ENTRY = ""
		except:
			pass
		if ENTRY != "":
			ahind.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(ahind)

		tukukoht = doc.createElement('tukukoht')
		ENTRY = "0" # DEFAULT
		try:
			raise Exception
			ENTRY = ""
		except:
			pass
		if ENTRY != "":
			tukukoht.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(tukukoht)

		rakonto = doc.createElement('rakonto')
		ENTRY = "" # DEFAULT
		try:
			raise Exception
			ENTRY = ""
		except:
			pass
		if ENTRY != "":
			rakonto.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(rakonto)

		partii = doc.createElement('partii')
		ENTRY = "" # DEFAULT
		try:
			raise Exception
			ENTRY = ""
		except:
			pass
		if ENTRY != "":
			partii.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(partii)

		kaal = doc.createElement('kaal')
		ENTRY = "0.00" # DEFAULT
		try:
			raise Exception
			ENTRY = ""
		except:
			pass
		if ENTRY != "":
			kaal.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(kaal)

		lisamoot = doc.createElement('lisamoot')
		ENTRY = "0.000" # DEFAULT
		try:
			raise Exception
			ENTRY = ""
		except:
			pass
		if ENTRY != "":
			lisamoot.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(lisamoot)

		osakond = doc.createElement('osakond')
		ENTRY = "0" # DEFAULT
		try:
			raise Exception
			ENTRY = ""
		except:
			pass
		if ENTRY != "":
			osakond.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(osakond)

		firma = doc.createElement('firma')
		ENTRY = "" # DEFAULT
		try:
			raise Exception
			ENTRY = ""
		except:
			pass
		if ENTRY != "":
			firma.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(firma)

		isik = doc.createElement('isik')
		ENTRY = "0" # DEFAULT
		try:
			raise Exception
			ENTRY = ""
		except:
			pass
		if ENTRY != "":
			isik.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(isik)

		allikas = doc.createElement('allikas')
		ENTRY = "" # DEFAULT
		try:
			raise Exception
			ENTRY = ""
		except:
			pass
		if ENTRY != "":
			allikas.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(allikas)

		algdok = doc.createElement('algdok')
		ENTRY = "" # DEFAULT
		try:
			raise Exception
			ENTRY = ""
		except:
			pass
		if ENTRY != "":
			algdok.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(algdok)

		komplekt = doc.createElement('komplekt')
		ENTRY = "" # DEFAULT
		try:
			raise Exception
			ENTRY = ""
		except:
			pass
		if ENTRY != "":
			komplekt.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(komplekt)

		kokog = doc.createElement('kokog')
		ENTRY = "0.00" # DEFAULT
		try:
			raise Exception
			ENTRY = ""
		except:
			pass
		if ENTRY != "":
			kokog.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(kokog)

		kmprot = doc.createElement('kmprot')
		ENTRY = "20.00" # DEFAULT
		try:
			ENTRY = toode["VATRate"]
		except:
			pass
		if ENTRY != "":
			kmprot.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(kmprot)

		pkogus = doc.createElement('pkogus')
		ENTRY = "0.00" # DEFAULT
		try:
			raise Exception
			ENTRY = ""
		except:
			pass
		if ENTRY != "":
			pkogus.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(pkogus)

		hankeid = doc.createElement('hankeid')
		ENTRY = "" # DEFAULT
		try:
			raise Exception
			ENTRY = ""
		except:
			pass
		if ENTRY != "":
			hankeid.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(hankeid)

		triik = doc.createElement('triik')
		ENTRY = "" # DEFAULT
		try:
			ENTRY = toode["EAN"]
		except:
			pass
		if ENTRY != "":
			triik.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(triik)

		staatus = doc.createElement('staatus')
		ENTRY = "" # DEFAULT
		try:
			raise Exception
			ENTRY = ""
		except:
			pass
		if ENTRY != "":
			staatus.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(staatus)

		ahliik = doc.createElement('ahliik')
		ENTRY = "" # DEFAULT
		try:
			raise Exception
			ENTRY = ""
		except:
			pass
		if ENTRY != "":
			ahliik.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(ahliik)

		vhind = doc.createElement('vhind')
		ENTRY = "0.00" # DEFAULT
		try:
			raise Exception
			ENTRY = ""
		except:
			pass
		if ENTRY != "":
			vhind.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(vhind)

		valkood = doc.createElement('valkood')
		ENTRY = "" # DEFAULT
		try:
			raise Exception
			ENTRY = ""
		except:
			pass
		if ENTRY != "":
			valkood.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(valkood)

		vreasum = doc.createElement('vreasum')
		ENTRY = "0.00" # DEFAULT
		try:
			raise Exception
			ENTRY = ""
		except:
			pass
		if ENTRY != "":
			vreasum.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(vreasum)

		vkmsum = doc.createElement('vkmsum')
		ENTRY = "0.00" # DEFAULT
		try:
			raise Exception
			ENTRY = ""
		except:
			pass
		if ENTRY != "":
			vkmsum.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(vkmsum)

		tkood = doc.createElement('tkood')
		ENTRY = "" # DEFAULT
		try:
			ENTRY = toode["SellerProductId"]
		except:
			pass
		if ENTRY != "":
			tkood.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(tkood)

		UnitOfMeasure = doc.createElement('UnitOfMeasure')
		ENTRY = "EUR" # DEFAULT
		try:
			ENTRY = toode["Currency"]
		except:
			pass
		if ENTRY != "":
			UnitOfMeasure.appendChild(doc.createTextNode(ENTRY))
		tooterida.appendChild(UnitOfMeasure)

	print(doc.toprettyxml(indent = ' '))
	return doc


#inquiry = import_motoral("52852320200414.xml")
#doc = export_baltiautoosad(inquiry)

#print(inquiry)
