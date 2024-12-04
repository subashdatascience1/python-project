import unittest
import account as AccountClass

class Test(unittest.TestCase):
	accInfo = AccountClass.account()

	def test_check_password_length(self):
		print("Checking possible password\n")
		passwordList = ['abeautifulday', 'astrictboss', 'alovleyboss' ]
		for passwd in passwordList:
			print("Checking passowrd" + passwd + "\n")
			passInfo = self.accInfo.check_password_length(passwd)
			self.assertTrue(passInfo)

if __name__ == '__main__':
	unittest.main()


