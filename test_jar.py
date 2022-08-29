import pytest
from jar import Jar

# Main function
def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()

# Instance function
def test_init():
    jar = Jar()
    assert jar.capacity == 12


# String function
def test_str():
    jar = Jar()
    jar.deposit(2)
    assert str(jar) == "🍪🍪"

# Deposit function
def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2

# Withdraw function
def test_withdraw():
    jar = Jar()
    jar.deposit(3)
    jar.withdraw(2)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.withdraw(4)