class SaveStats():

	def __init__(self, aika, pelaaja):
		self.aika = aika
		self.pelaaja = pelaaja

		self.filehandler()

	def filehandler(self):
		try:
			self.f = open("sav.txt", "r")
			line = self.f.readlines()
			count = len(line)
			self.f.seek(0)
			for i in line:
				if self.pelaaja in i:
					arr = i.split("|")
					if float(arr[1]) > self.aika:
						self.f.close()
						self.deleteline()
						self.f = open("sav.txt","a")
						self.f.write("{:s}|{:f}\n".format(self.pelaaja,self.aika))
				else:
					count -= 1
			self.f.close()
			self.f = open("sav.txt", "a")

			if count == 0:
				self.f.write("{:s}|{:f}\n".format(self.pelaaja,self.aika))
			
			self.f.close()

		except FileNotFoundError:
			with open("sav.txt", "w+") as f:
				f.write("{:s}|{:f}\n".format(self.pelaaja,self.aika))
			
	def deleteline(self):
		with open("sav.txt","r+") as f:
			lines = f.readlines()
			f.seek(0)
			for line in lines:
				if self.pelaaja not in line:
					f.write(line)
			f.truncate()