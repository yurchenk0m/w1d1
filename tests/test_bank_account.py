import pytest
from codes import BankAccount

def test_deposit():
    acc = BankAccount("Alice", 100)
    assert acc.deposit(50) == 150

def test_withdraw():
    acc = BankAccount("Alice", 100)
    assert acc.withdraw(30) == 70

def test_withdraw_insufficient():
    acc = BankAccount("Alice", 50)
    with pytest.raises(ValueError):
        acc.withdraw(100)

def test_invalid_deposit():
    acc = BankAccount("Alice", 100)
    with pytest.raises(ValueError):
        acc.deposit(-10)
