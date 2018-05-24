#Mailroom_OO

import sys
import json
import unittest 

#If a function works with a single donor, it will be in this class
class Donor:
	def __init__(self,Name,donations = None): #add default parameters for donations
		self.Name = Name
		self.donations = [] if donations is None else donations 

	def add_donations(self,donation):
		 self.donations.append(donation)

	@property
	def Name(self):
		return self.Name

	@property
	def donations(self):
		return self.donations

	@property
	def sum_donation(self, donations):
		return sum(self.donations)

	@property
	def number_of_donations(self,donations):
		return len(self.donations)

	@property
	def donation_average(self,donations):
		return average(self.donation)

	# def __repr__(self):
	# 	return "Circle({})".format(self.radius) 


#If a function works with multiple donors, it will be in this class
class Donor_db:
	def __init__(self):
		self.donors = {}

	def add_donor(self,donor):
		self.donors[donor.name.lower()] = donor

	def total_donors(self,donor_name):
		return self.donors[donor_name.lower()].sum_donation

	 def get_donor(self, donor_name):
        return self.donors[donor_name.lower()]

	@property
	def numberofdonors(self):
		return len(self.donors)





#################################################################################

Db = Donor_db()

def create_db():
	#a = Donor("Bill Gates")
	#add donations to Donor using method
	Donors["Bill Gates"] = [10000,12000]
	Donors["Jeff Bezos"]=[50]
	Donors["Mark Zuckerberg"] = [500,600,700]
	Donors["Paul Allen"] = [250,350,450]
	Donors["King of Siam"] = [200,250]

def get_Db():
	return Db 
	

def print_Db():
	for x,v in Db.items(): #modify to get proper name of donor
		print("\n{} donated ${}".format(x,v)) 

def thankall():
	for x in Db:
		totaldonated = sum(Donors[x]) #call property of donor that calculates total donations
		letterofthanks(x,totaldonated)

def letterofthanks(donorname,totaldonated): #Potentially create method for letterofthanks within donor class
	#To add sum of donations
	filename = donorname+".txt"
	f = open(filename,"w+")
	statementtowrite = "Thank you "+donorname+" for your donation of $"+str(totaldonated)+". We greatly appreciate your help."
	f.write(statementtowrite)
	f.close()
	print("\nLetter of thanks has been saved to hard disk as text file under "+str(filename))

def sumdonor(thankdonor): #redundant - refactor to remove this
	return sum(Donors[thankdonor])

def searchdonors(thankdonor):
		try:
			print(Donors[thankdonor])
			totaldonated = sumdonor(thankdonor)
			letterofthanks(thankdonor,totaldonated)
		except KeyError:
			print("\nThat donor doesn't exist")


def newdonation():
	newdonor = input("Input name of new donor\n")
	while len(str.strip(newdonor)) == 0:
		newdonor = input("Invalid input, enter name of new donor\n")
	newdonor = str.strip(newdonor)
	Donors[newdonor] = []
	donationsdone = False
	newdonations = []
	while donationsdone is False:	
		donation = input("Input donations or hit enter when done\n")
		if donation == "":
			donationsdone = True 
		else:
			try:
				newdonations.append(float(donation))
			except ValueError:
				print("Enter number or hit enter - no letters!")
	#print("Donations is/are {}".format(newdonations))
	Donors[newdonor] = newdonations
	printdonors()

def thanks():
	thankdonor = input("\nPlease enter full name of donor you'd like to thank or list to view donors\n")
	if thankdonor == "list":
		printdonors()
		thanks()
	else:
		searchdonors(thankdonor)

def report():
	sorteddonors = sorted(Donors)
	print(sorteddonors)


def mainloop():
	createlist()
	print("Introducing Mailroom!")
	done = False
	while done is False:
		print("\nWhat do you want to do?")
		print("\n (1) Send a thank you\n", "(2) Create a Report,\n", "(3) Send letters to everyone,\n","(4) Add donor \n", "(5) Quit")
		response = input(">> ")
		print("response was,",response)
		if response =="1":
			print("\nYou have chosen the 'Thank' option")
			thanks()
		elif response == "2":
			report()
		elif response == "3":
			thankall()
		elif response == "4":
			newdonation()
		else:
			print("\nSee you later!")
			done = True 


if __name__ == "__main__":
	mainloop()
