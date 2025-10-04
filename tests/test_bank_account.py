import unittest
from codes import BankAccount

class TestBankAccount(unittest.TestCase):
    def test_deposit(self):
        acc = BankAccount("Bob", 100)
        self.assertEqual(acc.deposit(40), 140)

    def test_deposit_wrong_type(self):
        acc = BankAccount("Bob", 50)
        with self.assertRaises(TypeError):
            acc.deposit("50")

    def test_withdraw(self):
        acc = BankAccount("Bob", 100)
        self.assertEqual(acc.withdraw(40), 60)

    def test_withdraw_negative(self):
        acc = BankAccount("Bob", 100)
        self.assertEqual(acc.withdraw(-40), 60)

    def test_withdraw_insufficient(self):
        acc = BankAccount("Bob", 50)
        with self.assertRaises(ValueError):
            acc.withdraw(100)

    def test_deposit_negative(self):
        acc = BankAccount("Bob", 50)
        with self.assertRaises(ValueError):
            acc.deposit(-10)

if __name__ == "__main__":
    unittest.main()
