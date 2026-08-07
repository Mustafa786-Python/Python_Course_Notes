# Write a python program using function to convert Celsius to Fahrenheit.
print(
    "                    \033[1mWelcome to the Celcious to Fahrenheit convertor!\033[0m")


def c_to_f(celcius):
    fahrenheit = 1.8 * celcius + 32
    data = f"The temperature is \033[1m{fahrenheit:.2f}\033[0m Fahrenheit"
    return data


# We can take from the user and print
# celcius = float(input("Enter temperature in celcious: "))

# We can store different result of functions in variables
temp = c_to_f(25.445345)
print(temp)
temp1 = c_to_f(50)
print(type(temp1))
