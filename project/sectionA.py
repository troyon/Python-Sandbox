# Program 1
# no = 5
# if no < 0:
#     print('The given no is negative')
# else:
#     print('The given no is positive')


# Program 2
# no = 13
# if no % 2 == 1:
#     print('The given no is odd')
# else:
#     print('The given no is even')
    
    
# Program 3
# ageofperson1 = 20
# ageofperson2 = 37

# if ageofperson1 > ageofperson2:
#     print('Person1 is elder')
# else:
#     print('Person2 is elder')

# Program 4
# year = 2020

# if year % 4 == 0:
#     print(year, 'is a leap year')
# else:
#     print(year , 'is not a leap year')


# Program 5
# age = 15

# if age > 18:
#     print('age is greater than 18')
# else:
#     print('age is not greater than 18')


# Program 6
# ageofcitizen = int(input("Input person's age: "))

# if ageofcitizen > 60:
#     print('person is a senior citizen')
# else:
#     print('person is not a senior citizen')
    
# Program 7

# no1 = 5
# no2 = 8

# if no1 < no2:
#     print('number 1 is lowest')
# else:
#     print('number 2 is lowest')


# Program 8

# no1 = 9
# no2 = 1
# no3 = 50

# if no1 > no2 and no1 > no3:
#     print('number 1 is greatest')
# elif no2 > no3 and no2 > no1:
#     print('number 2 is greatest')
# else:
#     print('number 3 is greatest')



# Program 9

# no = 11

# if no % 5 == 0 and no % 11 == 0:
#     print('The given no is divisible by 5 and 11')
# else:
#     print('The given no is not divisible by 5 and 11')


# # Program 10
# numbers = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
# no = int(input('Enter a no between 0 and 9: ')) 
# print(numbers[no])


# Program 11
# characters = ["a","e","i","o","u"]
# char = (input('Enter a character: ')).lower()

# if char in characters:
#     print('character is a vovel')
# else:
#     print('character is not a vovel')


# Program 12
print('1. Area of Circle')
print('2. Area of Square')
print('3. Area of Rectange')

tocalculate = int(input('Enter a no between 1 & 3: '))

if tocalculate == 1:
    r1 = int(input('Enter radius of circle '))
    a1 = (22 / 7) * (r1 ** 2)
    print('area =',a1)

elif tocalculate == 2:
    s = int(input('Enter sides of square '))
    a2 = s ** 2
    print('area =',a2)

elif tocalculate == 3:
    l = int(input('Enter length of rectangle '))
    b = int(input('Enter breadth of rectangle '))
    a3 = l * b
    print('area =',a3)

else:
    print('Invalid input')
