temp = input('Please enter a temperature in Fahrenheit ')
temp = int(temp)

def f2c(user_temp):
    user_temp = (temp - 32) * 5 / 9
    return user_temp

print(f2c(temp))