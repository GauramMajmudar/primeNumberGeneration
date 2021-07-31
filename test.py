from prime import get_prime_1, get_prime_2

def test1():
    assert get_prime_1(2, 10) == [2, 3, 5, 7]
    assert get_prime_2(2, 10) == [2, 3, 5, 7]

def test2():
    assert get_prime_1(10, 50) == [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    assert get_prime_2(10, 50) == [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

def test3():
    assert get_prime_1(0, 20) == "One or both the entered values are 0 or less. Please enter values greater than 0."
    assert get_prime_2(0, 20) == "One or both the entered values are 0 or less. Please enter values greater than 0."

def test4():
    assert get_prime_1(40, 10) == "First value cannot be greater than or equal to second value"
    assert get_prime_2(40, 10) == "First value cannot be greater than or equal to second value"