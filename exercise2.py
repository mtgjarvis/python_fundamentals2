number  = input('Plese enter a number ')
number = int(number)

def negative(num):
    if num > 0:
        return True
    if num < 0:
        return False

print(negative(number))