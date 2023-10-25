from project_first import password as p


def test_password():
    print("Example:")
    print(p.is_acceptable_password("short"))

    # These "asserts" are used for self-checking
    assert p.is_acceptable_password("short") == False
    assert p.is_acceptable_password("short54") == True
    assert p.is_acceptable_password("muchlonger") == True
    assert p.is_acceptable_password("ashort") == False
    assert p.is_acceptable_password("muchlonger5") == True
    assert p.is_acceptable_password("sh5") == False
    assert p.is_acceptable_password("1234567") == False
    assert p.is_acceptable_password("12345678910") == True
    assert p.is_acceptable_password("password12345") == True
    assert p.is_acceptable_password("PASSWORD12345") == True
    assert p.is_acceptable_password("pass1234word") == True

    print("The mission is done! Click 'Check Solution' to earn rewards!")

    assert p.print_password("mama")==False
    assert p.print_password("grandmam")==True
    assert p.print_password("baba")==False

    print("good code !!!!!")


