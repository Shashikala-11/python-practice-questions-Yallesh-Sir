a=(input('Enter a char:'))

####### Using built-ins
if a.isupper():
    print('Yes , its uppercase')
if a.islower():
    print('No, its lowercase')


####### Without built-ins
if a in "aeiou":
    print('Yes , its lowercase')
if a in "AEIOU":
        print('No, its uppercase')

