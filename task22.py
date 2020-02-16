def convert():
    a = float(input('Farenheit for convertation: '))
    b = (a - 32) * (5 / 9)
    return b
print(convert(), 'celcius')

def reverse_conv():
    a = float(input('Celcius for convertation: '))
    b = (a * 9 / 5) + 32
    return b
print(reverse_conv(), 'farenheit')