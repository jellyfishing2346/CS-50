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
    secondJar = Jar(3)
    assert secondJar.capacity == 3

# String function
def test_str():
    jar = Jar()
    assert str(jar) == ''
    jar.deposit(1)
    assert str(jar) == '🍪'
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

# Deposit function
def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 0

# Withdraw function
def test_withdraw():
    jar = Jar()
    jar.deposit(3)
    jar.withdraw(2)
    assert jar.size == 1