def is_prime(number):
    if number <= 1:
        return False  # 1 and non-positive numbers are not prime

    if number <= 3:
        return True  # 2 and 3 are prime

    if number % 2 == 0 or number % 3 == 0:
        return False  # Numbers divisible by 2 or 3 are not prime


# check it
num = int(input("Enter a positive integer: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
