#Mailroom_OO

import sys
import json
import unittest 
import math 

#If a function works with a single donor, it will be in this class
class Donor:
	def __init__(self,name,donations = None): #add default parameters for donations
		self._name = name
		self._donations = [] if donations is None else donations 

	def add_donation(self,donation):
		self._donations.append(donation)

	@property
	def name(self):
		return self._name

	@property
	def donations(self):
		return self._donations

	@property
	def sum_donation(self):
		return sum(self._donations)

	@property
	def number_of_donations(self):
		return len(self._donations)
#My ipython was going nuts so I had to manually calculate the average >=(
	
	@property
	def donation_average(self):
		return sum(self._donations)/len(self._donations)

	# def __repr__(self):
	# 	return "Circle({})".format(self.radius) 


#If a function works with multiple donors, it will be in this class
class Donor_db:
	def __init__(self):
		self._donors = {}

	def add_donor(self,donor):
		self._donors[donor.name.lower()] = donor

	def all_donors_donations(self):
		total_sum = 0
		for x,v in self.donors.items():
			total_sum = total_sum + sum(v)
		return total_sum

	def get_donor(self, donor_name):
	 	return self._donors[donor_name.lower()]

	def print_Db(self):
		for name,donor_obj in self._donors.items(): 
			print("\n{} donated individual donations of ${} for a total of ${}".format(name,donor_obj.donations,donor_obj.sum_donation))

	def get_sorted_donors(self): 
		return sorted(self._donors)

	@property
	def numberofdonors(self):
		return len(self._donors)

#################################################################################


def create_db():
	a = Donor("Bill Gates")
	a.add_donation(10000)
	a.add_donation(12000)
	b = Donor("Jeff Bezos")
	b.add_donation(50)
	c = Donor("Mark Zuckerberg")
	c.add_donation(500)
	c.add_donation(600)
	c.add_donation(700)
	d = Donor("Paul Allen")
	d.add_donation(250)
	d.add_donation(350)
	d.add_donation(450)
	e = Donor("King of Siam")
	e.add_donation(200)
	e.add_donation(250)
	donor_db = Donor_db()
	donor_db.add_donor(a)
	donor_db.add_donor(b)
	donor_db.add_donor(c)
	donor_db.add_donor(d)
	donor_db.add_donor(e)
	return donor_db

def thankall(db):
	for name in db.get_sorted_donors():
		donor = db.get_donor(name)
		totaldonated = donor.sum_donation
		letterofthanks(name,totaldonated)

def letterofthanks(donorname,totaldonated): #Potentially create method for letterofthanks within donor class
	#To add sum of donations
	filename = donorname+".txt"
	f = open(filename,"w+")
	statementtowrite = "Thank you "+donorname+" for your donation of $"+str(totaldonated)+". We greatly appreciate your help."
	f.write(statementtowrite)
	f.close()
	print("\nLetter of thanks has been saved to hard disk as text file under "+str(filename))

# def sumdonor(thankdonor): #redundant - refactor to remove this
# 	return sum(Donors[thankdonor])

def searchdonors(thankdonor,db):
		try:
			#print(db[thankdonor])
			donor = db.get_donor(thankdonor)
			totaldonated = donor.sum_donation
			letterofthanks(thankdonor,totaldonated)
		except KeyError:
			print("\nThat donor doesn't exist")


def newdonation(db):
	newdonor = input("Input name of new donor\n")
	while len(str.strip(newdonor)) == 0:
		newdonor = input("Invalid input, enter name of new donor\n")
	newdonor = str.strip(newdonor)
	try:
		newdonor_object = db.get_donor(newdonor)
	except:	
		newdonor_object = Donor(newdonor)
	donationsdone = False
	while donationsdone is False:	
		donation = input("Input donations or hit enter when done\n")
		if donation == "":
			donationsdone = True 
		else:
			try:
				newdonor_object.add_donation(float(donation))
			except ValueError:
				print("Enter number or hit enter - no letters!")
	#print("Donations is/are {}".format(newdonations))
	db.add_donor(newdonor_object)
	db.print_Db()

def thanks(db):
	thankdonor = input("\nPlease enter full name of donor you'd like to thank or list to view donors\n")
	if thankdonor == "list":
		db.print_Db()
		thanks(db)
	else:
		searchdonors(thankdonor,db)

def report(db):
	sorteddonors = db.get_sorted_donors()
	print(sorteddonors)


def mainloop():
	donor_database = create_db()
	print("Introducing Mailroom!")
	done = False
	while done is False:
		print("\nWhat do you want to do?")
		print("\n (1) Send a thank you\n", "(2) Create a Report,\n", "(3) Send letters to everyone,\n","(4) Add donor \n", "(5) Quit")
		response = input(">> ")
		print("response was,",response)
		if response =="1":
			print("\nYou have chosen the 'Thank' option")
			thanks(donor_database)
		elif response == "2":
			report(donor_database)
		elif response == "3":
			thankall(donor_database)
		elif response == "4":
			newdonation(donor_database)
		else:
			print("\nSee you later!")
			done = True 


if __name__ == "__main__":
	mainloop()


