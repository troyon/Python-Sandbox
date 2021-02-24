name = input('Enter your name: ')
age = int(input('Enter your age: '))


if age > 19:
    print('Your name is',name,'and you are an Adult')
elif age > 12:
    print('Your name is', name, 'and you are a teenager')
else:
    print('Your name is', name, 'and you are a kid')
