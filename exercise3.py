number  = input('Plese enter a number ')
number = int(number)

def is_even(num):
    if num % 2 == 0:
        return True
    if num % 2 != 0:
        return False

print(is_even(number))