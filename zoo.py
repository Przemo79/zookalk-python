wybor = int(input("Wybierz program: 1 - nazywanie zwierząt, 2 - obliczanie pola figur: "))
if wybor == 1:

	class Zoo:
		def __init__(self, imie, wiek):
			self.imie = imie
			self.wiek = wiek

	class Pies(Zoo):
		def voice(self):
			print("Hau, hau, łof, łof")
	class Kot(Zoo):
		def voice(self):
			print("Meow, meow, miau, miał")
	class Slon(Zoo):
		def voice(self):
			print("Tururu, tururu")
	class Monkey(Zoo):
		def voice(self):
			print("u u ah ah")
	
	imie_psa = str(input("Podaj imię psa: "))
	wiek_psa = str(input("Podaj wiek psa: "))
	pies = Pies(imie_psa, wiek_psa)
		
	imie_kota = str(input("Podaj imię kota: "))
	wiek_kota = str(input("Podaj wiek kota: "))
	kot = Kot(imie_kota, wiek_kota)

	imie_slonia = str(input("Podaj imię słonia: "))
	wiek_slonia = str(input("Podaj wiek słonia: "))
	slon = Slon(imie_slonia, wiek_slonia)
	
	imie_malpy = str(input("Podaj imię małpy: "))
	wiek_malpy = str(input("Podaj wiek małpy: "))
	malpa = Monkey(imie_malpy, wiek_malpy)

	print("Pies ma na imię " + imie_psa + " i ma " + wiek_psa + " lat.")
	pies.voice()
	
	print("Kot ma na imię " + imie_kota + " i ma " + wiek_kota + " lat.")
	kot.voice()
		
	print("Słoń ma na imię " + imie_slonia + " i ma " + wiek_slonia + " lat.")
	slon.voice()
		
	print("Małpa ma na imię " + imie_malpy + " i ma " + wiek_malpy + " lat.")
	malpa.voice()

elif wybor == 2:
	figura = int(input("Jaką figurę chcesz obliczyć? 1 - kwadrat, 2 - prostokąt, 3 - trójkąt, 4 - trapez, 5 - koło: "))
	if figura == 1:
		a = int(input("Podaj długość boku kwadratu: "))
		print("Pole tego kwadratu wynosi %s cm2." % (a ** 2))
	if figura == 2:
		a = int(input("Podaj długość pierwszego boku prostokąta: "))
		b = int(input("Podaj długość drugiego boku prostokąta: "))
		print("Pole tego prostokąta wynosi %s cm2." % (a * b))
	if figura == 3:
		a = int(input("Podaj długość boku trójkąta: "))
		h = int(input("Podaj długość wysokości padającej na ten bok: "))
		print("Pole tego trójkąta wynosi %s cm2." % ((a * h) / 2))
	if figura == 4:
		a = int(input("Podaj długość pierwszego boku trapezu: "))
		b = int(input("Podaj długość drugiego boku trapezu: "))
		h = int(input("Podaj długość wysokości padającej na ten bok: "))
		print("Pole tego trapezu wynosi %s cm2." % (((a + b) * h) / 2))
	if figura == 5:
		r = int(input("Podaj długość promienia koła: "))
		print("Pole tego koła wynosi %.2f cm2." % ((r ** 2) * 3.14))