
import unittest
from Mailroom_class import Donor, Donor_db

class MyFuncTestCase(unittest.TestCase):
	def test_donor_class(self):
		a = Donor("Foghorn Leghorn")
		a.add_donation(100)
		a.add_donation(200)
		self.assertEqual(a.sum_donation,300)
		self.assertEqual(a.number_of_donations,2)
		self.assertEqual(a.donation_average,150)
		b = Donor("Bugs Bunny",[500,600])
		self.assertEqual(b.sum_donation,1100)
		self.assertEqual(b.number_of_donations,2)
		self.assertEqual(b.donation_average,550)
		b.add_donation(700)
		self.assertEqual(b.sum_donation,1800)
		self.assertEqual(b.number_of_donations,3)
		self.assertEqual(b.donation_average,600)

	def test_donor_db_class(self):
		a = Donor("Foghorn Leghorn",[100,200])
		b = Donor("Bugs Bunny",[500,600])
		donor_db = Donor_db()
		donor_db.add_donor(a)
		donor_db.add_donor(b)
		self.assertEqual(donor_db.get_sorted_donors(),['bugs bunny','foghorn leghorn'])
		self.assertEqual(donor_db.num_donors(),2)
		self.assertEqual(donor_db.get_donor('Bugs Bunny'),b)

if __name__ == '__main__':
	unittest.main()
	