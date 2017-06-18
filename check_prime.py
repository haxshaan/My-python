def is_prime(x):
    while True:
        if x > 2:
            for n in range(2, x):
                return x % n != 0
        elif x == 0:
            return False
        elif x == 1:
            return False
        elif x == 2:
            return True
            break
        else:
            return False
