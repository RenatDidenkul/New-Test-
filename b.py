def is_prime(a):
    if a %2 == 0 and a != 0:
        print("Число просте")
        return True
    else:
        print("Число складове")
        return False

a = int(input("Enter a number: "))
print(is_prime(a))